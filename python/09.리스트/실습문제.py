# #문제32
# nums = [5, 15, 2, -8, -12, -29, 43, 1]

# #가장 작은 수를 저장하고 있는 변수 선언 (초기값은 확실히 크게 만들었음)
# min = 9999

# for num in nums:
#     if num < min :
#         min = num
# print(min)

# #최댓값 찾기
# max = -9999

# for num in nums:
#     if num < max :
#         max = num
# print(max)


# #문제33
# nums = [5, 15, 2, -8, -12, -29, 43, 1]

# i = 1 #번호를 나타내기 위한 변수 (for문을 돌면서 1씩 증가)
# sum = 0

# for num in nums:
#     if i %2 ==1: #홀수번째 원소들을 찾기 위한 조건문
#         sum += num
#     i += 1
# print(sum)


#문제34
import random

x = [] #로또 번호를 저장할 리스트
count = 0 #뽑은 로또 번호 개수

while True :
    n = random.randint(1,45) #1에서 45번까지의 번호 랜덤
    if n not in x: #만일 n이 x에 저장된 값과 같다면
        x.append(n) #n이 나오면 x리스트에 저장함
        count += 1
        if count == 6:
            break
print(x)        
for lotto in x :
    print(lotto, end=' ') #리스트 없이 번호만 출력됨
