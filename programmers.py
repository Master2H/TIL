# lv.1
'''나머지가 1이 되는 수 찾기
(내 코드)
def solution(n):
    i = 1
    while True:
        if n % i == 1:
            answer = i
            break
        else:
            i += 1
    return answer

(Best Code)
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]
'''
