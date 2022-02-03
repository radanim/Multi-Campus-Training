f = open('/Users/chaewon/python/yesterday.txt','r')
str = f.read().split()
f.close()

wd_arr = [w.lower() for w in str]
wd_set = set(wd_arr)
wd_dict = {}

for wd in wd_set:
    wd_dict[wd] = wd_arr.count(wd)

wd_dict = dict(sorted(wd_dict.items()))
for key in wd_dict.keys() :
    print(f'\'{key}\' : {wd_dict[key]}')
