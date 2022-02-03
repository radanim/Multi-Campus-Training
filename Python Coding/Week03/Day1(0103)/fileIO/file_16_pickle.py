# pickle 파일
# 메모리에 로딩된 객체나 정의된 클래스를 파일로 저장하여 사용

import pickle

# pickle.dump() : 객체(리스트형태) 저장
f = open("list.pickle",'wb')
result = [1,2,3,4,5]
pickle.dump(result,f)
f.close()

#pickle.load() : 객체 로딩
f = open("list.pickle",'rb')
result2 = pickle.load(f)
print(result2)
result2.append(100)
print(result2)
f.close()


















