n, s, m = map(int, input().split())
v_can = list(map(int, input().split()))

# 각 단계별로 가능한 볼륨을 저장하는 리스트
volume = [[] for _ in range(n+1)]
volume[0].append(s)  # 시작 볼륨 저장

for i in range(n):
    lst = set()  # 중복 제거를 위해 set 사용
    for x in volume[i]:  # 이전 단계에서 가능한 볼륨 값들
        plu = x + v_can[i]
        minu = x - v_can[i]
        
        # 유효한 범위 내의 값만 추가
        if 0 <= plu <= m:
            lst.add(plu)
        if 0 <= minu <= m:
            lst.add(minu)

    volume[i+1] = list(lst)  # set을 리스트로 변환

# 마지막 곡에서 가능한 볼륨이 있는지 확인
if volume[n]:
    print(max(volume[n]))
else:
    print(-1)