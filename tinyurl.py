import hashlib


class Codec:
    def __init__(self):
        self.map = {}
        self.map_inv = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        md5 = hashlib.md5(longUrl.encode('utf-8')).hexdigest()
        self.map[longUrl] = md5
        self.map_inv[md5] = longUrl
        
        return md5

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        return self.map_inv[shortUrl]
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))