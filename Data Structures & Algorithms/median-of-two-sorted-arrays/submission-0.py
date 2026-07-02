class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        k = n + m  
        arr = [0] * k

        k2 = k - 1
        p, p1 = n - 1, m - 1

        while p >= 0 and p1 >= 0:
            if nums1[p] < nums2[p1]:
                arr[k2] = nums2[p1]
                p1 -= 1
            else:
                arr[k2] = nums1[p]
                p -= 1
            k2 -= 1

        while p >= 0:
            arr[k2] = nums1[p]
            p -= 1
            k2 -= 1

        while p1 >= 0:
            arr[k2] = nums2[p1]
            p1 -= 1
            k2 -= 1

        mid = len(arr) // 2
        if len(arr) % 2 != 0:
            return arr[mid]
        else:
            return (arr[mid - 1] + arr[mid]) / 2
