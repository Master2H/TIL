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
Countlist = [Word.count(Alphabet) for Alphabet in Alphabets]
Max = max(Countlist)
max_number = 0
for count in Countlist:
    if Max == count:
        max_number += 1
if max_number == 1:
    print(Alphabets[Countlist.index(max(Countlist))].upper())
else:
    print("?")
'''

# 1152
'''
Input = input().strip()
WordList = Input.split()
print(len(WordList))
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
WordList = [input() for _ in range(TestCase)]
for word in WordList:
    character_list = []
    for character in word:
        if character not in character_list:
            character_list.append(character)
        elif character_list[-1] == character:
            character_list.append(character)
    if word == ''.join(character_list):
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
num_list = [int(i) for i in input().split()]
number = int(input())
print(num_list.count(number))
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
numberList = [int(a) for a in input().split()]
answer = 0
for i in numberList:
    for j in range(2,int(math.sqrt(i))):
        print(j)
        if i % j != 0:
            pass
        else:
            break
'''

# 11382
'''
answerList = [int(x) for x in input().split()]
print(sum(answerList))
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


