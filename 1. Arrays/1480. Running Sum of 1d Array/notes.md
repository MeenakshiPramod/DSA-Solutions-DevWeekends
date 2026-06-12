# Intuition
The running sum at any index is the sum of all elements from the beginning of the array up to that index. Instead of calculating the sum repeatedly for each position, we can use the previously computed running sum and add the current element to it. This is the Prefix Sum concept.

# Approach
1. Traverse the array starting from index `1`.
2. For each index `i`, add the value at index `i-1` (which already stores the running sum up to the previous position) to the current element.
3. Update the current element with this new sum.
4. After the traversal, the original array itself contains the running sums, so return it.

# Complexity
- Time complexity:
$$O(n)$$

We traverse the array once, where `n` is the length of the array.

- Space complexity:
$$O(1)$$

No extra space is used apart from the input array, as the running sums are computed in-place.

# Code
```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Using Prefix Sum concept
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums