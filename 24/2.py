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

with open("input.gv", "w") as f:
    f.write("Digraph G {\n")
    for operation in operations:
        wire_1, gate, wire_2, wire_out = operation
        f.write(f"{wire_1} -> {wire_1}_{gate}_{wire_2};\n")
        f.write(f"{wire_2} -> {wire_1}_{gate}_{wire_2};\n")
        f.write(f"{wire_1}_{gate}_{wire_2} -> {wire_out};\n")
    f.write("}\n")

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
a1 = "".join(str(presets[i]) for i in reversed(sorted(presets)) if i.startswith("x"))
a2 = "".join(str(presets[i]) for i in reversed(sorted(presets)) if i.startswith("y"))
actual = bin(int(a1, base=2) + int(a2, base=2))[2:]
out = "".join(str(presets[i]) for i in reversed(sorted(presets)) if i.startswith("z"))
print(a1)
print(a2)
print(actual)
print(out)
for idx, i in enumerate(actual[::-1]):
    if i != out[::-1][idx]:
        print(f"Problem at z{idx-1}")
        break
