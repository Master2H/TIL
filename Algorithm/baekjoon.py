# 4673
'''
def d(N):
    ssj = [int(digit) for digit in str(N)]
    return sum(ssj) + N

NotSelfnumber = [d(x) for x in range(1,10001) if d(x) <= 10000]

for number in range(1,10001):
    if number not in NotSelfnumber:
        print(number)
'''

# 1065
'''
N = int(input())

def Check_hansu(n):
    hansu = 0
    if n < 100:
        return print(n)
    elif n <= 1000:
        for number in range(100, n+1):
            number = str(number)
            if int(number[0]) - int(number[1]) == int(number[1]) - int(number[2]):
                hansu += 1
        return print(99 + hansu)

Check_hansu(N)
'''

# 11654
'''
Input = input()
print(ord(Input))
'''

# 10809
'''
S = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"
for alphabet in alphabets:
    print(S.find(alphabet), end=" ")
'''

# 1157
'''
Word = input().lower()
Alphabets = 'abcdefghijklmnopqrstuvwxyz'
Countx = [Word.count(Alphabet) for Alphabet in Alphabets]
Max = max(Countx)
max_number = 0
for count in Countx:
    if Max == count:
        max_number += 1
if max_number == 1:
    print(Alphabets[Countx.index(max(Countx))].upper())
else:
    print("?")
'''

# 1152
'''
Input = input().strip()
Wordx = Input.split()
print(len(Wordx))
'''

# 2908
'''
A, B = input().split()
A = A[::-1]
B = B[::-1]
if int(A) > int(B):
    print(int(A))
else:
    print(int(B))
'''

# 1316
'''
TestCase = int(input())
Answer = 0
Wordx = [input() for _ in range(TestCase)]
for word in Wordx:
    character_x = []
    for character in word:
        if character not in character_x:
            character_x.append(character)
        elif character_x[-1] == character:
            character_x.append(character)
    if word == ''.join(character_x):
        Answer += 1
print(Answer)
'''

# 1712(time limit)
'''
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    n = A // (C - B)
    print(n+1)
'''

# 2292
'''
N = int(input())
answer = 1
Stage = 1
while True:
    if N <= Stage:
        print(answer)
        break
    else:
        Stage += 6*(answer)
        answer += 1
'''


# 1193 time out - google reference
'''(Best Code/ Copy Code)
N = int(input())
max_num = 0
line = 0
while N > max_num:
    line += 1
    max_num += line

gap = max_num - N
if line % 2 == 1:
    numer = gap + 1
    denom = line - gap
else:
    numer = line - gap
    denom = gap + 1

print(f"{numer}/{denom}")
'''

# 2869 error - google reference
'''
A, B, V = map(int, input().split())

if (V - B) % (A - B) == 0:
    print((V - B) //  (A - B))
else:
    print((V - B) // (A - B) + 1)
'''

# 10250
'''
test_case = int(input())
for _ in range(test_case):
    H, W, N = map(int, input().split())
    if N%H == 0:
        floor = H
        back = N//H
    else:
        floor = N%H
        back = N//H +1
    if back < 10:
        print(int(f"{floor}0{back}"))
    else:
        print(int(f"{floor}{back}"))
'''

# 2775
'''
test_case = int(input())
for _ in range(test_case):
    k = int(input())
    n = int(input())
    f1 = [sum(range(i+2)) for i in range(n)]
    if k == 1:
        print(f1[-1])
    else:
        for j in range(k-1):
            f1 = [sum(f1[:j+1]) for j in range(n)]
        print(f1[-1])
'''

# 10807
'''
N = int(input())
num_x = [int(i) for i in input().split()]
number = int(input())
print(num_x.count(number))
'''

# 5597
'''
good_student = [int(input()) for _ in range(28)]
for i in range(30):
    if i+1 not in good_student:
        print(i+1)
'''

# 2839
'''
N = int(input())
Q = N // 5
if Q == 0:
    if N == 3:
        print(1)
        Q=-2
    else:
        print(-1)
        Q=-2
while Q >= 0:
    if N - 5*Q == 0:
        print(Q)
        break
    elif (N -5*Q) % 3 == 0:
        print(Q+((N -5*Q)//3))
        break
    else:
        Q -= 1

if Q == -1:
    print(-1)
'''

# 10757
'''
Answer = [int(a) for a in input().split()]
print(sum(Answer))
'''

# 1978 (미완)
'''
import math
testCase = int(input())
numberx = [int(a) for a in input().split()]
answer = 0
for i in numberx:
    for j in range(2,int(math.sqrt(i))):
        print(j)
        if i % j != 0:
            pass
        else:
            break
'''

# 11382
'''
answerx = [int(x) for x in input().split()]
print(sum(answerx))
'''

