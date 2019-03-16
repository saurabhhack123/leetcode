#https://leetcode.com/problems/median-of-two-sorted-arrays
#T: O(M+N) S:O(M+N)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = []
        i = 0
        j = 0
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                merge.append(nums1[i])
                i+=1
            else:
                merge.append(nums2[j])
                j+=1
        
        if i==len(nums1):
            for index in range(j,len(nums2)):
                merge.append(nums2[index])
        else:
            for index in range(i,len(nums1)):
                merge.append(nums1[index])
        
        if len(merge)%2==0:
            return (float(merge[len(merge)/2]+merge[(len(merge)-1)/2])/2)
        else:
            return float(merge[len(merge)/2])
        
        
