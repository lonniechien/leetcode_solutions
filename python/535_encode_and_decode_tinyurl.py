class Codec:
    def __init__(self):
        self.global_codes = dict()
        self.count = 298313
        self.mywebsite = "lonniechien.github.io/"
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        def randnum():
            self.count = self.count * 198427 + 324989
            return self.count % 62
        def gen_code():
            chars = list("1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
            code = str()
            for i in range(6):
                code += chars[randnum()]
            return code
        code = gen_code()
        while code in self.global_codes:
            code = gen_code()
        self.global_codes[code] = longUrl
        return self.mywebsite + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.lstrip(self.mywebsite)
        return self.global_codes[code]
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
