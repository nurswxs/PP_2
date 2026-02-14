expression = input().strip()

digit_map = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

reverse_map = {
    "0": "ZER", "1": "ONE", "2": "TWO", "3": "THR", "4": "FOU",
    "5": "FIV", "6": "SIX", "7": "SEV", "8": "EIG", "9": "NIN"
}

if '+' in expression:
    operator = '+'
elif '-' in expression:
    operator = '-'
else:
    operator = '*'

left, right = expression.split(operator)

num1 = ""
for i in range(0, len(left), 3):
    num1 += digit_map[left[i:i+3]]

num2 = ""
for i in range(0, len(right), 3):
    num2 += digit_map[right[i:i+3]]

num1 = int(num1)
num2 = int(num2)

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
else:
    result = num1 * num2

result_str = ""
for digit in str(result):
    result_str += reverse_map[digit]

print(result_str)
