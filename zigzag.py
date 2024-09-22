import time, sys
whitespace = 0
grow = True
while True:
    gap = " " * whitespace
    print(gap + "**********")
    time.sleep(0.1)
    if grow:
        whitespace = whitespace + 1
    else:
        whitespace = whitespace - 1
    if whitespace == 20:
        grow = False
    if whitespace == 0:
        grow = True
