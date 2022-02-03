# 매직 메서드/ 특별한 메서드
# __메서드이름__ : 미리 정의되어 있는 메서드

# __ge__() : >=
# __gt__() : >
# __le__() : <=
# __lt__() : <
# __ne__() : !=
# __eq__() : ==
# __init__() : 생성자
# __repr__() : 만들어진 인스턴스를 print()문으로 출력
# __add__() : +
# __del__() : 소멸자 메서드, 인스턴스를 삭제할 때 (메모리에서 완전 삭제)

# 선 (line)
# 필드 : 길이, 색상, 두께
# 메서드 : 길이 간 더하기/빼기, 크기 비교


class Line :
    def __init__(self,length=0,color='black'):
        self.length = length
        print(f'길이 {self.length}의 선분 생성됨')

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __mul__(self, other):
        return self.length * other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __ne__(self, other):
        return self.length != other.length

    def __eq__(self, other):
        return self.length == other.length

    def __repr__(self):
        return f'선의 길이 : {self.length}'

    # def __del__(self):
    #     print(f'{self.length} 길이의 선분이 삭제되었습니다.')




line1 = Line(30)
line2 = Line(20)
print('-'* 80)

print('line1 + line2 = ',line1+line2)
print('line1 - line2 = ',line1-line2)
print('line1 * line2 = ',line1*line2)
print('line1 > line2 = ',line1 > line2)
print('line1 >= line2 = ',line1 >= line2)
print('line1 < line2 = ',line1 < line2)
print('line1 <= line2 = ',line1 <= line2)
print('line1 != line2 = ',line1 != line2)
print('line1 == line2 = ',line1 == line2)
print('-'* 80)

print(line1)
print(line2)
print('-'* 80)