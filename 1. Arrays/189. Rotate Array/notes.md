# Intuition

To rotate the array to the right by `k` positions efficiently, we can use the reversal technique. Instead of shifting elements one by one (which would take `O(n*k)` time), we reverse parts of the array to place the elements in their correct rotated positions.

The idea is:
1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n-k` elements.

This restores the relative order of elements while achieving the desired rotation.

# Approach

1. Compute `k % n` to handle cases where `k` is greater than the length of the array.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the elements from index `k` to `n-1`.
5. The array is now rotated to the right by `k` positions.

For example:

```text
nums = [1,2,3,4,5,6,7], k = 3

Reverse whole array:
[7,6,5,4,3,2,1]

Reverse first k elements:
[5,6,7,4,3,2,1]

Reverse remaining elements:
[5,6,7,1,2,3,4]
```

# Complexity

- Time complexity:

$$O(n)$$

The array is traversed a constant number of times through the reversal operations.

- Space complexity:

$$O(1)$$

The rotation is performed in-place without using any extra array.

# Code

```python
class Solution(object):
    def reverseArray(self, nums, l, r):
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k = k % n

        self.reverseArray(nums, 0, n - 1)
        self.reverseArray(nums, 0, k - 1)
        self.reverseArray(nums, k, n - 1)
```