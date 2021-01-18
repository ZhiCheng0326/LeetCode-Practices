class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                tmp = '' # store the string within brackets
                while stack[-1] != "[":
                    p = stack.pop()
                    tmp = p + tmp
                stack.pop() # remove '['

                ## extract k for multiplication
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)

                encoded_string = k*tmp

                ## append the decoded string into stack
                for t in encoded_string:
                    stack.append(t)
        return "".join(stack)
