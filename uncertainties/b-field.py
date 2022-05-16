from sympy import Eq, solve, symbols

r_n, v_n, f_n, q_si, q_g, q_n, b_si, b_g, b_n = symbols('r_N, v_N, F^N, q^SI, q^G, q^N, B^SI, B^G, B^N')
pi, hbar, c, e, a = symbols('π, ħ, c, e, α')
e0 = e**2/4/pi/hbar/c/a
r = hbar*c*r_n
f = f_n/hbar/c
v = v_n*c
eq4 = Eq(f, q_si**2/4/pi/e0/r**2)
eq5 = Eq(f, q_g**2/r**2)
eq6 = Eq(f_n, q_n**2/4/pi/r_n**2)
s46 = solve(Eq(eq4.lhs/eq6.lhs, eq4.rhs/eq6.rhs), q_n)
s56 = solve(Eq(eq5.lhs/eq6.lhs, eq5.rhs/eq6.rhs), q_n)
# choose s46[1] (positive) and s56[1] (positive)
print(f'q^N = {s46[1]/q_si} q^SI = {s56[1]/q_g} q^G')
q_si = q_si/s46[1]*q_n
q_g = q_g/s56[1]*q_n
eq8 = Eq(f, q_si*v*b_si)
eq9 = Eq(f, q_g*v*b_g/c)
eq10 = Eq(f_n, q_n*v_n*b_n)
s810 = solve(Eq(eq8.lhs/eq10.lhs, eq8.rhs/eq10.rhs), b_n)
s910 = solve(Eq(eq9.lhs/eq10.lhs, eq9.rhs/eq10.rhs), b_n)
print(f'B^N = {s810[0]/b_si} B^SI = {s910[0]/b_g} B^G')