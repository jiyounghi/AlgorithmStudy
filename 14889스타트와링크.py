from itertools import combinations

n = int(input()) # 인원수 
s = [] # 능력치 표 
for _ in range(n):
    lst = list(map(int, input().split()))
    s.append(lst)

people = list(range(n)) # 사람 리스트 
min_diff = float('inf')  # 최소 능력치 차이

# 스타트팀과 링크팀 구하기 
for start_team in combinations(people, n//2):
    # 링크팀 = 전체 - 스타트팀
    link_team = list(set(people) - set(start_team))
    
    # 스타트팀 능력치 계산
    start_score = sum(s[i][j] + s[j][i] for i, j in combinations(start_team, 2))
    
    # 링크팀 능력치 계산
    link_score = sum(s[i][j] + s[j][i] for i, j in combinations(link_team, 2))
    
    # 두 팀의 능력치 차이의 최솟값 갱신
    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)

