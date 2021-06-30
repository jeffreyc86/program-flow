# when using range, python will iterate from the start up to but not including the end

for i in range(1, 10):
    print("i is now {}".format(i))

# i is now 1
# i is now 2
# i is now 3
# i is now 4
# i is now 5
# i is now 6
# i is now 7
# i is now 8
# i is now 9

# if only one parameter is passed into range
# it will act as the end value and the start value will default to 0

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

# step values can also be passed into range
for i in range(0, 10, 2):
    print(i)

# 0
# 2
# 4
# 6
# 8

# step values can also be negative to count backwards BUT the start value must be after the end value
for i in range(10, 0, -2):
    print(i)

# 10
# 8
# 6
# 4
# 2


