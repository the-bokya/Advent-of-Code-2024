from collections import Counter
nums = []
while True:
    try:
        inp = int(input())
        nums.append(inp)
    except:
        break

def secret_calc(secret_number, n):
    price_changes = []
    digit = secret_number % 10
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
        price_changes.append((c%10, c%10 - digit))
        digit = c % 10
    return c, price_changes

count_all = Counter()
for num in nums:
    counter = Counter()
    secret_number, price_changes = secret_calc(num, 2000)
    for i in range(len(price_changes)-4):
        price, _ = price_changes[i+3]
        seq = tuple([y for x, y in price_changes[i:i+4]])
        if seq not in counter:
            counter[seq] = price
    count_all += counter
print(count_all.most_common(1)[0][1])
