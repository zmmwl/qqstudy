from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前填充nums1
        p1 = m - 1  # 指向nums1的最后一个有效元素
        p2 = n - 1  # 指向nums2的最后一个元素
        p = m + n - 1  # 指向nums1的最后一个位置

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果nums2还有剩余，直接复制到nums1前面
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(numbers[i])

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)

print(nums1)
