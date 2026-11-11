class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()

        for s in tokens:
            if s == "+":
                q.append(q.pop() + q.pop())
            elif s == "-":
                a,b = q.pop(),q.pop()
                q.append(b - a)
            elif s == "*":
                q.append(q.pop() * q.pop())
            elif s == "/":
                a,b = q.pop(),q.pop()
                q.append(int(b / a))
            else:
                q.append(int(s))
                
        return q[0]