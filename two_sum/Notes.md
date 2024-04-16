Original: https://leetcode.com/problems/two-sum/solutions/5032323/two-pass-python3-solution-beats-70-o-n-space-and-time-complexity/

# Intuition

Two-pass solution.

We store the elements and their indices in a dictionary(hashmap).
And then we use the hashmap to find the existence of (target-current number) in the array. If we don't find any, we move on to the next number.

# Approach

### First Pass

We create a hashmap of elements and their indices, where the elements are the keys.
An O(n) operation, in both time and space.

In case of repeated elements, the index stored will the last occurrence of the element. This won't cause any problems, as the solution will be found - in the second pass - when are at the first occurrence of the element in the array, wherein the hashmap will contain the second/last occurrence of the array.

### Second Pass
We go through the array, element by element.

For each element(current), we calculate diff=(target-current). Then we check if `diff` is present in the array, using the hashmap/dictionary's `get()` method.

There are two scenarios where we move on to the next iteration.

- If it is not present, then we get `None` as the result of the `get()` method, so we move on the next iteration.
- If the diff is found, but it is the same element(current index), then we continue, as the problem description does not allow this.

Now, if we do find the the index of `diff` in the the array, and it is not the current index, then we return both values in a list, solving the problem

### Edge Case
An input like `[3,3]`, with a target of 6.

After first pass, the dictionary will contain `[3: 1]` as its contents, aka the last occurrence of the element.

In the second pass, when we encounter the 3 at index 0, the dictionary's get will returnn 1 as the index of the `diff`. As this solution does not conflict with the problem description, we can submit the solution as `[0,1]`.

# Complexity

- Time complexity: **O(n)**

    Creation of the hashmap of elements and their indices is O(n). Going through the array to find a solution is also O(n), since searching for the existence of a number in the array is a O(1) operation. Therefore overall complexity is O(n).

- Space complexity: **O(n)**
    
    The size of the hashmap grows linearly with the size of the input array.

# Code

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num]=i
        for i, num in enumerate(nums):
            diff = target-num
            diff_index = nums_dict.get(diff)
            if diff_index is None or diff_index==i:
                continue
            else:
                return [i, diff_index]
```