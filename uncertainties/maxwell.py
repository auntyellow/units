from sympy import Eq, solve, symbols

nabla, pt, c, aL, aH, aM, e0, m0, lam = symbols('∇, ∂_t, c, α_L, α_H, α_M, ε_0, µ_0, λ')
D, E, P = symbols('D, E, P')
eq1 = Eq(D, lam*(e0*E + P))
H, B, M = symbols('H, B, M')
eq2 = Eq(H, lam*(aH*B/m0 - M))
J, Jf, Jm, Jp = symbols('J, J_f, J_m, J_p')
eq3 = Eq(J, Jf + Jm + Jp)
eq4 = Eq(nabla*B, (m0*J + pt*E/c**2)/aL)
eq5 = Eq(Jm, aM*nabla*M)
eq6 = Eq(Jp, pt*P)
# TODO: H = f(Jf, D)?