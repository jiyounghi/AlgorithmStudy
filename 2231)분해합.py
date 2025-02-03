# n = 123이면
# 123+1+2+3=>129 
# 1. 자연수 N 입력받기 
# 2. 자연수 N의 한자리수씩 읽기
# 3. 읽어들인 수를 N에 더하기 
# 4. 생성자가 없는 경우 0 출력하기
n = input()
lst = []
total = int(n)

# n 읽어서 리스트에 넣기 
for i in n:
    lst.append(int(i))
print(lst)

# 리스트 값 읽어서 n에 더하기 
for j in lst:
    total += j
print(total)
