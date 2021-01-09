class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort first
        intervals.sort()

        ans = []
        most_left = intervals[0][0]
        most_right = intervals[0][1]

        for left, right in intervals:
            if left > most_right:
                # won't overlap, therefore create new interval
                ans.append([most_left, most_right])
                most_left = left
                most_right = right


            else:
                # overlap, modify the existing interval
                if right > most_right:
                    most_right = right
        ans.append([most_left, most_right])
        return ans
