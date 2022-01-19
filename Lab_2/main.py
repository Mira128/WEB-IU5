from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rectangle = Rectangle("синего", 10, 5)
    circle = Circle("зеленого", 15)
    square = Square("красного", 15)
    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()