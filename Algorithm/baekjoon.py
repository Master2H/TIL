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

# 10816
'''
import sys
import collections

input = sys.stdin.readline
N = int(input())
Ncard = list(map(int, input().split()))
cardSet = collections.Counter(Ncard)
M = int(input())
nums = list(map(int, input().split()))
for i in nums:
    if i in cardSet:
        print(cardSet[i], end = ' ')
    else:
        print(0, end =' ')
'''

# 1764
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
notHear = {input().strip() for _ in range(N)}
answer = []
for _ in range(M):
    name = input().strip()
    if name in notHear:
        answer.append(name)
answer.sort()

print(len(answer))
for i in answer:
    print(i)
'''

# 1269
'''
import sys
import collections

input = sys.stdin.readline

A, B = map(int, input().split())
ASet = list(map(int, input().split()))
BSet = list(map(int, input().split()))
answer = collections.Counter(ASet+BSet)
print(list(answer.values()).count(1))
'''

# 11478
'''
S = input()
answer = set()
for i in range(len(S)):
    for j in range(1,len(S)+1):
        if i >= j:
            pass
        else:
            answer.add(S[i:j])
print(len(answer))
'''

# 1934
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    AA, BB = A, B

    while BB != 0:
        AA, BB = BB, AA%BB
    
    print(int(A*B/AA))
'''

# 13241
'''
A, B = map(int, input().split())
AA, BB = A, B

while BB != 0:
    AA, BB = BB, AA%BB
    
print(int(A*B/AA))
'''

# 1735
'''
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

def getGCD(a, b):
    aa, bb = a, b
    
    while bb != 0:
        aa, bb = bb, aa%bb
    return aa
gcd1 = getGCD(B1, B2)
B3 = int(B1*B2/gcd1)
A3 = int(A1*(B3/B1) + A2*(B3/B2))

gcd2 = getGCD(A3, B3)
A3, B3 = int(A3/gcd2), int(B3/gcd2)
print(A3, B3)
'''

# 2485 (google reference)
'''
import sys
import math
input = sys.stdin.readline

N = int(input())
numList = [int(input()) for _ in range(N)]
numList.sort()
intervalList = [numList[i+1] - numList[i] for i in range(len(numList)-1)]
intervalset = list(set(intervalList))
gcd = intervalset[0]
for i in range(1, len(intervalset)):
    gcd = math.gcd(gcd, intervalset[i])

answer = 0
for i in intervalList:
    answer += (i // gcd) - 1
print(answer)
'''

# 4134
'''
import sys
import math
input = sys.stdin.readline

def isPrimeNumber(n):
    for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                     return False
    return True

testCase = int(input())

for _ in range(testCase):
    n = int(input())

    if n <= 2:
        print(2)
    elif n == 3:
        print(3)
    elif n == 4:
        print(5)
    else:
        while True:
            if isPrimeNumber(n) == True:
                 print(n)
                 break
            n += 1
'''

# 1929
'''
import math

def isPrimeNumber(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

M, N = map(int, input().split())

for i in range(M, N+1):
     if isPrimeNumber(i) == True:
         print(i)
'''

# 4948
'''
import math

def isPrimeNumber(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    answer = 0

    if n == 0:
        break

    for i in range(n+1, 2*n + 1):
        if isPrimeNumber(i) == True:
            answer += 1
    print(answer)
'''

# 17103
'''
import sys

primeNum = [False, False] + [True]*999999

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i):
            primeNum[j] = False

testCase = int(input())

for i in range(testCase):
    N = int(input())
    answer = 0

    for j in range(2, N//2+1):
        if primeNum[j] and primeNum[N-j]:
                    answer += 1
    print(answer)
'''

# 13909
'''
import math

N = int(input())

print(int(math.sqrt(N)))
'''

# 15439
'''
N = int(input())
print(N**2-N)
'''

# 24723
'''
N = int(input())
print(2**N)
'''

# 10872
'''
(재귀함수)
N = int(input())

def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(N))
(math 라이브러리 활용)
import math
N = int(input())
print(math.factorial(N))
'''

# 11050
'''
import math

N, K = map(int, input().split())
print(math.factorial(N)//(math.factorial(N-K)*math.factorial(K)))
'''

# 1010
'''
import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(math.factorial(M)//(math.factorial(M-N)*math.factorial(N)))
'''

