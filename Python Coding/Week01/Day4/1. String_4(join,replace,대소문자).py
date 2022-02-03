# 문자열 결합 메소드
# join() : 각 문자 사이에 특정문자(열) 삽입 후 결합
a = '-'
b = 'bb'

c = a.join('bbb')
print('a.join(bbb):',c)

c = a.join(b)
print('a.join(bb):',c)

c = a.join('1234')
print('a.join(1234):',c)
print('------------------------------------------------')

# replace() : 문자열 변경 메소드
# 전체 문자열에서 특정 문자열을 찾아서 다른 문자열로 변경
# 찾는 문자열이 존재하면 변경할 문자열로 대체 후 반환
# 찾는 문자열이 존재하지 않으면 원래 문자열 반환

lan = 'Python programming'
lan_rep = lan.replace('Python','Java')
print(lan_rep)

# 대소문자 변경 메소드
# 1. upper() : 대문자로 변경
# 2. lower() : 소문자로 변경
# 3. capitalize() : 문장의 첫 문자열의 첫 문자를 대문자로 변경
# 4. swapcase() : 문자의 첫 문자열의 첫 문자를 소문자로 변경, 나머지는 대문자
# 4. title() : 각 단어의 첫 문자를 대문자로 변경

upper_lan = lan.upper()
lower_lan = lan.lower()
capitalize_lan = lan.capitalize()
swapcase_lan = lan.swapcase()
title_lan = lan.title()

print(upper_lan)
print(lower_lan)
print(capitalize_lan)
print(swapcase_lan)
print(title_lan)

# 공백 제거 메소드
# 1. strip(): 문자열의 앞 뒤의 공백을 제거
# 2. lstrip() : 문자열의 왼쪽의 공백을 제거
# 3. rstrip() : 문자열의 오른쪽의 공백을 제거

string = '   ---python---      '
print(string.strip())
print(string.lstrip())
print(string.rstrip())




