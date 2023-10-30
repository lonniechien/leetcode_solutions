class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = str()
        for char in address:
            if char == '.':
                defanged += "[.]"
            else:
                defanged += char
        return defanged
