class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 ==0:
                arr.append("FizzBuzz")
                continue
            if i%3 == 0:
                arr.append("Fizz")
                continue
            if i%5 == 0:
                arr.append("Buzz")
                continue
            arr.append(str(i))
        return arr
    ##key is continue as it will just jump to next iteration