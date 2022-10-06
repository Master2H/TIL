# lv.1
'''나머지가 1이 되는 수 찾기
(My Code)
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

'''음양 더하기
(My Code)
def solution(absolutes, signs):
    answer = []
    for x, y in zip(absolutes, signs):
        if y == False:
            answer.append(-x)
        else:
            answer.append(x)
    return sum(answer)

(Best Code)
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
'''

'''없는 숫자 더하기
(My Code)
def solution(numbers):
    answer = [n for n in range(10) if n not in numbers]
    return sum(answer)

(Best Code)
def solution(numbers):
    return 45 - sum(numbers)
'''

'''내적
(My Code)
def solution(a, b):
    answer = [A*B for A, B in zip(a, b)]
    return sum(answer)

(Best Code)
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])
'''

'''약수의 개수와 덧셈
(My Code)
def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        yaksu = []
        for n in range(1, x+1):
            if x%n == 0:
                yaksu.append(n)
        if len(yaksu) % 2 == 0:
            answer += x
        else:
            answer -= x
    return answer

(Best Code) 제곱수는 약수의 갯수가 홀수인 것을 활용
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
'''

'''부족한 금액 계산하기
(My Code)
def solution(price, money, count):
    total_fee = [x*price for x in range(1, count+1)]
    if money - sum(total_fee) >= 0:
        answer = 0
    else:
        answer = -money + sum(total_fee)
    return answer

(Best Code) 산술평균 이용한 수학적 사고
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
'''

'''3진법 뒤집기
(My Code) int()의 10진법 변환 기능은 구글링 활용
def solution(n):
    ternary = ''
    while n != 0:
        q = n // 3
        r = n % 3
        ternary += str(int(r))
        n = int(q)
    return int(ternary,3)

(Best Code)
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

'''

'''예산
(My Code)
def solution(d, budget):
    d.sort()
    answer = len(d)
    while True:
        if sum(d[:answer]) <= budget:
            break
        else:
            answer -= 1

    return answer

(Best Code)
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
'''

'''[1차] 비밀지도
(My Code)
def solution(n, arr1, arr2):
    map1 = [list(format(x,'b')) for x in arr1]
    map2 = [list(format(x,'b')) for x in arr2]
    answer = []
    for line in map1:
        while True:
            if len(line) != n:
                line.insert(0, '0')
            else:
                break
    
    for line in map2:
        while True:
            if len(line) != n:
                line.insert(0, '0')
            else:
                break
    
    for line1, line2 in zip(map1, map2):
        answer_line = ''
        for x, y in zip(line1, line2):
            if (x == '1') or (y == '1'):
                answer_line += '#'
            else:
                answer_line += ' '
        answer.append(answer_line)
    return answer

(Best Code) rjust()(자릿수와 채울 문자 적용)와 비트연산자 활용
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''

'''두 개 뽑아서 더하기
(My Code)
def solution(numbers):
    answer = []
    i = 0
    j = i + 1
    while i != len(numbers) - 1:
        answer.append(numbers[i] + numbers[j])
        if j == len(numbers) - 1:
            i += 1
            j = i + 1
        else:
            j += 1

    return sorted(list(set(answer)))

(Best Code)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''

