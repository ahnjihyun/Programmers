
#######################################################################################
## TO DO
# 어떤 정수들이 있습니다. 
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
#######################################################################################

def solution(absolutes, signs):
    answer = 0
    
    for i, absol in enumerate(absolutes):
        if signs[i] == True:
            answer += absol
        else:
            answer -= absol

    return answer 



if __name__ == '__main__':
    absolutes = [4,7,12] # [1,2,3]
    signs = [True,False,True] # [false,false,true]
    # 9 # 0
    print(solution(absolutes, signs))


###############################
## 다른 풀이 1
###############################

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))


###############################
## 다른 풀이 2
###############################

def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
