import re

class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.complex_multiply(a, b)
    
    def parse_complex(self, cplx):
        cplx = cplx.replace('+-', '-')
        
        p = re.compile("([+-]*\d+)([+-]\d+)i")
        
        real = p.search(cplx).group(1)
        img = p.search(cplx).group(2)
        
        return int(real), int(img)
    
    def complex_multiply(self, a, b):
        r1, i1 = self.parse_complex(a)
        r2, i2 = self.parse_complex(b)
        
        result = str(r1 * r2 - i1 * i2) + '+' + str(i1 * r2 + r1 * i2) + 'i'
        
        return result
                    