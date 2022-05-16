## Magnetic B Field in SI, Gaussian and Natural Units

### Force

In natural units, length and time are represented as the reciprocal of energy, and force is represented as the square of energy:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{E}l=\frac{E}{ct}=\frac{E\omega}c=\frac{E^2}{{\hbar}c}">

Therefore, the relation among SI, Gaussian and natural units for force is:

<img src="https://latex.codecogs.com/gif.latex?F^\text{SI}=F^\text{G}=\frac{F^\text{N}}{{\hbar}c}\quad(1)">

### Electric Charge

The dimension of electric charge can be determined by Coulomb's law in different unit systems:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}F^\text{SI}=\dfrac{q^\text{SI}_1q^\text{SI}_2}{4\pi\varepsilon_0r^2}&(2)\\[1em]F^\text{G}=\dfrac{q^\text{G}_1q^\text{G}_2}{r^2}&(3)\\[1em]F^\text{N}=\dfrac{q^\text{N}_1q^\text{N}_2}{4{\pi}r^2}&(4)\end{cases}">

Apply (1) on (2), (3) and (4): <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{\sqrt{4\pi\alpha}{\hbar}c}e\;q^\text{SI}=\sqrt{4\pi{\hbar}c}\;q^\text{G}=q^\text{N}\quad(5)">

### Magnetic B Field

The dimension of magnetic **B** field can be determined by Lorentz force in different unit systems:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{F}^\text{SI}=q^\text{SI}\mathbf{v}\times\mathbf{B}^\text{SI}&(6)\\[1em]\mathbf{F}^\text{G}=\dfrac{q^\text{G}}c\mathbf{v}\times\mathbf{B}^\text{G}&(7)\\[1em]\mathbf{F}^\text{N}=q^\text{N}\mathbf{v}\times\mathbf{B}^\text{N}&(8)\end{cases}">

Apply (1) and (5) on (6), (7) and (8): <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{e}{\sqrt{4\pi\alpha}}\;\mathbf{B}^\text{SI}=\sqrt{\frac{c}{\hbar\alpha}}e\;\mathbf{B}^\text{G}=\mathbf{B}^\text{N}\quad(9)">

### Note

1. [Here](uncertainties/b-field.py) are the calculations.