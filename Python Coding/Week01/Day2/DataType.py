# 파이썬이 처리하는 자료형 (data type)
# 정수(integer)(int) : (2진수, 8진수, 10진수, 16진수)
# 실수(float) : (3.14)(1.2e3)
# 문자열(String)(str) : (' ')(" ")
# 불린(bool) : (True)(False)

a=100
b=3.14
c="name"
d=True

print("100의 자료형: ",type(a))
print("3.14의 자료형: ",type(b))
print("name의 자료형: ",type(c))
print("True의 자료형: ",type(d))
print("")

# 형변환 (type 변환)
# 1.str() : 문자열로 변환
print("str(a):",type(str(a)))

str1 = str(123)
str2 = str(3.14)

# 2.int(문자열) : 정수형으로 변환
print(int(b),":",type(int(b)),"\n")
print("int(str1):",int(str1))


# 3. float(문자열) : 실수로 변환
print("float(str2):",float(str2),"\n")

# int으로 변환하되, 진수를 명시
print("1010을 2진수로 변환: ",int('1010',2),"(2)")
print("1010을 8진수로 변환: ",int('1010',8),"(8)")
print("1010을 16진수로 변환: ",int('1010',16),"(16)")


print(int('AAF', 16))
print(bin(12))
print(hex(12))
print(oct(12))
