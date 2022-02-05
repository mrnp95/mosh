#copyright

import numpy as np
from sympy import *
from scipy.spatial.transform import Rotation as R


def rot(phi, theta, psi, degree):
    """
    Rotation matrix, given the Euler angles.
    :param phi: rotation around x-axis
    :param theta: rotation around y-axis
    :param psi: rotation around z-axis
    :param degree: Bool --> True if angles in degrees
    :return: rotation matrix.
    """
    r = R.from_euler('xyz', [phi, theta, psi], degrees=degree)
    return r.as_matrix()


def r_e_h(p_0, d, m):
    """
    The eye vector in head reference frame.
    :param p_0:
    :param d:
    :return: 3x1 vector.
    """
    return np.array([[p_0[0] + m * d[0]], [p_0[1] + m * d[1]], [p_0[2] + m * d[2]]])


def solve_m(x0, y0, r_e_I, m):
    """
    Solving for 'm'.
    :param x0: screen intersection point with x-axis
    :param y0: screen intersection point with y-axis
    :param r_e_I: Parameterised eye vector in terms of 'm'
    :return: 'm'.
    """
    f = y0*(r_e_I[0] - x0) + x0*r_e_I[1]
    return solve(f, m)