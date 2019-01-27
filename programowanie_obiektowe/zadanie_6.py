class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)


    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int):
            return Vector(self.x *other, self.y * other)
        return NotImplemented

    def __lt__(self, other):
        return self.lenght() < other.lenght()

    def __gt__(self, other):
        return f"[{self.x}, {self.y}]"

    def lenght(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


    # def __lt__(self, other):
    #     if isinstance(other, Vector):
    #         if self.x * self.y < other.x * other.y:
    #             return True
    #         return False
    #
    # def __gt__(self, other):
    #     if isinstance(other, Vector):
    #         if self.x *



def test_vector_init():
    vector_1 = Vector(x=1, y=2)
    assert vector_1.x == 1
    assert vector_1.y == 2

def test_vector_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 2
    assert vector_3.y == 4

def test_vector_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == 0
    assert vector_3.y == 0

def test_vector_mul():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    assert vector_1 * vector_2 == 1*1 + 2*2


def test_vector_mul_int():
    vector_1 = Vector(x=1, y=2)
    vector_2 = vector_1 * 5
    assert vector_2.x == 5
    assert vector_2.x == 10

    vector_2 = 6 * vector_1
    assert vector_2.x == 6
    assert vector_2.y == 12

def test_vector_lt():
    assert Vector(1, 1) < Vector(1, )









