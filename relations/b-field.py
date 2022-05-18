from sympy import Eq, solve, symbols

r_n, v_n, f_n, q_si, q_g, q_n, b_si, b_g, b_n = symbols('r_N, v_N, F^N, q^SI, q^G, q^N, B^SI, B^G, B^N')
pi, hbar, c, e, a = symbols('π, ħ, c, e, α')
e0 = e**2/4/pi/hbar/c/a
m0 = 4*pi*hbar*a/c/e**2
r = hbar*c*r_n
f = f_n/hbar/c
v = v_n*c
eq_si = Eq(f, q_si**2/4/pi/e0/r**2)
eq_g = Eq(f, q_g**2/r**2)
eq_n = Eq(f_n, q_n**2/4/pi/r_n**2)
s_si = solve(Eq(eq_si.lhs/eq_n.lhs, eq_si.rhs/eq_n.rhs), q_n)
s_g = solve(Eq(eq_g.lhs/eq_n.lhs, eq_g.rhs/eq_n.rhs), q_n)
# choose s_si[1] (positive) and s_g[1] (positive)
print(f'q^N = {s_si[1]/q_si} q^SI = {s_g[1]/q_g} q^G')
q_si = q_si/s_si[1]*q_n
q_g = q_g/s_g[1]*q_n
eq_si = Eq(f, q_si*v*b_si)
eq_g = Eq(f, q_g*v*b_g/c)
eq_n = Eq(f_n, q_n*v_n*b_n)
s_si = solve(Eq(eq_si.lhs/eq_n.lhs, eq_si.rhs/eq_n.rhs), b_n)
s_g = solve(Eq(eq_g.lhs/eq_n.lhs, eq_g.rhs/eq_n.rhs), b_n)
print(f'B^N = {s_si[0]/b_si} B^SI = {s_g[0]/b_g} B^G')
b_si = b_si/s_si[0]*b_n
b_g = b_g/s_g[0]*b_n

qm_g, qm_n, qm_w, qm_a, qm_c = symbols('q_m^G, q_m^N, q_m^W, q_m^A, q_m^C')
eq_g = Eq(f, qm_g*b_g)
eq_n = Eq(f_n, qm_n*b_n)
eq_w = Eq(f, qm_w*b_si/m0)
eq_a = Eq(f, qm_a*b_si)
eq_c = Eq(f, c*qm_c*b_si)
s_g = solve(Eq(eq_g.lhs/eq_n.lhs, eq_g.rhs/eq_n.rhs), qm_n)
s_w = solve(Eq(eq_w.lhs/eq_n.lhs, eq_w.rhs/eq_n.rhs), qm_n)
print(f'q_m^N = {s_g[0]/qm_g} q_m^G = {s_w[0]/qm_w} q_m^W')
s_n = solve(Eq(eq_n.lhs/eq_c.lhs, eq_n.rhs/eq_c.rhs), qm_c)
s_a = solve(Eq(eq_a.lhs/eq_c.lhs, eq_a.rhs/eq_c.rhs), qm_c)
print(f'{s_n[0]/qm_n} q_m^N = {s_a[0]/qm_a} q_m^A = q_m^C')