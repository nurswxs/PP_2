#1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#2--->Values are true
print(bool("Hello"))
print(bool(15))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#3--->Values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#4
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
