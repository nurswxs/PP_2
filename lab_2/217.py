n = int(input())
asd = {}

for _ in range(n):
    number = input()
    if number in asd:
        asd[number] += 1
    else:
        asd[number] = 1

cnt = 0
for number in asd:
    if asd[number] == 3:
        cnt += 1

print(cnt)
