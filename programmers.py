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

'''소수 만들기
(My Code)
from itertools import combinations

def solution(nums):
    answer = []
    prime_numbers = [sum(nC3) for nC3 in list(combinations(nums, 3))]
    for prime_number in prime_numbers:
        check_pn = 0
        for n in range(1, prime_number+1):
            if prime_number % n == 0:
                check_pn += 1
        if check_pn == 2:
            answer.append(prime_number)
    return len(answer)

(Best Code)
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
'''

'''실패율
(My Code1-Runtime Error)
import operator

def solution(N, stages):
    fail = dict()
    for n in range(1, N+1):
        nomi = 0
        deno = 0
        for stage in stages:
            if n <= stage:
                deno += 1
            if n == stage:
                nomi += 1
        fail[n] = nomi / deno
    sort_fail = sorted(fail.items(), key=operator.itemgetter(1), reverse = True)
    answer = [x for x, y in sort_fail]
    return answer

(My Code2-Google 참고)
import operator

def solution(N, stages):
    fail = dict()
    deno = len(stages)
    for stage in range(1, N+1):
        if deno != 0:
            count = stages.count(stage)
            fail[stage] = count / deno
            deno -= count
        else:
            fail[stage] = 0
    sort_fail = sorted(fail.items(), key=operator.itemgetter(1), reverse = True)
    answer = [x for x, y in sort_fail]
    return answer

(Best Code)
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
'''

'''[1차] 다트 게임
(My Code)
def solution(dartResult):
    if "S" in dartResult:
        dartResult = dartResult.replace("S","^1,")
    if "D" in dartResult:
        dartResult = dartResult.replace("D","^2,")
    if "T" in dartResult:
        dartResult = dartResult.replace("T","^3,")
    if ",#" in dartResult:
        dartResult = dartResult.replace(",#","x(-1),")
    dartResult = dartResult.split(",")

    for score in dartResult:
        if "*" in score:
            if dartResult.index(score) == 1:
                dartResult[0] += "x2"
            elif dartResult.index(score) == 2:
                dartResult[0] += "x2"
                dartResult[1] += "x2"
            elif dartResult.index(score) == 3:
                dartResult[1] += "x2"
                dartResult[2] += "x2"
            elif dartResult.index(score) == 4:
                dartResult[2] += "x2"
                dartResult[3] += "x2"
    answer = []
    for x in dartResult:
        if (x == "") or (x =="*"):
            pass
        elif "*" in x:
            answer.append(x.replace("*",""))
        else:
            answer.append(x)

    answer_1 = []
    for a in answer:
        if "^" in a:
            answer_1.append(a.replace("^","**"))

    answer_2 = []
    for a in answer_1:
        if "x" in a:
            answer_2.append(a.replace("x","*"))
        else:
            answer_2.append(a)

    final = []
    for i in answer_2:
        final.append(eval(i))
    return sum(final)

(Best Code)
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
'''