# 10810
'''
N, M = map(int, input().split())
answer = [0 for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    answer[a-1:b] = [c for _ in range(b-(a-1))]
for i in answer:
    print(i, end=" ")
(Best Code)
N, M = map(int, input().split())
answer = [0 for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    answer[a-1:b] = [c for _ in range(b-(a-1))]
print(*answer)
'''

# 10813
'''
N, M = map(int, input().split())
answer = [x+1 for x in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    x, y = answer[a-1], answer[b-1]
    answer[a-1] = y
    answer[b-1] = x
print(*answer)
'''


# 10811
'''
N, M = map(int, input().split())
answer = [x+1 for x in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    answer[a-1:b] = answer[a-1:b][::-1]
print(*answer)
'''

# 2743
'''
answer = input()
print(len(answer))
'''

# 9086
'''
testCase = int(input())
for _ in range(testCase):
    x = input()
    print(x[0]+x[-1])
'''

# 11718 (error - google reference)
'''
while True:
    try:
        a = input()
        print(a)
    except:
        break
# try-except 구문으로 예외처리하는 법 잊지 말자!
'''

# 2444
'''
x = int(input())
for i in range(1,2*x):
    if i <= x:
        print(" "*int(((2*x-1-(2*i-1))/2))+"*"*(2*i-1))
    else:
        print(" "*int((2*x-1-(2*(2*x-i)-1))/2)+"*"*(2*(2*x-i)-1))
'''

# 10812
'''
N, M = map(int, input().split())
answer = [x+1 for x in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    answer[a-1:b] =  answer[c-1:b] + answer[a-1:c-1]
print(*answer)
'''

# 25206
'''
subjectDict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
scoreGrade = [input().split()[1:] for _ in range(20)]
total = 0
scoreSum = 0
for x in scoreGrade:
    try:
        total += float(x[0]) * subjectDict[x[1]]
        scoreSum += float(x[0])
    except:
        continue
print(round(total/scoreSum,6))
'''

# 25314
'''
N = int(input())
print("long "*int(N/4)+"int")
'''

# 27866
'''
S = input()
i = int(input())
print(S[i-1])
'''

# 2738
'''
N, M = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for i, j in zip(A,B):
    for k in range(M):
        print(i[k]+j[k], end=" ")
    print(end="\n")
'''

# 2566
'''
matrix = [list(map(int, input().split())) for _ in range(9)]
maxNumber = 0
rowNumber = 0
for number, row in enumerate(matrix, start=1):
    if maxNumber <= max(row):
        maxNumber = max(row)
        rowNumber = number
    else:
        pass
print(maxNumber)
print(rowNumber, matrix[rowNumber-1].index(maxNumber)+1)
'''

# 10798
'''
wordList = [input() for _ in range(5)]
maxLength = 0
for word in wordList:
    if len(word) >= maxLength:
        maxLength = len(word)

for n in range(maxLength):
        for word in wordList:
            try:
                    print(word[n], end = '')
            except:
                    pass
'''

# 2563
'''
testCase = int(input())
paper = [[0]*100 for _ in range(100)]
for _ in range(testCase):
    a, b = map(int, input().split())
    for x in range(a, 10+a):
        for y in range(10):
            paper[100-b-y][x] = 1
answer = 0
for i in range(100):
        answer += paper[i].count(1)
print(answer)
'''

# 5086
'''
while True:
    x, y = map(int, input().split())
    if x == 0:
        break
    elif x > y:
        if x % y == 0:
            print("multiple")
        else:
            print("neither")
    else:
        if y % x == 0:
            print("factor")
        else:
            print("neither")
'''

# 2501
'''
N, K = map(int, input().split())
factorList = [i for i in range(1, N+1) if N % i == 0]
if len(factorList) < K:
    print(0)
else:
    print(factorList[K-1])
'''

# 9506
'''
while True:
    x = int(input())
    if x < 0:
        break
    else:
        factorList = [i for i in range(1,x) if x % i == 0]
        if sum(factorList) == x:
            factorList = list(map(str,factorList))
            print(str(x) + " = ", end = "")
            print(" + ".join(factorList))
        else:
            print(f"{x} is NOT perfect.")
'''

# 1978
'''
testCase = int(input())
numberList = list(map(int, input().split()))
answerList = []
for i in numberList:
    temp = []
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 2:
        answerList.append(i)
print(len(answerList))
'''

# 2581
'''
M = int(input())
N = int(input())
answerList = []
for i in range(M,N+1):
    temp = []
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 2:
        answerList.append(i)
if len(answerList) == 0:
    print(-1)
else:
    print(sum(answerList))
    print(min(answerList))
'''

