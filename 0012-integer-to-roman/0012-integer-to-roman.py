class Solution:
    def intToRoman(self, num: int) -> str:
        dict={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        # out=""

        def func(numm):
            out=""
            while numm>0:
                need=0
                for k in dict:
                    if k<=numm:
                        need=max(need,k)
                out=out+dict[need]
                numm=numm-need
            return out
        roman=""
        num=[int(d) for d in str(num)]
        for j in range(len(num)):
            roman=roman+func(num[j]*(10**(len(num)-1-j)))

        return roman