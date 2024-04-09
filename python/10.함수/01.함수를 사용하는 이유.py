#1. 반복되는 코드가 줄어든다.
#2. 재사용성이 좋아진다.
#3. 수정이 쉬워진다.

print("안녕하세요 동준님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요 현식님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")

print("안녕하세요 원준님")
print("현재 프리미엄 서비스 사용기간이 8일 남았습니다.")

#함수의 사용
def print_message(name, age):
    print(f'안녕하세요 {name}님')
    print(f'현재 프리미엄 서비스 사용기간이 {age}일 남았습니다.')