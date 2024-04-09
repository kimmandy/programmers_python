# #문제9
# #연산 우선순위
# #1. 괄호
# #2. 지수
# #3. 곱셈, 나눗셈, 몫, 나머지
# #4. 덧셈, 뺄셈
# #5. 같은 우선순위에서는 왼쪽에서 오른쪽으로 연산
# result = 100+20 / (4-2)*5
# print("예측한 결과: 150")
# print(result)


# #문제10
# pay = int(input())
# work_time = int(input())
# day_work = int(input())
# bonus = int(input())

# total_wage = day_work * work_time * pay + bonus
# print(total_wage)


#문제11
English = int(input())
Language = int(input())
Math = int(input())
Science = int(input())

total_score = (English + Language + Math + Science) / 4

print(total_score)