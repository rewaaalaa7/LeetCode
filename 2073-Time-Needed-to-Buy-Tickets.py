class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0 

        for i, x in enumerate(tickets):
            if i<= k:
                total += min(tickets[k], tickets[i])
            else:
                total += min(tickets[k]-1, tickets[i])
        return total
        