a = []
rmv = []

# 아홉개 입력받고 리스트에 저장 
for i in range(9):
    b = input()
    a.append(b)

# 지금 난쟁이들 키의 합 - 원래 난쟁이들 키의 합 100해서 변수에 저장
a = list(map(int, a))
total = sum(a) - 100 

# x+y=total을 이용해서 숨어들어온 난쟁이 추려내기
for x in a:
    for y in a:
        if x+y==total and x != y:
            rmv.append(x)
            rmv.append(y)

# 거짓 난쟁이들 후보 중복제거             
rmv_set = set(rmv)
rmv = list(rmv_set)

# 거짓 난쟁이 제거 
for i in rmv: 
    a.remove(i)
a.sort()

# 진짜 난쟁이들 출력 
for i in a:
    print(i)



