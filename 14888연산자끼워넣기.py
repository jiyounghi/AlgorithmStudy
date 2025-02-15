import sys
from itertools import permutations

input = sys.stdin.read
def solve():
    # 입력 처리
    data = input().split("\n")
    N = int(data[0])
    numbers = list(map(int, data[1].split()))
    operator_counts = list(map(int, data[2].split()))
    
    # 연산자 리스트 생성
    operators = ('+', '-', '*', '/')
    operator_list = []
    for i, count in enumerate(operator_counts):
        operator_list.extend([operators[i]] * count)  # 연산자를 개수만큼 리스트에 추가

    # 최댓값, 최솟값 초기화
    max_value = -int(1e9)
    min_value = int(1e9)
    
    # 연산자의 모든 순열 경우의 수 탐색
    for perm in set(permutations(operator_list)):  # 중복을 제거하기 위해 set 사용
        result = numbers[0]  # 첫 번째 숫자를 초기값으로 설정
        for i in range(1, N):  # 1번 인덱스부터 차례대로 연산 적용
            if perm[i - 1] == '+':
                result += numbers[i]
            elif perm[i - 1] == '-':
                result -= numbers[i]
            elif perm[i - 1] == '*':
                result *= numbers[i]
            elif perm[i - 1] == '/':
                if result < 0:
                    result = -(-result // numbers[i])  # 음수 나눗셈 처리
                else:
                    result //= numbers[i]
        
        # 최댓값, 최솟값 갱신
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    
    # 결과 출력
    print(max_value)
    print(min_value)

if __name__ == "__main__":
    solve()
