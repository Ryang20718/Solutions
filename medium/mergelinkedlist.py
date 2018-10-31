pseudo-code:
def helper(a,b):
    if(a == None):
        return b
    if(b == None):
        return a
    temp = a
    if(a.data <= b.data):
        a.next = helper(a.next,b)
    else:
        b.next = helper(a,b.next)