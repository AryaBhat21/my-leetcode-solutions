class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {k:v for k,v in knowledge}
        res = []
        key = []
        inside = False
        for ch in s:
            if ch=="(":
                inside = True
            elif ch==")":
                inside = False
                key_str = "".join(key)
                res.append(d.get(key_str, "?"))
                key.clear()
            elif inside:
                key.append(ch)
            else:
                res.append(ch)
        return "".join(res)