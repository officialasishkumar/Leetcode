class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        # Initialise number of pieces Alice and Bob can take as 0.
        alice, bob = 0, 0

        # For every piece that is not an edge piece, check if it can be taken by Alice or Bob.
        for i in range(1, len(colors)-1):
            # If (i-1)th,ith and (i+1)th pieces are A, Alice can take it.
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                alice += 1
             # If (i-1)th,ith and (i+1)th pieces are B, Bob can take it.
            elif colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
                bob += 1
        
        ''' Since Alice starts the game, Alice only wins the game if Alice can get more
        pieces than Bob. If Bob gets equal or more pieces, Bob wins.
        '''
        if alice > bob:
            return True
        else:
            return False