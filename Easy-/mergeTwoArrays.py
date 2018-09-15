import copy
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        filter(lambda a: a != 0, nums1)
        arr = []
        index1 = 0
        index2 = 0
        while(index1 < m and index2 < n):
            if(nums1[index1] <= nums2[index2]):
                arr.append(nums1[index1])
                index1+=1
            else:
                arr.append(nums2[index2])
                index2+=1
        while(index1 < m):
            arr.append(nums1[index1])
            index1 += 1
        while(index2 < n):
            arr.append(nums2[index2])
            index2+= 1
        for index in range(0,len(nums1)):
            nums1[index]= arr[index]
#essentially compares each element in two arrays and puts into separate array and then copies separate array into num1