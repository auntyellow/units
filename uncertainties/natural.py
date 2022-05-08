from uncertainties import ufloat
from math import pi

c = 299792458
h = 6.62607015e-34
hbar = h/2/pi
eV = 1.602176634e-19
nu_mass = eV/c**2
nu_momentum = eV/c
nu_freq = eV/hbar
nu_time = 1/nu_freq
nu_length = c*nu_time
nu_force = nu_momentum/nu_time
print(f'1      = {hbar} J s')
print(f'1 eV   = {nu_mass} kg')
print(f'1 eV   = {nu_momentum} kg m/s')
print(f'1 eV   = {nu_freq} Hz')
print(f'1/eV   = {nu_time} s')
print(f'1/eV   = {nu_length} m')
print(f'1 eV^2 = {nu_force} N')

# https://physics.nist.gov/cgi-bin/cuu/Value?alph
a = 7.2973525693e-03
a = ufloat(a, a*1.5e-10)
nu_e = (4*pi*a)**.5
nu_charge = eV/nu_e
nu_e_field = nu_force/nu_charge
nu_b_field = nu_e_field/c
print(f'1 e    = {nu_e:S}')
print(f'1      = {nu_charge:S} C')
print(f'1 eV^2 = {nu_e_field:S} V/m')
print(f'1 eV^2 = {nu_b_field:S} T')