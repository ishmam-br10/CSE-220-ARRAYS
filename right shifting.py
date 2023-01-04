# Shifting (right)
a = [10, 20, 30, 40, 50]
b = [0] * 5

# ekhane miss pura ta dekhan nai
for i in range(len(a) - 1):
    b[i] = a[i]

print(b)
