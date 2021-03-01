# 주사위의 짝 리스트 만들기 반복문 이용

# 주사위
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
    #리스트

c = [[1,1],[1,2],[5,6],[6,6]] # 끝까지 가면 36개

#for문 
def cube():

    cube_set= []

    for i in range(1,7):

        for j in range(1,7):


            cube_set.append((i,j))


    print(cube_set)

cube()


# 두 주사위의 합이 x의 배수는 몇개인가

# 4의 배수라고 하자 


def cube_multi(x):

    sum = []

    for i in range(1,7):

        for j in range(1,7):

            a = i + j

            if a % 4 == 0:

                sum.append(a)


    print(len(sum))


cube_multi(4)







    