# 11653
'''
N = int(input())
i = 2
while i <= N:
    if N == 1:
        break
    while N % i == 0:
        print(i)
        N = N // i
    i += 1
'''

# 9020
'''
testCase = int(input())
for _ in range(testCase):
    N = int(input())
    A, B = N // 2, N // 2
    if N == 4:
        print(2, 2)
    else:
        if A % 2 == 0:
            A = A - 1
            B = B + 1
        while True:
            temp = []
            for i in range(1, A+1):
                if A % i == 0:
                    temp.append(i)
                    if len(temp) >= 3:
                        break
            if len(temp) == 2:
                temp2=[]
                for j in range(1, B+1):
                    if B % j == 0:
                        temp2.append(j)
                        if len(temp2) >= 3:
                            break
                if len(temp2) == 2:
                    if A + B == N:
                        print(A, B)
                        break
            A -= 2
            B += 2
'''

# 24262
'''
print("""1
0""")
'''

# 24263
'''
n = int(input())
print(f"""{n}
1""")
'''

# 24264
'''
n = int(input())
print(f"""{n**2}
2""")
'''

# 24265
'''
n = int(input())
print(f"""{int(0.5*n*(n-1))}
2""")
'''

# 24266
'''
n = int(input())
print(f"""{n**3}
3""")
'''

# 24267
'''
n = int(input())
answer = []
for i in range(1,n-1):
    answer.append(int(0.5 * (n-i) * (n-(i+1))))
print(f"""{sum(answer)}
3""")
'''

# 24313
'''
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

while n0 <= 100:
    if c*n0 >= a1*n0 + a0:
        n0 += 1
    else:
        print(0)
        break

if n0 >= 101:
    print(1)
'''

# 2587
'''
numberList = [int(input()) for _ in range(5)]
print(int(sum(numberList)/5), sorted(numberList)[2])
'''

# 25305
'''
N, k = map(int, input().split())
scoreList = list(map(int, input().split()))
print(sorted(scoreList)[-k])
'''

# 2751
'''
testCase = int(input())
numberList = [int(input()) for _ in range(testCase)]
for i in sorted(numberList):
    print(i)
'''

# 10989
'''
import sys

testCase = int(sys.stdin.readline())
numberList = [0] * 10000
for _ in range(testCase):
    n = int(sys.stdin.readline())
    numberList[n-1] += 1

for i in range(0,10000):
    if numberList[i] > 0:
        for _ in range(numberList[i]):
            print(i+1)
'''

# 2798
'''
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()
answerList = []
for i in combinations(numList, 3):
    answerList.append(sum(i))
answerList.sort()
answer=0
for j in answerList:
    if j <= M:
        answer = j
print(answer)
'''

# 2231
'''
(My Code)
import sys

N = int(sys.stdin.readline())
bhhList=[]
for i in range(1,1000001):
    bhh = [i]
    for j in range(len(str(i))):
        bhh.append(int(str(i)[j]))
    bhhList.append(sum(bhh))
if N in bhhList:
    print(bhhList.index(N)+1)
else:
    print(0)

(Best Code)
n = int(input())

for i in range(1, n+1):
    num = i
    num_sum = sum(map(int, str(i)))
    num = num + num_sum

    if num == n:
        print(i)
        break
    if n == i:
        print(0)
'''


# 19532
'''
a, b, c, d, e, f = map(int, input().split())
x = -1000
y = -1000
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i + b*j == c:
            if d*i + e*j == f:
                x = i
                y = j
                break
print(x, y)
'''

# 1018 (google reference)
'''
import sys
N, M = map(int, sys.stdin.readline().split())
chessLine = [list(map(str, sys.stdin.readline().strip("\n"))) for _ in range(N)]
cnt = []
for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if chessLine[x][y] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if chessLine[x][y] != 'B':
                        w += 1
                    else:
                        b += 1
        cnt.append(w)
        cnt.append(b)

print(min(cnt))
'''

# 1436
'''
N = int(input())
answer = 0
count = 0
i = 0
while True:
    if '666' in str(i):
        count += 1
        if N == count:
            answer = i
            break
    i += 1
print(answer)
'''

# 2108
'''
import sys
from collections import Counter
N = int(sys.stdin.readline())
numberList = [int(sys.stdin.readline()) for _ in range(N)]
numberList.sort()
cnt = Counter(numberList)
freq = cnt.most_common(2)
if len(freq) >= 2:
    if freq[0][1] == freq[1][1]:
        freq = freq[1][0]
    else:
        freq = freq[0][0]
else:
    freq = numberList[0]
print(f"""{round(sum(numberList)/N)}
{numberList[int((N/2))]}
{freq}
{max(numberList)-min(numberList)}""")
'''

# 1427
'''
import sys
N = sys.stdin.readline().strip("\n")
N = int(''.join(sorted(N, reverse=True)))
print(N)
'''

