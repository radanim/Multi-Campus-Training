# 문자열 정렬 : 정렬 문자 < > ^
# 문자 : 왼쪽 정렬, 숫자 : 오른쪽 정렬
# 1. < : 왼쪽 정렬
string = 'python'
num = 1234
print('string: ',string)
print('left: {:-<10}'.format(string)) #왼쪽 정렬
print('right: {:->10}'.format(string)) #오른쪽 정렬
print('center: {:-^10}'.format(string)) #가운데 정렬
print('----------------------------------------')

print('num: ',num)
print('{:6d}'.format(num))
print('{:06d}'.format(num))
print('----------------------------------------')

#  ljust(자릿수) : 왼쪽 정렬
#  rjust(자릿수) : 오른쪽 정렬
#  center(자릿수) : 가운데 정렬

print(string.ljust(10))
print(string.rjust(10))
print(string.center(10))