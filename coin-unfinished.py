        if amount == 0:
            return 0
        cur = 0
        dic = {}
        for c in coins:
            dic[c] = 1
        for num in range(1,amount+1):# only starts from 1 and only goes to amount
            for item in coins:
                diff = num - item
                if(diff in dic):
                    if(num not in dic):
                        dic[num] = dic[diff] + 1
                    else:
                        dic[num] = min(dic[num],dic[diff] + 1)
        if amount not in dic:
            return -1
        return dic[amount]