# 11650
'''
import sys
N = int(sys.stdin.readline())
coordinateList = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinateList.sort()
for i in range(len(coordinateList)):
    print(coordinateList[i][0], coordinateList[i][1])
'''

# 11651
'''
import sys
N = int(sys.stdin.readline())
coordinateList = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinateList.sort(key=lambda x:(x[1],x[0]))
for i in range(len(coordinateList)):
    print(coordinateList[i][0], coordinateList[i][1])
'''

# 1181
'''
import sys

N = int(sys.stdin.readline())
wordList = [sys.stdin.readline().strip() for _ in range(N)]
wordList = list(set(wordList))
wordList.sort(key=lambda x : (len(x),x))

for i in wordList:
    print(i)
'''

# 10814
'''
import sys

N = int(sys.stdin.readline())
memberList = [sys.stdin.readline().split() for _ in range(N)]
memberList.sort(key=lambda x:int(x[0]))
for i in memberList:
    print(' '.join(i))
'''

# 18870 (google reference - 시간초과 문제 해결을 위해 dictionary 활용)
'''
import sys
N = int(sys.stdin.readline())
NumList = list(map(int, sys.stdin.readline().split()))
NumOrder = sorted(list(set(NumList)))
dic = {NumOrder[i] : i for i in range(len(NumOrder))}
for i in NumList:
    print(dic[i], end = ' ')
'''

# 2745
'''
N, B = map(str, input().split())
dic = {"A" : 10,
       "B" : 11,
       "C" : 12,
       "D" : 13,
       "E" : 14,
       "F" : 15,
       "G" : 16,
       "H" : 17,
       "I" : 18,
       "J" : 19,
       "K" : 20,
       "L" : 21,
       "M" : 22,
       "N" : 23,
       "O" : 24,
       "P" : 25,
       "Q" : 26,
       "R" : 27,
       "S" : 28,
       "T" : 29,
       "U" : 30,
       "V" : 31,
       "W" : 32,
       "X" : 33,
       "Y" : 34,
       "Z" : 35,
       }
answer = 0
for i in range(len(N)):
    try:
        temp = int(N[i])*int(B)**(len(N)-(i+1))
        answer += temp
    except:
        temp = dic[N[i]]*int(B)**(len(N)-(i+1))
        answer += temp

print(answer)
'''

# 11005
'''
N, B = map(int, input().split())
dic = {10 : "A",
       11 : "B",
       12 : "C",
       13 : "D",
       14 : "E",
       15 : "F",
       16 : "G",
       17 : "H",
       18 : "I",
       19 : "J",
       20 : "K",
       21 : "L",
       22 : "M",
       23 : "N",
       24 : "O",
       25 : "P",
       26 : "Q",
       27 : "R",
       28 : "S",
       29 : "T",
       30 : "U",
       31 : "V",
       32 : "W",
       33 : "X",
       34 : "Y",
       35 : "Z",
       }
answer = ''
while True:
    if N == 0:
        break
    rem = N % B
    if rem < 10:
        answer = str(rem) + answer
        N = N // B
    else:
        answer = dic[rem] + answer
        N = N // B
print(answer)
'''

# 2720
'''
import sys

testCase = int(sys.stdin.readline())
coin = [25, 10, 5, 1]
for _ in range(testCase):
    answer = [0, 0, 0, 0]
    change = int(sys.stdin.readline())
    while True:
        if change == 0:
            break
        if change >= coin[0]:
            answer[0] += 1
            change = change - coin[0]
            continue
        elif change >= coin[1]:
            answer[1] += 1
            change = change - coin[1]
            continue
        elif change >= coin[2]:
            answer[2] += 1
            change = change - coin[2]
            continue
        elif change >= coin[3]:
            answer[3] += 1
            change = change - coin[3]
            continue
    for i in answer:
        print(i, end = " ")
    print()
'''

# 2903
'''
N = int(input())
number = 2
for _ in range(N):
    number = (number + number-1)
print(number**2)
'''

# 10815
'''
import sys
N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
numDict = {x : 1 for x in numList}
M = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    try:
        temp = numDict[i]
        print(1, end = " ")
    except:
        print(0, end = " ")
'''

# 14425
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = {input() for _ in range(N)}
answer = 0
for i in range(M):
    a = input()
    if a in S:
        answer += 1
print(answer)
'''

# 7785
'''
import sys
input = sys.stdin.readline
nameSet = set()
n = int(input())
for i in range(n):
    name, log = input().split()
    if log == 'enter':
        nameSet.add(name)
    if log == 'leave':
        nameSet.discard(name)
nameSet = sorted(list(nameSet), reverse=True)
for i in nameSet:
    print(i)
'''

