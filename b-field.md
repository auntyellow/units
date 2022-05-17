## Magnetic B Field in SI, Gaussian and Natural Units

In this page, constants <img src="https://latex.codecogs.com/gif.latex?\hbar">, *c* and *e* are in SI units and they all have exact values; the dimensionless constant *α* has a relative uncertainty of 0.15 ppb in CODATA-2018.

### Mechanics

In natural units:

- length and time are represented as the reciprocal of energy: <img src="https://latex.codecogs.com/gif.latex?l=ct=c/\omega={\hbar}c/E">
- force is represented as the square of energy: <img src="https://latex.codecogs.com/gif.latex?F=E/l=E/ct=E\omega/c=E^2/{\hbar}c">
- velocity is dimensionless

Therefore, the relations among SI, Gaussian and natural units for length, force and velocity are:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}l={{\hbar}c}\;l^\text{N}&(1)\\[1em]F=\dfrac{F^\text{N}}{{\hbar}c}&(2)\\[1em]v=v^\text{N}c&(3)\end{cases}">

### Electric Charge

The dimension of electric charge can be determined by Coulomb's law in different unit systems:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}F=\dfrac{q^\text{SI}_1q^\text{SI}_2}{4\pi\varepsilon_0r^2}&(4)\\[1em]F=\dfrac{q^\text{G}_1q^\text{G}_2}{r^2}&(5)\\[1em]F^\text{N}=\dfrac{q^\text{N}_1q^\text{N}_2}{4{\pi}r^\text{N2}}&(6)\end{cases}">

Apply (1) and (2) on (4), (5) and (6): <sup>[1,2]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{\sqrt{4\pi\alpha}}e\;q^\text{SI}=\sqrt{\frac{4\pi}{{\hbar}c}}\;q^\text{G}=q^\text{N}\quad(7)">

### Magnetic B Field

The dimension of magnetic **B** field can be determined by Lorentz force in different unit systems:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{F}^\text{SI}=q^\text{SI}\mathbf{v}\times\mathbf{B}^\text{SI}&(8)\\[1em]\mathbf{F}^\text{G}=\dfrac{q^\text{G}}c\mathbf{v}\times\mathbf{B}^\text{G}&(9)\\[1em]\mathbf{F}^\text{N}=q^\text{N}\mathbf{v}^\text{N}\times\mathbf{B}^\text{N}&(10)\end{cases}">

Apply (2), (3) and (7) on (8), (9) and (10): <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{{\hbar}c^2e}{\sqrt{4\pi\alpha}}\;\mathbf{B}^\text{SI}={\hbar}c\sqrt{\frac{{\hbar}c}{4\pi}}\;\mathbf{B}^\text{G}=\mathbf{B}^\text{N}\quad(11)">

### Notes

1. [Here](uncertainties/b-field.py) are the calculations.
2. <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=e^2/4\pi{\hbar}c\alpha">