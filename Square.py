class Square:
    x, y = 0, 0
    def __init__(self):
        print("a rect is created")

class Rectangle(Square):
    def area(self, x, y):
        return x * y

class Parallelogram(Square):
    def area(self, x, y):
        return x * y

square_type = input("사각형의 조류는?\n 1)직사각형\n 2)평행사변형\n >> ")

if square_type == '1':
    rect = Rectangle()
    input_value = input("가로와 세로는??(입력예: 10,20)")
    input_x, input_y = input_value.split(',')
    x = int(input_x)
    y = int(input_y)
    result = rect.area(x, y)
    print(f"직사각형의 넓이는 {result}입니다.")
else:
    rect = Parallelogram()
    input_value = input("밑변과 높이는??(입력예: 10,20)")
    input_x, input_y = input_value.split(',')
    x = int(input_x)
    y = int(input_y)
    result = rect.area(x, y)
    print(f"평행사변형의 넓이는 {result}입니다.")




