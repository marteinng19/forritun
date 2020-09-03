num = int(input("enter number of fibonacci numbers:"))

last = 0
new = 1
for i in range(0, num):
    temp = last
    last = new
    new = temp + new
    print(new)

