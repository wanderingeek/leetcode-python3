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
                    # Also handle encounter of closing brace before opening brace
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