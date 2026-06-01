class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        p = 0

        while p < len(s):
            curr = s[p]
            if curr not in m:
                stack.append(curr)
            else:
                opp = m[curr]

                if len(stack)>0 and stack[-1] == opp:
                    stack.pop()
                else:
                    return False
            
            p += 1
        return len(stack) == 0
        