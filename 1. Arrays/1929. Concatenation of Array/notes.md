# Intuition
The task is to create a new array that contains the original array twice in the same order. Instead of appending elements one by one, we can create an array of size `2 * n` and fill it using the modulo operator. Since `i % n` cycles through the indices of the original array repeatedly, it allows us to copy the elements twice efficiently.

# Approach
1. Let `n` be the length of the input array.
2. Create a result array `ans` of size `2 * n`.
3. Traverse the indices from `0` to `2 * n - 1`.
4. For each index `i`, assign:
   - `ans[i] = nums[i % n]`
5. The modulo operation ensures that after reaching the end of `nums`, we start again from the beginning.
6. Return the resulting array.

# Complexity
- Time complexity:
$$O(n)$$

We iterate through `2n` elements, which simplifies to `O(n)`.

- Space complexity:
$$O(n)$$

An additional array of size `2n` is created to store the concatenated result.

# Code
```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(2 * n):
            ans[i] = nums[i % n]

        return ans