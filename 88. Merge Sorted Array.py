class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        counter = m+n-1

        while m > -1 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                print('counter:', counter, 'result:', nums1, nums1[m-1], nums2[n-1])
                nums1[counter] = nums1[m-1]
                m -= 1
                counter -= 1
            else: 
                print('counter:', counter, 'result:', nums1, nums1[m-1], nums2[n-1])
                nums1[counter] = nums2[n-1]
                n -= 1 
                counter -= 1

        if (len(nums1) > 0 and len(nums2) > 0):
            if (nums1[0] > nums2[0]):
                nums1[0] = nums2[0]
