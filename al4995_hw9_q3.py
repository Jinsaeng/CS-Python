class BinaryPositiveInteger:
    def __init__(self, num):
        self.num = num
        self.string = ""
        
    def __add__(self, other):
        self.num = self.num + self.other
        return self.num
    
    def __lt__(self_other):
        if self.num < self.other:
            return True
        else:
            return False
        
    def is_power_of_2(self):
        if self.num % 2 == 0:
            return True
        else:
            return False
        
    def largest_power_of_2(self):
        power = 2
        while int(self.num) % power == 0:
            power = power ** 2

        return power
    
    def __repr__(self):
        divisor = 128
        while self.num >0:
            if self.num > divisor:
                self.num -= divisor
                self.string += "1"
                divisor /= 2
            else:
                self.string += "0"
                divisor /=2
        return self.string

def main():
    print(BinaryPositiveInteger.largest_power_of_2("16"))
main()
