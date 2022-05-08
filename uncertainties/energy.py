from uncertainties import ufloat
from math import pi

c = 299792458
h = 6.62607015e-34
hbar = h/2/pi
cal = 4.184
eV = 1.602176634e-19
na = 6.02214076e+23
# https://physics.nist.gov/cgi-bin/cuu/Value?ryd
r_inf = 10973731.568160
r_inf = ufloat(r_inf, r_inf*1.9e-12)
units = ['Hartree', 'eV', 'kcal/mol', 'kJ/mol', 'cm^-1', 'GHz']
units_j = [4*pi*hbar*c*r_inf, eV, cal*1000/na, 1000/na, 100*h*c, 1e+09*h]
print('|', end='')
for i in range(6):
    print(units[i], end='|')
print()
for i in range(6):
    print('|', units[i], sep='', end='|')
    for j in range(6):
        if i == j:
            print(1, end='|')
        elif i == 0 or j == 0:
            print('{:S}'.format(units_j[i]/units_j[j]), end='|')
        else:
            print(units_j[i]/units_j[j], end='|')
    print()