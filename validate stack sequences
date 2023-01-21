class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for num in pushed:
            stack.append(num)
            if num == popped[j]:
                while stack and popped[j]==stack[-1]:
                    j += 1
                    stack.pop()
        if stack:
            return False
        return True
