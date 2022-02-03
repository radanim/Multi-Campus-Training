from datetime import date, datetime, timedelta

today = date.today()
year = today.year
month = today.month
day = today.day
print(f'{year}년 {month}월 {day}일')
print('----------------------------------------')
today2 = datetime.today()
current_time = datetime.now().time()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
mcr_second = current_time.microsecond
print(f'{hour}시 {minute}분 {second}초 {mcr_second}')
print('----------------------------------------')
print("어제 :",today + timedelta(days=-1))
print("내일 :",today + timedelta(days=1))
print("일주일 전 :",today + timedelta(days=-7))
print("일주일 후 :",today + timedelta(days=7))
print('----------------------------------------')
current_time = datetime.now()
print("한 시간 전:",current_time + timedelta(hours=-1))
print("내일 두 시간 전:",current_time + timedelta(days=1,hours=-2))
print('----------------------------------------')
# strftime() 함수 : 날짜 형식을 문자열로 반환
print('날짜를 문자열로 변환 :',today.strftime('%Y-%m-%d %H:%M:%S'))
print('날짜를 문자열로 변환 :',today.strftime('%Y-%m-%d %I:%M:%S %p'))
print('----------------------------------------')
# strptime() 함수 : 문자열을 날짜형식으로 반환
today = '2020-06-20 17:40:20'
trans_today = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
print("문자열을 날짜로 변환 : ",trans_today)
print('----------------------------------------')