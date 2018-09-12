def arithmetic_boggle(magic_number, numbers):
    # Fill in the code
    return helper(magic_number,0,numbers,0)

def helper(target,current,cur_list,i):
    if(i >= len(cur_list) and current != target):
        return False
    if(i >= len(cur_list) and current == target):
        return True

    return (helper(target,current + cur_list[i],cur_list,i+1) or helper(target,current - cur_list[i],cur_list,i+1))
    
def main():                      ##Checks if possible combinations in array can add/subtract to the target number
    print (arithmetic_boggle(0,[1]))

main()      