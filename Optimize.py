from gekko import GEKKO
m = GEKKO(remote=True)
ret = [0.2, 0.15]
ret_var = [0.002, 0.0015]
l_plus = [0, 0]
p = [0.005, 0.005]

# init variable
u1 = m.sos1([0, 1])
u2 = m.sos1([0, 1])
# u1 = m.Var(lb=0, ub=1, integer=True)
# u2 = m.Var(lb=0, ub=1, integer=True)


w1 = m.Var(lb=0, ub=1)
w2 = m.Var(lb=0, ub=1)
# w1_plus = m.Var(lb=0.05*u1, ub=0.2*u1)
# w2_plus = m.Var(lb=0.05*u2, ub=0.2*u2)

w1.value = 0
w2.value = 0



# Objective
m.Minimize(w1**2*ret_var[0]**2 + w2**2*ret_var[1]**2)
m.Minimize(w1**2*ret_var[0]**2 + w2**2*ret_var[1]**2 + 2*w1*w2*ret_var[0]*ret_var[1])
m.Minimize(-(ret[0]*w1 + ret[1]*w2))
m.Minimize(p[0]*l_plus[0] + p[0]*l_plus[1])


# Equations
m.Equation(w1 + w2 == 1)

# Weight Constraints
# Cause of there's only two of the asset, so set the maximize lager then usual
m.Equation(w1/u1 >= 0.1)
m.Equation(w1/u1 <= 0.8)
m.Equation(w2/u2 >= 0.1)
m.Equation(w2/u2 <= 0.8)


m.solve()
print('w1: ' + str(w1.value))
print('w2: ' + str(w2.value))


