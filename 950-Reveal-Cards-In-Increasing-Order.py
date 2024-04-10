class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        '''
        1. sort dec
        2. pop right side card from deque then put it to the front ot them
        3. pop top card from deque, put into front of deque
        '''
        deck.sort(reverse=True)
        queue = collections.deque()
        for card in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)
        return queue

        