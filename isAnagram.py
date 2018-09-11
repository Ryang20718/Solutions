        counts = {}
        counts2 = {}
        if len(s) != len(t):
            return False
        for x in s: #string1
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1 
        for x in t: #string1
            if x in counts2:
                counts2[x] += 1
            else:
                counts2[x] = 1 
        for key, value in counts.items():
            if key in counts2 and value == counts2[key]:
                continue
            else:
                return False
        return True
    ## creates two hashmaps and then checks if both have same amt of keys and value count