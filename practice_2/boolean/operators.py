#1 Python operators
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
#2---> Arithmetic operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
#3--->Assigment operators
x = 5	#x = 5	
x += 3	#x = x + 3	
x -= 3	#x = x - 3	
x *= 3	#x = x * 3	
x /= 3	#x = x / 3	
x %= 3	#x = x % 3	
x //= 3	#x = x // 3	
x **= 3	#x = x ** 3	
x &= 3	#x = x & 3	
x |= 3	#x = x | 3	
x ^= 3	#x = x ^ 3	
x >>= 3	#x = x >> 3	
x <<= 3	#x = x << 3	
print(x := 3)	#x = 3 --- print(x)
#4
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
#5--->Bitwise operators
x = 5
y = 4
x & y  #Sets each bit to 1 if both bits are 1	
x | y  #Sets each bit to 1 if one of two bits is 1		
x ^ y  #Sets each bit to 1 if only one of two bits is 1		
~x     #Inverts all the bits		
x << 2 #Zero fill left shift	
#Shift left by pushing zeros in from the right and let the leftmost bits fall off		
x >> 2 #Signed right 
#Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	

