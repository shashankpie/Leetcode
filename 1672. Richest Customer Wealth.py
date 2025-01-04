class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for row in range(len(accounts)):
            wealth = 0
            for col in accounts[row]:
                wealth += col
                if wealth > max_wealth:
                    max_wealth = wealth
        return max_wealth
