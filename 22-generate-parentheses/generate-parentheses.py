class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current_str: list[str], open_count: int, close_count: int):
            if len(current_str) == 2 * n:
                
                result.append("".join(current_str))
                return

            if open_count < n:
                current_str.append("(")
                backtrack(current_str, open_count + 1, close_count)
                current_str.pop()  # undo choice

            if close_count < open_count:
                current_str.append(")")
                backtrack(current_str, open_count, close_count + 1)
                current_str.pop()  # undo choice

        backtrack([], 0, 0)
        return result