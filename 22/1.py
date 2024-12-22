nums = []
while True:
    try:
        inp = int(input())
        nums.append(inp)
    except:
        break

def secret_calc(secret_number, n):
    mix = lambda x, secret_number: x^secret_number
    prune = lambda x: x % 16777216
    c = secret_number
    for i in range(n):
        c = mix(c*64, c)
        c = prune(c)
        c = mix(c//32, c)
        c = prune(c)
        c = mix(c*2048, c)
        c = prune(c)
    return c
print(secret_calc(1, 2000))
count = sum([secret_calc(num, 2000) for num in nums])
print(count)
