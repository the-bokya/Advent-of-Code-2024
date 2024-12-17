import re
"""
oA = int(re.findall("[0-9]+", input())[0])
oB = int(re.findall("[0-9]+", input())[0])
oC = int(re.findall("[0-9]+", input())[0])
input()
"""
#ops = [int(i) for i in re.findall("[0-9]+", input())]
ops = [2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]
class Comp:
    def __init__(self, A):
        self.ops = [2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]
        self.digit_matches = []
        self.A = A
        self.B = 0
        self.C = 0
        self.idx = 0
        self.output = []
        self.mapping = {0: self.adv,
                        1: self.bxl,
                        2: self.bst,
                        3: self.jnz,
                        4: self.bxc,
                        5: self.out,
                        6: self.bdv,
                        7: self.cdv,
                        }
    def combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        return [self.A, self.B, self.C][operand-4]
    def adv(self, operand):
        self.A = self.A//(2**self.combo(operand))
    def bxl(self, operand):
        self.B = self.B ^ operand
    def bst(self, operand):
        self.B = self.combo(operand) % 8
    def jnz(self, operand):
        if self.A == 0:
            return
        self.idx = operand
        return "jumped"
    def bxc(self, operand):
        self.B = self.B ^ self.C
    def out(self, operand):
        self.output.append(self.combo(operand)%8)
    def bdv(self, operand):
        self.B = self.A//(2**self.combo(operand))
    def cdv(self, operand):
        self.C = self.A//(2**self.combo(operand))
    
    def calc(self):
        self.idx = 0
        while self.idx < len(self.ops):
            instr = self.ops[self.idx]
            operand = self.ops[self.idx+1]
            func = self.mapping[instr]
            self.idx += 2
            func(operand)
        return self.output
def bktk(mult, adds, digs):
    new_adds = []
    digit_matches = []
    not_found = False
    for add in adds:
        iA = 1
        while True:
            im = iA*mult + add
            output = Comp(im).calc()
            if output[:digs] == ops[:digs]:
                new_adds.append(im)
            
            digit_matches.append(output[digs-1])
            iA += 1
            print(output, im, digs)
            if digit_matches[:len(digit_matches)//2] == digit_matches[len(digit_matches)//2:] and iA > 3:
                new_adds = new_adds[:len(new_adds)//2]
                digit_matches = digit_matches[:len(digit_matches)//2]
                print(output)
                break
            if iA > 2048:
                not_found = True
                break
        if not_found:
            return
        print(new_adds, iA)
        bktk(mult*(iA//2), new_adds, digs+1)
digs = 1
mult = 0
for digs in range(17):
    for j in range(100):
        i = mult*8 + j
        current = Comp(i).calc()
        if current == ops[len(ops)-digs:]:
            mult = i
            print(digs, mult, current)
            continue
