class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vector is ({self.x}, {self.y})")


class vector3d(vector2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The vector is ({self.x}, {self.y}, {self.z})")


o = vector2d(3, 4)
b = vector3d(5, 6, 7)
b.show()
o.show()