preset = True
presets = dict()
operations = []
while True:
    try:
        inp = input()
        if inp == "":
            preset = False
            continue
        if preset:
            wire, val = inp.split(": ")
            presets[wire] = int(val)
        else:
            wire_1, gate, wire_2, _, wire_out = inp.split()
            operations.append((wire_1, gate, wire_2, wire_out))
    except:
        break

should_check = lambda operation: operation[0] in presets and operation[2] in presets and operation[3] not in presets

def write_to_wire(wire_1, gate, wire_2):
    a, b = presets[wire_1], presets[wire_2]
    if gate == "AND":
        return a & b
    if gate == "OR":
        return a | b
    if gate == "XOR":
        return a ^ b

stop = False
while not stop:
    stop = True
    for operation in filter(should_check, operations):
        stop = False
        wire_1, gate, wire_2, wire_out = operation
        presets[wire_out] = write_to_wire(wire_1, gate, wire_2)

out = "".join(str(presets[i]) for i in reversed(sorted(presets)) if i.startswith("z"))
out = int(out, base=2)
print(out)
