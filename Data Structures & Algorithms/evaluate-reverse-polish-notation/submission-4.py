class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])
        print(ops)
        s = []

        i = 0
        while i in range(len(tokens)):
            print(s)
            curr = tokens[i]
            if curr not in ops:
                s.append(int(curr))
            else:
                if curr == '+':
                    s.append(s.pop() + s.pop())
                elif curr == '-':
                    a,b = s.pop(), s.pop()
                    s.append(b-a)
                elif curr == '*':
                    s.append(s.pop() * s.pop())
                elif curr == '/':
                    a,b = s.pop(), s.pop()
                    s.append(int(float(b)/a))
            i += 1
        
        return s[0]

        