import unittest
from ec import EllipticCurve, POINT_ON_INF
from wrapper import ECPoint, isOnCurveCheck, scalarMult
from random import randrange

class TestEllipticCurve(unittest.TestCase):
    def setUp(self):
        self.p = int("ffffffffffffffffffffffffffffffff000000000000000000000001", 16)
        self.a = -3
        self.b = int("b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4", 16)
        self.G_x = int("b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21", 16)
        self.G_y = int("bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34", 16)
        self.G = ECPoint(self.G_x, self.G_y)
        self.P_224 = EllipticCurve(self.a, self.b, self.p)
        self.order = 26959946667150639794667015087019625940457807714424391721682722368061

    def test_PisOnCurveCheck(self):
        Q = scalarMult(self.P_224, self.order - 1, self.G)
        self.assertTrue(isOnCurveCheck(self.P_224, Q))


    def test_identityEl(self):
        L = scalarMult(self.P_224, self.order, self.G)
        self.assertEqual(L, POINT_ON_INF)

    def test_eccProp(self):
        # k*(d*G) = d*(k*G)
        k = randrange(256)
        d = randrange(256)

        H1 = scalarMult(self.P_224, d, self.G)
        H2 = scalarMult(self.P_224, k, H1)

        H3 = scalarMult(self.P_224, k, self.G)
        H4 = scalarMult(self.P_224, d, H3)
        
        self.assertTrue(H2.x == H4.x and H2.y == H4.y)


if __name__ == '__main__':
    unittest.main()
