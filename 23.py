#deg F/ deg C

unit=input("Enter unit of temperature(F/C):")
temp=float(input("Enter temperature:"))

if unit=='F':
    temp=(temp-32)*5/9
    print("The temperature in degree celsius is",temp,end=".")
elif unit=='C':
    temp=(9/5*temp)+32
    print("The temperature in degree fahrenheit is", temp, end=".")