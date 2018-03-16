class RomanNumer(object):

    def __init__(self, num):
        self.num = num;
        self.digit_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        
    def convert_to_decimal(self):
        val = 0
        for m in self.num:
            val += self.digit_map[m]
        print(val)
        return val