# 1037
'''
number = int(input())
realDivList = list(map(int, input().split()))
realDivList.sort()
print(realDivList[0]*realDivList[-1])
'''

# 25192
'''
(My Code)
import sys
input = sys.stdin.readline

N = int(input())
answer = 0
logList = [input().rstrip() for _ in range(N)]
answerList = []
for i in range(len(logList)):
    if logList[i] == 'ENTER':
        answerList.append(i)
if len(answerList) == 1:
    print(len(set(logList))-1)
elif len(answerList) == 2:
    answer += len(set(logList[answerList[0]+1:answerList[1]])) + len(set(logList[answerList[1]+1:]))
    print(answer)
else:
    for i in range(len(answerList)-1):
        if i == len(answerList) - 2:
            answer += len(set(logList[answerList[i+1]+1:])) + len(set(logList[answerList[i]+1:answerList[i+1]]))
        else:
            answer += len(set(logList[answerList[i]+1:answerList[i+1]]))

    print(answer)

(Best Code)
N = int(input())
dic = {}
count = 0

for i in range(N):
    Input = input()

    if Input == 'ENTER':
        for key, value in dic.items():
            if value == 1:
                count += 1
        dic = {}
    else:
        if Input not in dic:
            dic[Input] = 1
for key, value in dic.items():
    if value == 1:
        count += 1
print(count)
'''

# 26069
'''
(MY Code)
import sys
input = sys.stdin.readline

N = int(input())
danceList = set()

for i in range(N):
    A, B = map(str, input().split())
    if (A == 'ChongChong') or (B == 'ChongChong'):
        danceList.add(A)
        danceList.add(B)
    elif A in danceList:
        danceList.add(B)
    elif B in danceList:
        danceList.add(A)
print(len(danceList))

(Best Code)
import sys
input = sys.stdin.readline

n = int(input())
dance = {'ChongChong'}

for i in range(1, n+1):
    a, b = input().rstrip().split()

    if a in dance:
        dance.add(b)

    if b in dance:
        dance.add(a)

print(len(dance))
'''

# 20920 (google Reference)
'''
(Version 1)
import sys

input =sys.stdin.readline
vocaDic = dict()
N, M = map(int, input().split())
for _ in range(N):
    voca = input().rstrip()
    if len(voca) < M:
        continue
    if vocaDic.get(voca):
        vocaDic[voca][0] += 1
    else:
        vocaDic[voca] = [1, len(voca), voca]

answer = sorted(vocaDic.items(), key = lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in answer:
    print(i[0])

(Version 2)
import sys

input =sys.stdin.readline
vocaDic = dict()
N, M = map(int, input().split())
for _ in range(N):
    voca = input().rstrip()
    if len(voca) < M:
        continue
    if voca in vocaDic:
        vocaDic[voca] += 1
    else:
        vocaDic[voca] = 0
answer = sorted(vocaDic.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in answer:
    print(i[0])
'''

# 10828
'''
import sys
input = sys.stdin.readline
stack = []
N = int(input())
for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        stack.append(cmd[1])
    if cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack.pop(-1)))
    if cmd[0] == 'size':
        print(len(stack))
    if cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
'''

# 28278
'''
import sys
input = sys.stdin.readline
stack = []
N = int(input())
for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        stack.append(cmd[1])
    if cmd[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack.pop(-1)))
    if cmd[0] == '3':
        print(len(stack))
    if cmd[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
'''

# 10773
'''
import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):

    n = int(input())

    if n == 0:
        stack.pop(-1)
    else:
        stack.append(n)
print(sum(stack))
'''

# 9012
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = []
    Input = input().rstrip()
    for ps in Input:
        if ps == '(':
            stack.append(ps)
        else:
            if len(stack) == 0:
                stack.append(ps)
                break
            else:
                stack.pop(-1)
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')
                    
