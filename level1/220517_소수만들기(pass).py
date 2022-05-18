
#######################################################################################
## fileName: 220517_소수만들기(pass)
## level01 
#######################################################################################
## TO DO
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
#######################################################################################


## 소수: 약수(나눠지는수)가 자기자신과 1뿐인 수 
## ex) 17이 소수인지 확인하려면 2~16으로 나눠지는지 확인 # https://seethefuture.tistory.com/87
## 즉 나머지가 0인지 여부를 판별하면 된다.
## 즉 17 % 2~16 != 0 이면 소수

from itertools import combinations

def solution(nums):  
    answer = 0
    sum_list = []
    not_prime_num = []
    
    ## 3개 숫자 조합 뽑기 -> sum()
    combine = list(combinations(nums, 3)) # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    for comb in combine:
        sum_list.append(sum(comb)) # [6, 7, 8, 9]
    
    ## 소수 판별 -> 카운트 +=1
    for num in sum_list:
        for i in range(2,num):
            if num%i == 0 : # 소수 아님 
                not_prime_num.append(num)
                break
    # print('not_prime_num', not_prime_num)

    answer = len(sum_list)-len(not_prime_num)
    return answer 


if __name__ == '__main__':
    # nums = [1,2,3,4] # 1
    nums = [1,2,7,6,4] # 4
    print(solution(nums))


#############################
## 다른 풀이 
#############################

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

#############################
## for ... else문 
#############################

## 예시 1 # https://www.delftstack.com/ko/howto/python/for-else-statement-python/
# 목록에서 요소를 검색 할 때 목록에 있는지 여부를 알고 싶을 때 사용할 수 있습니다.

a = 15
lst = [10,5,6,8,9,7,5,11]
for i in lst:
    if(i == 15):
        print("Found") # 출력 안 됨
        break
else:
     print("Not Found Loop Over")   # 출력됨


## 예시 2 # https://itholic.github.io/python-for-else/
## Before 
import random

lucky_num = random.randint(1,100)

for i in range(7):
    num = random.randint(1,100)
    if num == lucky_num:
        print("Congraturations!")
        break
    if i == 6:
        print("fail")

## After
lucky_num = random.randint(1,100)

for i in range(7):
    num = random.randint(1,100)
    if num == lucky_num:
        print("Congraturations!")
        break
# for문에서 break가 발생하지 않았을 경우. (맨 마지막에!!!!!!)
else:
    print("fail")
