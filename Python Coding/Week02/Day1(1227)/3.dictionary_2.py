# 문제) 요리에 대한 정보를 딕셔너리에 저장, 음식정보들은 리스트로 구성
data1 = {'name':'버섯불고기','class':'한식','type':'불고기','ingr':['소고기','양파','간장','설탕']}
data2 = {'name':'카레덮밥','class':'양식','type':'덮밥','ingr':['카레','감자','양파','당근']}

datum = [data1,data2]

for data in datum:
    # print('values:',data.values())
    print('keys:',data.keys())
    # print('items:', data.items())
    # print('-------------------------------------------------')
    for d in data.keys():
        print(d)
        # print(datum[d])