class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def print(self):
        print(f"({self.getX()}, {self.getY()})", end='')


class ColorPoint(Point):
    def __init__(self, x=0, y=1, color="xanh"):
        super().__init__(x, y)
        self.__color = color

    def read(self):
        data = input().split()
        self.setXY(int(data[0]), int(data[1]))
        self.__color = ' '.join(data[2:])

    def print(self):
        super().print()
        print(f": {self.__color}")

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color


class C002454:
    @staticmethod
    def testCase1():
        print("Test case 1:")
        A = ColorPoint(5, 10, "trang")
        A.print()
        print("Constructor: PASS\n")

    @staticmethod
    def testCase2():
        B = ColorPoint()
        print("Nhap toa do va mau diem B (ví dụ: 1 2 do):")
        B.read()
        B.move(10, 8)
        print("Sau khi di chuyen:")
        B.print()
        print()

    @staticmethod
    def testCase3():
        print("Test case 3:")
        C = ColorPoint(6, 3, "den")
        D = ColorPoint(C.getX(), C.getY(), C.getColor())
        print("D ban đau:")
        D.print()
        D.setColor("vang")
        print("D sau khi doi mau:")
        D.print()
        print("C khong đoi:")
        C.print()
        print("Constructor: PASS")
        print("Set color: PASS\n")

    @staticmethod
    def main():
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()


# Chạy chương trình chính
if __name__ == "__main__":
    C002454.main()
