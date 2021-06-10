age = int(input("How old are you? "))

# and - both conditions need to be true
# or - at least one condition needs to be true

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("You're old enough to work")
else:
    print("Enjoy not working")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy not working")
else:
    print("You're old enough to work")