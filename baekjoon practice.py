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
'''
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

