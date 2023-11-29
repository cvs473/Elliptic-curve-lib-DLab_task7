from ec import EllipticCurve, POINT_ON_INF
from dataclasses import dataclass
from random import randrange

@dataclass
class ECPoint:
    x: int
    y: int


def isOnCurveCheck(self: EllipticCurve, point: ECPoint):
		return self.equalModP(point.y ** 2, point.x ** 3 + self.a * point.x + self.b)

def addECPoints(self: EllipticCurve, P1, P2):
		if P1 == POINT_ON_INF:
			return P2
		if P2 == POINT_ON_INF:
			return P1

		x1, y1 = P1.x, P1.y
		x2, y2 = P2.x, P2.y

		if self.equalModP(x1, x2) and self.equalModP(y1, -y2):
			return POINT_ON_INF

		if self.equalModP(x1, x2) and self.equalModP(y1, y2):
			u = self.reduceModP((3 * x1 * x1 + self.a) * inverseModP(self, 2 * y1))
		else:
			u = self.reduceModP((y1 - y2) * inverseModP(self, x1 - x2))

		v = self.reduceModP(y1 - u * x1)
		x3 = self.reduceModP(u * u - x1 - x2)
		y3 = self.reduceModP(-u * x3 - v)
		return ECPoint(x3, y3)


def scalarMult(self: EllipticCurve, k, P: ECPoint):
		Q = POINT_ON_INF
		while k != 0:
			if k & 1 != 0:
				Q = addECPoints(self, Q, P)
			P = addECPoints(self, P, P)
			k >>= 1
		return Q

def inverseModP(self: EllipticCurve, x):
		if self.reduceModP(x) == 0:
			return None
		return pow(x, self.p - 2, self.p)
