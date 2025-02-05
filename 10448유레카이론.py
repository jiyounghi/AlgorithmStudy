# 삼각수 리스트 생성 
tri = []
n = 1
while True:
    t = n*(n+1) // 2 
    if t > 1000:
        break
    tri.append(t)
    n += 1 

# 세 개의 삼각수 합으로 표현 가능한지 
def eureka(num):
    for i in range(len(tri)):
        for j in range(len(tri)):
            for k in range(len(tri)):
                if tri[i] + tri[j] + tri[k] == num:
                    return 1 
    return 0 
     
# 입력 받고 출력 
T = int(input())   
for _ in range(T):
    K = int(input())
    print(eureka(K))