# 2021-12-20 변수
# 1. 값이 저장된 메모리의 위치를 가리키는 레퍼런스다
# 2. 값의 형에 따라서 고정되지 않고, 동적으로 자료 유형을 매핑해서 사용
#    (type 검사)(자료형 지정 x)(동적 타이핑)
#    자바: int x 처럼 변수에 대한 type를 고정시켜야 함
# 3. 변수는 이름을 가지고 있다
# 4. 변수에는 다른 값을 저장할 수 있다.(값 변경 가능)(2번과 같은 내용)
# 5. 변수는 선언이 필요없다.

x = 10  # 리터럴
print("x:", x) #x 값을 출력하기
id(x)  # 변수가 가리키는 값의 실제 주소
print("type(x):",type(x)) #변수가 가리키는 값의 형식
print("-----------------------------------")


y="hello"
print("y:",y)
print("type(y):",type(y))
print("")

y=100 # 형변환 가능
print("y:",y)
print("type(y):",type(y))
print("")

y=[20,30,40]  # 리스트
print("y:",y)
print("y[0]:",y[0])
print("y[1]:",y[1])
print("y[2]:",y[2])
print("type(y):",type(y))
print("-----------------------------------")

z = y[0]+10.0
print("z:",z)
print("type(z):",type(z))



ins, outs='python',''
strl = len(ins)
for i in range(0,strl):
    outs += ins[strl-(i+1)]
print(outs)







