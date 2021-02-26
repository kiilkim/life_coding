""" #Expression.

print(1+1)
#

a = 'world' in 'hello world'

print(a)


import os.path

print(os.path.exists('boolean2.py'))


#조건을 판단할 때 boolean 쓴다.
a = input('id?')
b = input('password?')


if a == 'kevin' and b == '1111':
    print("로그인")
else:
    print("로그인실패") """



#list 
s = [1, 'four', 9, 16, 25]

#어떻게 읽어오는가가 중요

print(s[0])

#[]안은 index 값인데 0부터 읽는다. 

del s[2]

print(s)

s.append(33)

print(s)

s.insert(0, 22)

print(s)

#컨테이너

print(len('egoing')+len(['a','b']))

#컨_딕셔너리

dic = {}

person = {'name':'kim', 'age':'31'}

print(person.get('name'))



#반복문 _ for문

for value in ['a','b','c']:
    print(value)
    #하나 하나 꺼내서 
    #10번 반복해라, ~x번반복해라 range



for value in range(0,11):
    print(value)
    #range 에선 range(x)라하면 x-1까지 표시
    #범위는 range(0,x) 0부터 x-1 까지~




 

