class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich_wealth = 0
        for rows in accounts:
            sums=0
            for i in rows:
                sums+=i
            rich_wealth = max(rich_wealth,sums)
        return rich_wealth                

        