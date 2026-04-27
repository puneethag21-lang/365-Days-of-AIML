marks = 95  
match marks:
    case m if 90 <= m <= 100:
        print('A+')
    case m if 80 <= m < 90:
        print('A')
    case m if 70 <= m < 80:
        print('B')
    case _:
        print('Below B')