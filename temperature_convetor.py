#temperature convertor alrt+0176=°

unit=input("is this temp in celsius or fahrenheit (C/F):")
temp=float(input("enter the temperature:"))

if unit.upper()=="C":
    temp=round((9*temp)/5+32,3)
    print(f"the temp in fahrenheit is:{temp}°F")

elif unit.upper()=="F":
    temp=round((temp-32)*5/9,1)
    print(f"the temp in celcius is:{temp}°C")

else:
    print(f"{unit} is an invalid unit of measurement")
