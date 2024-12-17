import re
A = int(re.findall("[0-9]+", input())[0])
B = int(re.findall("[0-9]+", input())[0])
C = int(re.findall("[0-9]+", input())[0])
output = []
input()

def combo(operand):
    global A, B, C
    if 0 <= operand <= 3:
        return operand
    return [A, B, C][operand-4]
ops = [int(i) for i in re.findall("[0-9]+", input())]
idx = 0
def adv(operand):
    global A
    A = A//(2**combo(operand))
def bxl(operand):
    global B
    B = B ^ operand
def bst(operand):
    global B
    B = combo(operand) % 8
def jnz(operand):
    global A, idx
    if A == 0:
        return
    idx = operand
    return "jumped"
def bxc(operand):
    global B, C
    B = B ^ C
def out(operand):
    output.append(combo(operand)%8)
def bdv(operand):
    global A, B
    B = A//(2**combo(operand))
def cdv(operand):
    global A, C
    C = A//(2**combo(operand))

mapping = {0: adv, 1: bxl, 2: bst, 3:jnz, 4:bxc, 5: out, 6: bdv, 7:cdv}

while idx < len(ops):
    instr = ops[idx]
    operand = ops[idx+1]
    func = mapping[instr]
    idx += 2
    func(operand)
print(",".join(str(i) for i in output), A, B, C)
