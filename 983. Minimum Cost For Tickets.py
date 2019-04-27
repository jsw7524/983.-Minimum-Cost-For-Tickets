class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp=[99999999]*366
        dp[0]=0
        lastDay=days[-1]
        for d in range(1,lastDay+1):
            if d in days:
                
                if d-1>=0:
                    if dp[d-1] + costs[0] < dp[d]:
                        dp[d]=dp[d-1] + costs[0]

                if d-7>=0:
                    if dp[d-7] + costs[1] < dp[d]:
                        dp[d]=dp[d-7] + costs[1]
                else:
                    if costs[1] < dp[d]:
                        dp[d] = costs[1]

                if d-30>=0:
                    if dp[d-30] + costs[2] < dp[d]:
                        dp[d]=dp[d-30] + costs[2]
                else:
                    if costs[2] < dp[d]:
                        dp[d] = costs[2]
            else:
                dp[d] =dp[d-1]
        return dp[lastDay]

sln=Solution()
assert 11==sln.mincostTickets([1,4,6,7,8,20],[2,7,15])
assert 17==sln.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15])
assert 6==sln.mincostTickets([1,4,6,7,8,20],[7,2,15])