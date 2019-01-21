import random


class Codec:
    def __init__(self):
        self.decode_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        key = ''.join([chr(random.randint(0, 255)) for _ in range(5)])

        self.decode_dict[key] = longUrl

        return key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        return self.decode_dict[shortUrl]