class Solution:
    def mincostTickets(self, days, costs):
        
        tickets = [1,7,30] #티켓 종류(n일권) 리스트
        dp = [0] * (days[-1] + 1) #마지막 날짜에 하나 늘려서 dp 배열 만듦
        
        for i in range(1, len(dp)):
            if i not in days: # days에 여행 날짜가 없을 때
                dp[i] = dp[ i - 1] # 마지막으로 지불한 티켓 비용을 사용

            else: # days에 여행 날짜가 있을 때
                dp[i] = min([dp[max(0, i - n)]+ c for n, c in zip(tickets, costs)])
                
                # 이 list comprehension의 의미는
                # 1. 1일권에 해당하는 cost c에 이전 cost를 더하는 경우
                # 2. 7일권에 해당하는 cost c에 7일 외에 남은 날짜의 cost를 더하는 경우
                # 3. 30일권에 해당하는 cost c에 30일 외에 남은 날짜의 cost를 더하는 경우
                # 이 세개의 경우 중 최소 비용을 택하겠다.
                
                # dp[i] = min(dp[max(0, i-1)] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)]+ costs[2])
                # 위처럼 풀어서 써도 동일함
                # cost length==3으로 제한되어있는데 만약 제한이 없을 경우에는 list comprehension이 유리할 것으로 보임
                
        return dp[-1]
