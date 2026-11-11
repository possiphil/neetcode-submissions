class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()

        for s in tokens:
            if s == "+":
                a = q.pop()
                b = q.pop()
                q.append(b + a)
            elif s == "-":
                a = q.pop()
                b = q.pop()
                q.append(b - a)
            elif s == "*":
                a = q.pop()
                b = q.pop()
                q.append(b * a)
            elif s == "/":
                a = q.pop()
                b = q.pop()
                q.append(int(b / a))
            else:
                q.append(int(s))
                
        return q.pop()