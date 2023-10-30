class Solution:
    def interpret(self, command: str) -> str:
        #return command.replace("()","o").replace("(al)","al")
        dic = {"()":"o","(al)":"al"}
        section = str()
        ans = str()
        for char in command:
            if char == "G":
                ans += char
                continue
            section += char
            if section in dic:
                ans += dic[section]
                section = str()
        return ans
