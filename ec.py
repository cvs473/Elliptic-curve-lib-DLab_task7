POINT_ON_INF = None

class EllipticCurve:
    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p
        self.defineDiscriminant()
        if self.discriminant == 0:
            print("This elliptic curve is singular")

    def defineDiscriminant(self):
        D = -16 * (4 * (self.a ** 3) + 27 * (self.b ** 2)) 
        self.discriminant = self.reduceModP(D)

    def reduceModP(self, x):
        return x % self.p 

    def equalModP(self, x, y):
        return self.reduceModP(x - y) == 0
