"""
Method 1: Using min heap to store top K frequent elements
Time complexity: O(nlogk)
Space complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1

        heap = []
        heapq.heapify(heap)
        for key, value in hashtable.items():
            # push k elements into heap
            if len(heap) < k:
                heappush(heap, (value, key))
            else:
                # replace top element if it is smaller than nums[i]
                if heap[0][0] < value:
                    heappop(heap)
                    heappush(heap, (value, key))


        ans = []
        for i in range(k):
            ans.append(heap[i][1])
        return ans

"""
Method 2: Quick sort
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # store frequency of each element in nums
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1

        # quicksort and return top k frequent key-value pairs
        arr = list(hashtable.items())
        left, right = 0, len(arr)-1
        topk_pairs = self.quicksort(arr, left, right, k)

        ans = []
        for i in range(k):
            ans.append(topk_pairs[i][0])
        return ans

    def quicksort(self, nums, left, right, k):
        # # take nums[left] as pivot
        # pivot = nums[left][1]

        # or set pivot randomly, which is faster
        pivot_ind = random.randint(left, right)
        pivot = nums[pivot_ind][1]
        nums[left], nums[pivot_ind] = nums[pivot_ind], nums[left]

        j = left + 1
        for i in range(left+1, right+1):
            if nums[i][1] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        # j is the index of the pivot, nums[:j] store smaller value, nums[j+1:] stores larger value
        j -= 1
        nums[left], nums[j] = nums[j], nums[left]

        if j == len(nums)-k:
            return nums[len(nums)-k:]
        elif j < len(nums)-k:
            return self.quicksort(nums, j + 1, right, k)
        else:
            return self.quicksort(nums, left, j - 1, k)
