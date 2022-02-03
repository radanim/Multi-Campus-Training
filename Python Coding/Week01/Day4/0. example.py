# format() 함수 사용
# string.format()

print((format(1.234567),'10.3f'))
print('Name:{0}, Phone: {1}'.format('kim', '1234-213'))

print('%d' % 123)
print('%5d' % 123)
print('%05d' % 123)
print('------------------------------------')
# f'String 사용
print(f'{1.234}')

tea = 'coffee'
n = 5
s3 = f'나는 {tea}를 좋아합니다. 하루에 {n}잔 마셔요'
print(s3)
print("------------------------------------")

for month in ['1월','2월','3월']:
    print(f'이번달은 {month}입니다.')