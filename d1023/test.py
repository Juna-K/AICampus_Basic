# 문제1. Captcha Code 인증기
    # Sample과 PassCode가 주어졌을때, Sample에서 PassCode를 만들 수 있는지 없는지를 판단하는 프로그램
    # 랜덤으로 N개 길이의 Sample이 주어진다.
    # K개 길이의 PassCode가 주어진다.
    
    # 검증: Sample에서 PassCode를 "순차적으로" 만들 수 있는지
    # 생성할 수 있으므로, 1을 출력


# def solve(N, K, sample, passcode):
#     solution = 0    # "1 or 0"
#     pos_li = []

#     for i in range(K):  # PassCode 길이 K
#         pos = 0

#         for j in range(N):  # Sample 길이 N
#             if passcode[i] == sample[j]:    # 처음일때의 j를 저장
#                                             # 동일 숫자인 경우 !!
#                 if pos == 0 :
#                     pos = j

#         pos_li.append(pos)
    

#     for i in range(len(pos_li)):
#         if i>1:
#             if pos_li[i] > pos_li[i-1] :    # 지금께 이전보다 작으면 0
#                                             # 
#                 solution = 1
#             else:
#                 solution = 0
#                 break   
    
#     return solution

def solve(N, K, sample, passcode):
    solution = 0    # "1 or 0"
    pos_li = []

    for i in range(K):  # PassCode 길이 K
        pos = 0

        for j in range(N):  # Sample 길이 N
            if passcode[i] == sample[j]:    # 처음일때의 j를 저장
                                            # 동일 숫자인 경우 !!
                if i == 0 :
                    pos_li.append(j)
                    break
                elif j > pos_li[i-1] :
                    pos_li.append(j)
                    break

        # pos_li.append(pos)
    
    if len(pos_li) == N :
        solution = 1
    
    return solution



#-------------------------------------------------

T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())    # N개 길이의 Sample / K개 길이의 PassCode

    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    solution = solve(N, K, sample, passcode)
    print(f"#{tc} {solution}")

