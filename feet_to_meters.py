from ftm_parse import parse, convert

feet_inches = input("enter feet and inches: ")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("the kids are alright!")
else:
    print("the kids are not alright")
