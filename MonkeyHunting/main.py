import MonkeyHuntingClass as MH

g_acc=-9.80655

xb = 0.0
zb = 0.0

xm = 1.0
zm = 1.0

v_abs=10.0

MH = MH.MonkeyHunting(g_acc)

MH.set_initial_bullet_position(xb,zb)
MH.set_initial_monkey_position(xm,zm)
MH.set_ground(0.0)
[flag,theta] = MH.solve_theta(v_abs)
if flag:
    print(theta)
else:
    print("Can not find the solution.")
