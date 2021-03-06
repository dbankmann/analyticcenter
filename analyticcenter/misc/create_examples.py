##
## Copyright (c) 2019
##
## @author: Daniel Bankmann
## @company: Technische Universität Berlin
##
## This file is part of the python package analyticcenter
## (see https://gitlab.tu-berlin.de/PassivityRadius/analyticcenter/)
##
## License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
##
import numpy as np

from analyticcenter.linearsystem import WeightedSystem
from analyticcenter.algorithm import get_algorithm_object
import control
from misc.misc import check_positivity


def generate_random_sys_and_save(m, n):
    while True:
        A = np.random.rand(n, n)
        B = np.random.rand(n, m)
        C = np.random.rand(m, n)
        D = np.random.rand(m, m)
        Q = np.random.rand(n, n)
        Q = Q @ Q.T
        S = 0.01 * np.random.rand(n, m)
        R = np.random.rand(m, m)
        R = R @ R.T
        sys = WeightedSystem(A, B, C, D, Q, S, R)
        alg = get_algorithm_object(sys, 10 ** (-3))
        if sys._check_positivity(sys.H0):
            continue
        if sys._check_positivity(alg._get_H_matrix(alg._get_initial_X())):
            break

    sys.save()


def generate_random_sys_and_save_2(m, n):
    while True:
        roots = -np.random.randint(1, 100, n)
        A = np.diag(roots)



        B = np.random.rand(n, m)
        C = np.random.rand(m, n)
        D = 10*np.random.rand(m, m)
        ss = control.ss( A, B, C, D)
        tf = control.ss2tf(ss)
        ss = control.tf2ss(tf)


        sys = WeightedSystem(ss.A, ss.B, ss.C, ss.D, np.zeros(n, n), ss.C.H, ss.D + ss.D.H)
        alg = get_algorithm_object(sys, 10 ** (-3))
        if sys._check_positivity(sys.H0):
            continue
        if sys._check_positivity(alg._get_H_matrix(alg._get_initial_X())):
            break

    sys.save()

def generate_random_sys_and_save_3(m, n):
    while True:
        print("new")



        ss = control.matlab.rss(n, m, m)


        ss.D = 100 * np.asmatrix(np.ones((m,m)))
        R = ss.D + ss.D.H
        ss.A = 10 * ss.A
        # ss.B = 1/10 * ss.B
        ss.C = 1/10 * ss.C
        sys = WeightedSystem(ss.A, ss.B, ss.C, ss.D, np.zeros((n, n)), ss.C.H, R)
        X = control.care(ss.A, ss.B, np.zeros((n,n)), R, ss.C.H, np.identity(n))[0]

        alg = get_algorithm_object(sys, 10 ** (-3))

        if check_positivity(-X):
            break

    sys.save()

def generate_pH_sys_and_save(n,m):
    dim = n+m
    R = np.asmatrix(np.random.random((dim,dim)))
    H = R.T @ R
    A = -0.5 * H[:n, :n]
    B = - 0.5 * H[:n,n:]
    C = - B.T
    D = 0.5 * H[n:, n:]
    R = D + D.T
    sys = WeightedSystem(A, B, C, D, np.zeros((n, n)), C.H, D + D.T)
    # Xm = control.care(A, B, np.zeros((n,n)), R, C.H, np.identity(n))[0]
    # Xp = control.care(-A, B, np.zeros((n,n)), -(D + D.T), C.H,np.identity(n))[0]
    alg = get_algorithm_object(sys, 10 ** (-3))
    #
    # check_positivity(-Xm)
    # check_positivity(-Xp)



    sys.save()
