f = int(input("Enter height in feet"))
i = int(input("Enter remaining inches"))

C = (f * 30.48) + (i * 2.54)

print("Centimeters", C)
 
if C > 150:
     print("You are tall")

if C < 150:
    print("You are short")
