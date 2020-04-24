string_n = list(input())
count = 0
for i in range(0, len(string_n)):
    if 65 <= ord(string_n[i]) <=90:
        count = count + 1

print(count + 1)
