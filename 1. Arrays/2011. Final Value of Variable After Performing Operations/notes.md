# Intuition
Each operation either increases or decreases the value of `X` by 1. Instead of checking all four possible strings (`"++X"`, `"X++"`, `"--X"`, `"X--"`), we can observe that the middle character determines the operation. If it is `'+'`, we increment `X`; otherwise, we decrement it.

# Approach
1. Initialize a variable `x` to `0`.
2. Traverse through each operation in the `operations` array.
3. Check the character at index `1`:
   - If it is `'+'`, increment `x` by `1`.
   - Otherwise, decrement `x` by `1`.
4. Return the final value of `x`.

This works because all valid operations have either `'+'` or `'-'` as their middle character.

# Complexity
- Time complexity:
$$O(n)$$

We iterate through the array once, where `n` is the number of operations.

- Space complexity:
$$O(1)$$

Only a single variable is used to store the current value of `x`.

# Code
```python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for op in operations:
            if op[1] == '+':
                x += 1
            else:
                x -= 1

        return x