'''

# 4949
'''
while True:
    stack = []
    Input = input()

    if Input == '.':
        break
    for i in Input:
        if (i == '(') or (i == '['):
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[':
                stack.append(i)
                break
            else:
                stack.pop(-1)
        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                stack.append(i)
                break
            else:
                stack.pop(-1)
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
'''

# 12789
'''
(My Code)
N = int(input())
stack = [1001]
count = 1
numList = list(map(int, input().split()))

for num in numList:
    if num == count:
        count += 1
        continue
    if stack[-1] == count:
        while stack[-1] == count:
            count += 1
            stack.pop()
    if stack[-1] <= num:
        print('Sad')
        break
    else:
        stack.append(num)
if count == stack[-1]:
    print('Nice')

(Best Code)
from collections import deque

N = int(input())
numList = deque(map(int, input().split()))
count = 1
stack = deque()

while numList:
    if numList[0] == count:
        count += 1
        numList.popleft()
    else:
        stack.append(numList.popleft())
    while stack and stack[-1] == count:
        stack.pop()
        count += 1
print('Nice' if not stack else 'Sad')
'''

# 18258
'''
from collections import deque
import sys
input = sys.stdin.readline

que = deque()
N = int(input())
for _ in range(N):
    cmd = input().split()
    
    if len(cmd) >= 2:
        que.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
'''

# 2164
'''
from collections import deque

N = int(input())
cardList = deque([x for x in range(1, N+1)])
while len(cardList) != 1:
    cardList.popleft()
    cardList.rotate(-1)
print(cardList[0])
'''

# 11866 (Google Reference)
'''
(Method 1)
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
numList = deque([x for x in range(1, N+1)])
answer = []
while numList:
    for i in range(K-1):
        numList.append(numList.popleft())
    answer.append(str(numList.popleft()))

print('<' + ', '.join(answer)+'>')

(Method 2)
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numList = [x for x in range(1, N+1)]
idx = 0
answer = []
while numList:
    idx += K - 1
    if idx >= len(numList):
        idx %= len(numList)
    answer.append(str(numList.pop(idx)))
print('<', ', '.join(answer), '>', sep ='')
'''

# 28279
'''
from collections import deque
import sys
input = sys.stdin.readline
deq = deque()
N = int(input())

for _ in range(N):
    cmd = input().split()
    
    if cmd[0] == '1':
        deq.appendleft(int(cmd[1]))
    if cmd[0] == '2':
        deq.append(int(cmd[1]))
    if cmd[0] == '3':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    if cmd[0] == '4':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    if cmd[0] == '5':
        print(len(deq))
    if cmd[0] == '6':
        if deq:
            print(0)
        else:
            print(1)
    if cmd[0] == '7':
        if deq:
            print(deq[0])
        else:
            print(-1)
    if cmd[0] == '8':
        if deq:
            print(deq[-1])
        else:
            print(-1)
'''

# 2346 (Error Fixed by Google Reference)
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
num = input().split()
bl = deque()
answer = []
idx = 0
for i in range(N):
    bl.append((i, int(num[i])))
while bl:
    idx, val = bl.popleft()
    answer.append(str(idx + 1))
    if val > 0:
        bl.rotate(-(val - 1))
    elif val < 0:
        bl.rotate(-val)
    
print(' '.join(answer))
'''

# 24511
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(input().split())
answer = []
for i in range(N):
    if A[i] == 0:
        answer.append(str(B[i]))
answer.reverse()
if len(answer) >= M:
    answer = answer[:M]
else:
    answer = answer + C[:M - len(answer)]
print(' '.join(answer))
'''

# 27433
'''
N = int(input())
def factorial(x):
    if (x == 0) or (x == 1):
        return 1
    return x*factorial(x-1)
print(factorial(N))
'''

# 10870
'''
N = int(input())
def Fibonacci(x):
    if x <= 1:
        return 0
    elif x == 2:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)
print(Fibonacci(N+1))
'''

# 25501
'''
testCase = int(input())
for _ in range(testCase):
    S = input()
    global count
    count = 0
    def recursion(s, l, r):
        global count
        count += 1
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return recursion(s, l+1, r-1)
    
    def isPalindrome(s):
        return recursion(s, 0, len(s)-1)
    
    print(isPalindrome(S), count)
'''

# 24060 (병합정렬 정의 및 코드 Google Reference)
'''
import sys
input = sys.stdin.readline

def m_sort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L) + 1) // 2

    a_1 = m_sort(L[:mid])
    a_2 = m_sort(L[mid:])

    i = j = 0
    tmp = []

    while i < len(a_1) and j < len(a_2):
        if a_1[i] < a_2[j]:
            tmp.append(a_1[i])
            answer.append(a_1[i])
            i += 1
        else:
            tmp.append(a_2[j])
            answer.append(a_2[j])
            j += 1
    
    while i < len(a_1):
        tmp.append(a_1[i])
        answer.append(a_1[i])
        i += 1
    
    while j < len(a_2):
        tmp.append(a_2[j])
        answer.append(a_2[j])
        j += 1
    
    return tmp

