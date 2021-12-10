class object:
    pass
class X(object):
    pass
class Y(object):
    pass
class Z(object):
    pass
class A(X):
    pass
class A(Y):
    pass
class B(Y):
    pass
class B(Z):
    pass
class M(A):
    pass
class M(B):
    pass
class M(Z):
    pass