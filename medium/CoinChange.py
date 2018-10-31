Pseudocode for min number of coins needed
    matrix = [[0 for x in range(len(a)+1)] for y in range(len(h)+1)] with extra space
    for i in range(1, amt+1):
        matrix[0][j] = i
    for i in range(1,len(coins)+1):
        matrix[i][0] = coins[i-1]
        
    count = 0
    for i in range(1,len(coins)+1):
        for j in range(1,amt+1):
            if(j >= coins[i]):
                matrix[i][j]= min(matrix[i-1][j], 1+ matrix[i][j-coin[i]])
            else:
                matrix[i][j] = matrix[i-1][j]
                
def minNumberOfCoins(amount, denominations):#recursion

    if amount <= 0:
        return(0)

    if amount in denominations:
        return(1)

    for d in sorted(denominations, reverse=True):
        if d <= amount:
            return 1 + minNumberOfCoins(amount - d, denominations)