answer = []
A, K = map(int, input().split())
A_list = list(map(int, input().split()))
m_sort(A_list)

print(answer[K-1] if len(answer) > K else -1)
'''

# 4779
'''
def cantor(s):
    if s == '-':
        return '-'
    
    part1 = s[:len(s)//3]
    part2 = s[len(s)//3:len(s)//3*2]
    part3 = s[len(s)//3*2:]

    if part1 == '-':
        return '- -'
    
    part2 = part2.replace('-',' ')


    return cantor(part1) + part2 + cantor(part3)

while True:
    try:
        N = int(input())
        string = '-'*3**N
        answer = cantor(string)
        print(answer)
    except EOFError:
        break
'''

# 2447 (Google Reference)
'''
def make_star(N):
    if N == 1:
        return ['*']
    stars = make_star(N//3)
    L = []

    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star + ' '*(N//3) + star)
    for star in stars:
        L.append(star*3)

        
    return L
N = int(input())
print('\n'.join(make_star(N)))
'''

# 11729 (Google Reference)
'''
N = int(input())

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi_tower(n-1, start, 6-start-end)
    
    print(start, end)

    hanoi_tower(n-1, 6-start-end, end)

print(2**N-1) # 하노이탑 최소 이동 횟수
hanoi_tower(N,1,3)
'''

# 15649
'''
from itertools import combinations, permutations

N, M = map(int, input().split())
num_list = [x for x in range(1, N+1)]
answer  = list(permutations(num_list, M))

for i in answer:
    for j in i:
        print(j, end = ' ')
    print()
'''

# 15650
'''
(My Code)
from itertools import combinations
N, M = map(int, input().split())

NList = [x for x in range(1, N+1)]

answer = list(combinations(NList, M))

for i in answer:
    i = list(map(str, list(i)))
    print(' '.join(i))

(Best Code)
N, M = map(int, input().split())
s = []
def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)
'''

# 15651
'''
N, M = map(int, input().split())

s = []
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()

dfs()
'''

# 15652
'''
N, M = map(int, input().split())
s = []
def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)
'''

# 9663 (Google Reference)
'''
(My Code)
N = int(input())

answer = 0
s = [0] * N

def promising(x):
    for i in range(x):
        if s[x] == s[i] or abs(s[x]-s[i]) == abs(x - i):
            return False
    
    return True


def find_queen(x):
    global answer
    if x == N:
        answer += 1
        return
    
    else:
        for i in range(N):
            s[x] = i
            if promising(x):
                find_queen(x+1)

find_queen(0)
print(answer)

(Best Code)
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
'''

# 2580 (Google Reference)
import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]

def row(a, n):
    for i in range(9):
        if n == sudoku[a][i]:
            return False
    return True

def column(a, n):
    for i in range(9):
        if n == sudoku[i][a]:
            return False
    return True

def square(y, x, n):
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3*3+i][x//3*3+j]:
                return False
    return True




# 14888 (Google Reference)
'''
import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(x) for x in input().split()]
cal_list = [int(x) for x in input().split()]

max_ = -10e9
min_ = 10e9

def find_max_min(depth, total, plus, minus, multiply, divine):

    global max_
    global min_

    if depth == N:
            max_ = max(max_, total)
            min_ = min(min_, total)
            return
    
    else:
        if plus:
            find_max_min(depth + 1, total + num_list[depth], plus - 1, minus, multiply, divine)
        if minus:
            find_max_min(depth + 1, total - num_list[depth], plus, minus - 1, multiply, divine)
        if multiply:
            find_max_min(depth + 1, total * num_list[depth], plus, minus, multiply - 1, divine)
        if divine:
            find_max_min(depth + 1, int(total / num_list[depth]), plus, minus, multiply, divine - 1)

find_max_min(1, num_list[0], cal_list[0], cal_list[1], cal_list[2], cal_list[3])
print(max_)
print(min_)
'''

# 14889 (Google Reference)
'''
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
ins = sys.maxsize
visited = [False] * N

def DFS(depth, idx):

    global ins


    if depth == (N // 2):
        
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += matrix[i][j]
                if not visited[i] and not visited[j]:
                    link += matrix[i][j]
        
        ins = min(ins, abs(start-link))
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(depth+1, i+1)
            visited[i] = False

DFS(0,0)
print(ins)
'''

