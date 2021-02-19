"""
Method 1:
Time complexity: O(n log n)
Space complexity: O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

"""
Method 2: quick find/partition
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        left, right = 0, n-1

        while True:
            # ind = self.partition(nums, left, right) # much slower (1872ms)
            ind = self.partition2(nums, left, right) # much faster (556ms)

            if ind == target:
                return nums[target]
            elif ind < target:
                left = ind + 1
            else:
                right = ind - 1

    # left side: < pivot, right side: > pivot
    def partition(self, nums, left, right):
        pivot = nums[left]
        pivot_ind = left
        left += 1

        while left <= right:
            if nums[left] > pivot and nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

            if nums[left] <= pivot: left += 1
            if nums[right] >= pivot: right -= 1

        nums[right], nums[pivot_ind] = nums[pivot_ind], nums[right]
        return right

    # left side: < pivot, right side: > pivot
    def partition2(self, nums, left, right):
        pivot = nums[left]
        pivot_ind = left
        left += 1

        # i is the right pointer
        for i in range(left, right+1):
            if nums[i] < pivot:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        nums[pivot_ind], nums[left-1] = nums[left-1], nums[pivot_ind]
        return left-1

"""
Method 3: priority queue (fastest, 32ms)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        heap = []
        heapq.heapify(heap)
        for i in nums:
            # push k elements into heap
            if len(heap) < k:
                heappush(heap, i)
            else:
                # replace top element if it is smaller than nums[i]
                if heap[0] < i:
                    heappop(heap)
                    heappush(heap, i)

        return heappop(heap) # min of the heap = kth largest element
