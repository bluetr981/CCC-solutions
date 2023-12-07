d = int(input())
e = int(input())
w = int(input())
if d <= 100:
    a_cost = round(0.15*e+0.20*w, 2)
else:
    a_cost = 0.25*(d-100)+0.15*e+0.20*w
    b_cost = 0.45*(d-250)+0.35*e+0.25*w
if d in range(0, 251):
    b_cost = round(0.35*e+0.25*w, 2)
if a_cost < 0:
    a_cost = round(0.15*e+0.20*w, 2)
if b_cost < 0:
    b_cost = round(0.35*e+0.25*w, 2)
print("Plan A costs", '%.2f' % a_cost)
print("Plan B costs", '%.2f' % b_cost)
if a_cost > b_cost:
    print("Plan B is cheapest.")
elif a_cost == b_cost:
    print("Plan A and B are the same price.")
else:
    print("Plan A is cheapest.")
