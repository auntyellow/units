## 3. Polarization and Magnetization

### Electric Polarization and Displacement Field

[Electric Polarization](https://en.wikipedia.org/wiki/Polarization_density) is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\frac{\text{d}\mathbf{p}}{\text{d}V}">

where **p** is the electric dipole moment and *V* is the volume.

Gauss's law for **P** is: <sup>[1,2]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b\quad(3.1)">

where *ρ*<sub>*b*</sub> is the bound charge density.

The free charge density is:

<img src="https://latex.codecogs.com/gif.latex?\rho_f=\rho-\rho_b">

Let's define [Electric Displacement Field](https://en.wikipedia.org/wiki/Electric_displacement_field) (in SI units) as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}^\text{SI}=\varepsilon_0\mathbf{E}^\text{SI}+\mathbf{P}^\text{SI}\quad(3.2\text{a})">

and apply Gauss's law for **E**:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}^\text{SI}=\frac{\rho^\text{SI}}{\varepsilon_0}\quad(3.3\text{a})">

Then we get Gauss's law for **D**:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{D}^\text{SI}=\rho_f^\text{SI}\quad(3.4\text{a})">

The above equations in Gaussian units are:

<img src="https://latex.codecogs.com/gif.latex?\begin{array}{ll}\mathbf{D}^\text{G}=\mathbf{E}^\text{G}+4\pi\mathbf{P}^\text{G}&(3.2\text{b})\\\nabla\cdot\mathbf{E}^\text{G}=4\pi\rho^\text{G}&(3.3\text{b})\\\nabla\cdot\mathbf{D}^\text{G}=4\pi\rho_f^\text{G}&(3.4\text{b})\end{array}">

From (2.1) mentioned [here](cgs.md), (3.1), and relation between (3.4a) and (3.4b) we get that: 

- Electric field **E**: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}\overset{\frown}=29979.2458082(22)\;\text{V/m}">
- Electric polarization **P**: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}=1\;\text{statC/cm}^2\overset{\frown}=3.33564095107(25){\times}10^{-6}\;\text{C/m}^2">
- Electric displacement field **D**: <sup>[3]</sup> <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}\overset{\frown}=2.65441872871(20)10^{-7}\;\text{C/m}^2">

### Notes

1. These holds in all unit systems.
2. [Here](https://en.wikipedia.org/wiki/Polarization_density#Gauss's_law_for_the_field_of_P) is the explanation.
3. [Here](uncertainties/displacement.py) is the calculation.