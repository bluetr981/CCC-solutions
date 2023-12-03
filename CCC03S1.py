x = 1
while x!=100:
    a = int(input())
    if x+a==9:
        x += a+25
    elif x+a==40:
        x += a+24
    elif x+a==67:
        x += a+19
    elif x+a==34:
        x += a
        x -= 25
    elif x+a==64:
        x += a
        x -= 24
    elif x+a==86:
        x += a
        x -= 19
    elif x+a>100:
        x -= 0
    elif x+a==54:
        x += a
        x -= 35
    elif x+a==99:
        x += a
        x -= 22
    elif x+a==90:
        x += a
        x -= 42
    else:
        x += a
    if a == 0:
        print("You Quit!")
        break
    if x == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    else:
        print("You are now on square", x)
