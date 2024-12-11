tests = []
while True:
    try:
        key, values = [i for i in input().split(": ")]
        key = int(key)
        values = [int(i) for i in values.split()]
        tests.append((key, values))
    except:
        break

count = 0

concat = lambda a, b: int(str(a) + str(b))

def match_test(key, values, value=-1):
    if len(values):
        val = value
        if value == -1:
            val = 1
        if match_test(key, values[1:], val*values[0]):
            return True
        if value == -1:
            val = 0
        if match_test(key, values[1:], val+values[0]):
            return True
        if value == -1:
            val = ""
        if match_test(key, values[1:], concat(val, values[0])):
            return True
    else:
        if key == value:
            return True
    return False
i = 0
for key, values in tests:
    if match_test(key, values, 0):
        count += key
    i += 1
    print(f"{i}/{len(tests)}: {i/len(tests)*100:.2f}% complete")
print(count)