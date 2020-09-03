print("Welcome to car rentals!")
#conditions for budget class
b_base = 40
b_mile = 0.25
#conditions for daily class
d_base = 60
d_mile = 0.25
while True:
    question = input("Would you like to continue (y/n)? ")
    if question == "y":
        code = input("Customer code (b or d): ")
        #customer code b
        if code == "b":
            days = int(input("Number of days: "))
            odo_start = int(input("Odometer reading at the start: "))
            odo_end = int(input("Odometer reading at the end: "))
            miles_driven = odo_end - odo_start
            print("Miles driven:",miles_driven)
            amount_due = round(float((days * b_base) + (miles_driven * b_mile)), 1)
            print("Amount due:",amount_due)
        #customer code d
        elif code == "d":
            days = int(input("Number of days: "))
            odo_start = int(input("Odometer reading at the start: "))
            odo_end = int(input("Odometer reading at the end: "))
            miles_driven = odo_end - odo_start
            print("Miles driven:",miles_driven)
            amount_due = round(float((days * d_base) + ((miles_driven - 100 * days) * d_mile)), 1)
            print("Amount due:",amount_due)    
    else:
        break 