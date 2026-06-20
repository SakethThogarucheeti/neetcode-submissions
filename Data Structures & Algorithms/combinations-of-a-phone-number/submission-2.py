class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtl = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        res = []
        part = []
        def dfs(didx):
            if didx >= len(digits):
                res.append("".join(part))
                return
            d = digits[didx]
            chars = dtl[d]
            for c in chars:
                part.append(c)
                dfs(didx + 1)
                part.pop()
        dfs(0)
        return res

        