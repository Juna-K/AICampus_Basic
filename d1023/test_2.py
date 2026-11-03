def solve(n, m, problem_ans, student_ans):
    score_li = []

    # 학생수 N 만큼 정답비교
    for i in range(n):
        score = 0
        s = 0

        for j in range(m):  # 한 학생의 점수
            if problem_ans[j] == student_ans[i][j]:

                if problem_ans[j-1] == student_ans[i][j-1]:
                    s += 1
                else:
                    s = 1

                score += s
            
            if j==(m-1):
                score_li.append(score)


    solution = max(score_li) - min(score_li)

    return solution



# -------------------------------------------

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # 학생의 수 N, 문제의 수 M
    problem_ans = list(map(int, input().split()))   # M개의 문제에 대한 정답
                                                    # N줄에 걸쳐, N명의 학생이 제출한 M개의 문제에 대한 답안지의 정보
    
    student_ans = [list(map(int, input().split())) for _ in range(n)]

    solution = solve(n, m, problem_ans, student_ans)
    print(f"#{tc} {solution}")