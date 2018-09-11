        answer = -1
        if(len(s) <= 0):
            answer = -1
        order = []
        counts = {}
        for x in s:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1 
                order.append(x)
        for x in order:
            print (x)
        for x in order:
            if counts[x] == 1:
                answer = s.index(x)
                break
        return answer
    ## creates a set that maps characters to # of times appear
    ## creates an array of the unique letters in order and finds the one that first appears that appears only once
    ## returns the index of the character in the string