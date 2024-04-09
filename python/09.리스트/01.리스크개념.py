#리스트 만들기
company_list = ['삼성전자', 'SK하이닉스', '네이버','카카오'] #데이터 리스트 안에 있는 데이터들은 원소라고 함

# #데이터 접근하기(인덱싱)
# print(company_list[0])
# print(company_list[1])
# print(company_list[2])

# #데이터 할당하기
# company_list[0] = '애플'
# company_list[1] = '구글'
# company_list[2] = '테슬라'
# print(company_list)


# #데이터 추가하기
# company_list.append('아마존')
# print(company_list)

# #데이터 삭제하기
# del company_list[0]
# print(company_list)

# #리스트 길이
# print(len(company_list))

#리스트 슬라이싱
print(company_list[0:2]) #0에서 2까지 슬라이싱 (0, 1)
print(company_list[:2]) #시작번호가 0이면 생략가능
print(company_list[1:3]) #1에서 3까지 슬라이싱(1,2)
print(company_list[1:]) #끝나는번호까지 슬라이싱(맨 끝 번호는 생략가능)
print(company_list[::2]) #2칸씩 띄어서 출력함
