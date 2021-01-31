# # Method 1: Double pointer (save a copy of nums1, compare from frt to end)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """

#         copy = nums1.copy()
#         p1 = p2 = i = 0
#         while p1 < m and p2 < n:
#             if nums2[p2] < copy[p1]:
#                 nums1[i] = nums2[p2]
#                 i += 1
#                 p2 += 1
#             else:
#                 nums1[i] = copy[p1]
#                 i += 1
#                 p1 += 1

#         if p1 < m: nums1[p1+p2:] =  copy[p1:m]
#         if p2 < n: nums1[p1+p2:] =  nums2[p2:]

# Method 2: Double pointer (Doesn't save a copy of nums1, compare from end to frt)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, i = m-1, n-1, m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        # add remaining elements from nums2 to nums1
        nums1[:p2+1] = nums2[:p2+1]
