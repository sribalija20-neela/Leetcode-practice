class Solution:
    def isValid(self, s: str) -> bool:
        backpack = []
        tape_matches = {")": "(", "}": "{", "]": "["}
        
        for symbol in s:
            if symbol in tape_matches:
                if not backpack or backpack[-1] != tape_matches[symbol]:
                    return False
                backpack.pop()
            else:
                backpack.append(symbol)
                
        return len(backpack) == 0
