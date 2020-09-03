max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
days_when_amount_acquired = -1
dollars = 0
for i in range(1, max_days+1):
    dollars += (i * i)
    days_when_amount_acquired += 1
    if dollars >= target:
        print('Days needed:',days_when_amount_acquired)
        break
    else:
        continue
else:
    print(0)