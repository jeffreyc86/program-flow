# indentation is important in python
# use the colon (:) to start a new code block
# if indented then the code will be part of a code block

for i in range(1, 6):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
print("*" * 80)
# No. 1 squared is 1 and cubed is    1
# No. 2 squared is 4 and cubed is    8
# No. 3 squared is 9 and cubed is   27
# No. 4 squared is 16 and cubed is   64
# No. 5 squared is 25 and cubed is  125
# ********************************************************************************

for i in range(1, 6):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    print("*" * 80)
# No. 1 squared is 1 and cubed is    1
# ********************************************************************************
# No. 2 squared is 4 and cubed is    8
# ********************************************************************************
# No. 3 squared is 9 and cubed is   27
# ********************************************************************************
# No. 4 squared is 16 and cubed is   64
# ********************************************************************************
# No. 5 squared is 25 and cubed is  125
# ********************************************************************************



