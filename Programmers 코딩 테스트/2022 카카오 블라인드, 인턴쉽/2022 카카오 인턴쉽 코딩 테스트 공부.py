def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for a,b,c,d,e in problems:
        max_alp = max(max_alp,a)
        max_cop = max(max_cop,b)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp = [[1e9 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp: # i+1인 이유 i = max_alp가 됐을 때 윗 부분 하지않고 아랫 i >= alp_req 부분을 하기 위해서 
                dp[i + 1][j] = min (dp[i + 1][j],dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min (dp[i][j + 1],dp[i][j] + 1)

            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[-1][-1]

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))

# 알고력과 코딩력을 따로 공부해서 시간이 1씩 늘어나는 거랑 요구된 값 대로 시간이
# 늘어나는 2개를 모든 경우의 수로 다 적용해서 그 중 가장 작은 값으로 채워나가면
# 마지막에 있는 값이 정답이다.