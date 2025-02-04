a = []

# 아홉개 입력받고 리스트에 저장 
for i in range(9):
    a.append(int(input()))

# 지금 난쟁이들 키의 합 - 원래 난쟁이들 키의 합 100해서 변수에 저장
total = sum(a) - 100 

# x+y=total을 이용해서 숨어들어온 난쟁이 추려내기
for i in range(9):
    for j in range(i+1, 9):
        if a[i] + a[j] == total:
            fake1, fake2 = a[i], a[j]
            found = True
    else:
        continue
    break

a.remove(fake1)
a.remove(fake2)

# 진짜 난쟁이들 출력 
a.sort()
for i in a:
    print(i)



