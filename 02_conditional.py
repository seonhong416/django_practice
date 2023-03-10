'''
조건문

if 조건 :
    코드
elif 조건 :
    코드
...
else :
    코드

비교 연산자
값 == 값 양쪽 값이 서로 같다
값 != 값 양쪽 값이 서로 다르다
값 > 값, 값 < 값, 값 >= 값, 값 <= 값 크기 비교

조건 연산자
1. 조건1 and 조건2 (조건1, 조건2 동시 만족)
2. 조건1 or 조건2 (두 조건중 하나만 만족하면 ok)
'''

a = 3
b = 5

print(a == 3 and b == 5)

'''
사과는 냉장실에
아이스크림은 냉동실에
나머지는 폐기처분 해 주세요
'''

물건 = '사과'

if 물건 == '사과' :
    print(f'{물건}이/가 냉장실에 들어갔습니다.')
    
elif 물건 == '아이스크림' :
    print(f'{물건}이/가 냉동실에 들어갔습니다.')

else :
    print(f'{물건}이/가 폐기처분 됐습니다.')
    
