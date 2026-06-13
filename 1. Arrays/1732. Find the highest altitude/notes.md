# Intuition
The altitude starts at `0`. Each value in the `gain` array represents the net change in altitude between two points. To find the highest altitude reached during the trip, we can continuously update the current altitude by adding each gain value and keep track of the maximum altitude encountered so far.

# Approach
1. Initialize `curAlt` to `0` since the trip starts at altitude 0.
2. Initialize `highest` to `0` because the starting altitude is also a possible highest altitude.
3. Traverse the `gain` array:
   - Add the current gain value to `curAlt`.
   - Update `highest` with the maximum of `highest` and `curAlt`.
4. After processing all gain values, return `highest`.

This approach effectively computes the prefix sum of the gain array while tracking the maximum prefix sum.

# Complexity
- Time complexity:
$$O(n)$$

We iterate through the `gain` array exactly once.

- Space complexity:
$$O(1)$$

Only a constant amount of extra space is used regardless of the input size.

# Code
```python
class Solution():
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curAlt = 0
        highest = 0

        for i in gain:
            curAlt += i
            highest = max(curAlt, highest)

        return highest