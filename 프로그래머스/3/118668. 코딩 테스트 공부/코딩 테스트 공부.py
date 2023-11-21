def solution(alp, cop, problems):
    answer = 0
    INF = float("inf")
    
    dp = [[INF] * 450 for _ in range(450)]
    dp[alp][cop] = 0
    
    max_alp = max([p[0] for p in problems])
    max_cop = max([p[1] for p in problems])
    
    max_alp = max(alp, max_alp)
    max_cop = max(cop, max_cop)
    
    cur_apl = alp
    cur_cop = cop
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j]) 
            dp[i][j+1] = min(dp[i][j] + 1, dp[i][j+1]) 
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    next_alp, next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                    
        
    answer = dp[max_alp][max_cop]
    return answer
    