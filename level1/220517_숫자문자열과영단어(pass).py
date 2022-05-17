
#######################################################################################
## fileName: 220517_숫자문자열과영단어(pass)
## level01 
#######################################################################################
## TO DO
# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
#######################################################################################

def solution(s):  
    answer = ''
    number = { 'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for key, val in number.items():
        if key in s:
            s = s.replace(key, val)
    answer = s 
    return int(answer) 





if __name__ == '__main__':
    s = "one4seveneight" # 1478
    # s = "23four5six7" # 234567
    # s = "2three45sixseven" # 234567
    # s = "123" # 123
    print(solution(s))


#############################
## 다른 풀이 1
#############################

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4",
             "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

## 따라 쓰기 
def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


#############################
## 다른 풀이  2
#############################

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)