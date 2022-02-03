# 딕셔너리를 이용하여 사용자로부터 영어단어와 뜻을 입력받아 사전을 구성하고,
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램을 작성하시오.

eng_dict = {}

while True:
    input_eng = input('영어 단어 등록 (종료는 quit) : ')

    if input_eng == 'quit':
        print()
        while True:
            search_msg = input('검색할 단어 입력 (종료는 quit) :')

            if(search_msg == 'quit'):
                break
            else:
                if search_msg in eng_dict.keys():
                    val = eng_dict[search_msg]
                    print(search_msg,'의 뜻은',val,'입니다.\n')
                else:
                    print(search_msg,'는 사전에 없는 단어 입니다. \n')
        break

    else:
        if input_eng in eng_dict.keys():
            print(input_eng +'는 이미 등록된 단어 입니다.\n')

        else :
            input_dict = input(input_eng + '의 뜻입력 (종료는 quit) :')
            eng_dict[input_eng] = input_dict
            print()


























