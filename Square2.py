class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class Square:
    name = '사각형'
    msg = "가로와 세로? > "
    def __init__(self):
        print("a rect is created")
    
    def input_data(self):
        datum = input(self.msg)
        if isinstance(self, Foursquare):
            x = Casting.to_int(datum)
            self.__init_area(x, x)
        else:
            data = datum.split(',')
            x, y = Casting.to_int(data[0]), Casting.to_int(data[1])
            self.__init_area(x, y)

    def __init_area(self, x, y):
        area = x * y
        print("{}의 넓이는 {}입니다.".format(self.name, area))

class Rectangle(Square):
    name = '직사각형'
    msg = "가로와 세로는??(입력예: 10,20) > "


class Parallelogram(Square):
    name = '평행사변형'
    msg = "밑변과 높이는??(입력예: 10,20) > "
   
class Foursquare(Square):
    name = '정사각형'
    msg = "한변의 길이는??(입력예: 10) > "

all_squares = [Square(), Rectangle(), Parallelogram(), Foursquare()]

first_msg = "사각형의 종류는\n"
for i, r in enumerate(all_squares):
    if i == 0: continue
    first_msg += "{:d}) {}\n".format(i, r.name)

first_msg += "(quit: q) >>"
while(True):
    print()
    square_type = input(first_msg)
    if square_type == 'q':
        break
    
    square_index = Casting.to_int(square_type)
    if square_index < 0 or square_index >= len(all_squares) :
        square_index = 0

    square = all_squares[square_index]
    square.input_data()
   
     




