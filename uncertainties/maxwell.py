from sympy import Eq, solve, symbols

nabla, pt, aL, e0, m0, lam = symbols('∇, ∂_t, α_L, ε_0, µ_0, λ')
D, E, P = symbols('D, E, P')
eq1 = Eq(D, lam*(e0*E + P))
H, B, M = symbols('H, B, M')
eq2 = Eq(H, lam*(aL**2*B/m0 - M))
J, Jf, Jm, Jp = symbols('J, J_f, J_m, J_p')
eq3 = Eq(J, Jf + Jm + Jp)
eq4 = Eq(Jp, pt*P)
eq5 = Eq(Jm, nabla*M/aL)
eq6 = Eq(nabla*B, (m0*J + m0*e0*pt*E)/aL)
s = solve([eq1, eq2, eq3, eq4, eq5, eq6], [E, P, J, H, B, M])
print(f'∇×H = {nabla*s[H]}')