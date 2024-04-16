Original: https://leetcode.com/problems/valid-parentheses/solutions/5033286/stack-based-python3-solution-beats-94-o-n/

# Intuition
We use a stack as the centerpiece of this solution. If we see an opening brace, push to stack. If we see a Closing brace, we pop the top of stack to see if there is matching opening brace. Rinse and repeat and we should have an empty stack at the end, in the ideal case.

# Approach
We use a Python list as a Stack.

We traverse the input character by character.
For each character, we check what kind of brace it is. So there are two cases to handle.
1. Case 1 - Opening brace - `(,{,[` - In this case, we simply push to the stack and continue to the next iteration.
2. Case 2 - Closing brace - `),},[` - This is a bit more complex. If the stack is empty, then we immediately return `False`, as it is a parentheses mismatch. If the stack is not empty, we pop the top of the stack, and check if the top is the opening brace of the same type. If it is, the braces match, and we continue to the next iteration.

If we have traversed the entire input, and the stack is empty, then it meanns the input is valid, and we return `True`. If the stack is not empty, then there was a parentheses mismatch, and input is invalid, and we return `False`.

# Complexity
- Time complexity: $$O(n)$$
    We make one traversal of the entire input, which is O(n). During which we check the type of braces, which are constant time operations.

- Space complexity: $$O(n)$$
    Size of stack grows with the size of input. To be more precise, size of stack grows with depth of nesting of the parentheses. Worst case is O(n).


# Code
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brace in s:
            match brace:
                # Opening brace, push to the stack
                case '(' | '{' | '[':
                    stack.append(brace)
                    continue
                # Closing brace
                case ')' | '}' | ']':
                    # Pop stack and check to see if top of stack is matching opening brace
                    # If not matching, return false immediately
                    # Edge case: Handle encounter of closing brace before opening brace
                    if not stack:
                        return False
                    else:
                        stack_top = stack.pop()
                    
                    if self.is_matching_brace(stack_top, brace):
                        continue
                    else:
                        return False
        
        # Check if stack empty
        if not stack:
            return True
        else:
            return False
    
    def is_matching_brace(self, opening: str, closing: str) -> bool:
        if (opening=='(' and closing==')') or (opening=='{' and closing=='}') or (opening=='[' and closing==']'):
            return True
        return False
```