# 사각형 그리기 : 최대한 면적이 큰 사각형을 몇 개 그릴 수 있는가?
    # 단, 사각형의 왼쪽 상단 좌표의 값과 우측 하단의 좌표의 값은 동일해야 한다.
    # 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수

def solve(N, board):
    start_point = [0]*2
    end_point = [0]*2

    max_area = 0

    for s1 in range(N):
        for s2 in range(N):
            for e1 in range(s1, N):
                for e2 in range(s2, N):

                    if board[s1][s2] == board[e1][e2] :
                        area = (board[e1]-board[s1]+1) * (board[e2]-board[s2]+1)

                    if max_area < area :
                        max_area = area

    solution = 0
    
    return solution, max_area


# ---------------------------------
T = int(input())

for tc in range(1, T+1) :
    N = int(input())    # 게임판의 크기 N
    board = [list(map(int, input().split())) for _ in range(N)]

    solution, max_area = solve(N, board)
    
    print(max_area)
    
    print(f"#{tc} {solution}")