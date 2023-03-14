import numpy as np

def rotation_matrix_3d(frm, to):
    if np.array_equal(frm, to):
        return np.identity(3)
    if np.array_equal(frm, -to):
        return -np.identity(3)
    s = frm + to
    return 2.0 * np.outer(s, s) / np.dot(s, s) - np.identity(3)

if __name__ == '__main__':
    #r = np.random.random()
    #a = generate(r)
    #b = generate(r)
    a = np.array([-np.sqrt(3)/2, 0, -1/2])          #ガンの単位方向ベクトル
    b = np.array([0, 0, -np.linalg.norm(a)])        #Fixed!
    r = rotation_matrix_3d(a, b)
    #r_T = r.T
    c = np.array([-1/2, 1, np.sqrt(3)/2])

    # test
    print(" R =", r)
    print()
    print(" a =", a)
    print("Ra =", np.dot(r, a))
    print(" b =", b)
    print(" x =", -np.dot(r, c))
