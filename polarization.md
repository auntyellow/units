## 3. Polarization and Magnetization

### Electric Polarization and Displacement Field

The [Electric Polarization](https://en.wikipedia.org/wiki/Polarization_density) is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\frac{\text{d}\mathbf{p}}{\text{d}V}">

where **p** is the electric dipole moment and *V* is the volume.

Gauss's law for **P** is: <sup>[1,2]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b\quad(3.1)">

where *ρ*<sub>*b*</sub> is the bound charge density.

The free charge density is:

<img src="https://latex.codecogs.com/gif.latex?\rho_f=\rho-\rho_b">

The [Electric Displacement Field](https://en.wikipedia.org/wiki/Electric_displacement_field) (in SI units) is defined as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}^\text{SI}=\varepsilon_0\mathbf{E}^\text{SI}+\mathbf{P}^\text{SI}\quad(3.2\text{a})">

And apply Gauss's law for **E**:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}^\text{SI}=\frac{\rho^\text{SI}}{\varepsilon_0}\quad(3.3\text{a})">

Then we get Gauss's law for **D**:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{D}^\text{SI}=\rho_f^\text{SI}\quad(3.4\text{a})">

The above equations in Gaussian units are:

<img src="https://latex.codecogs.com/gif.latex?\begin{array}{ll}\mathbf{D}^\text{G}=\mathbf{E}^\text{G}+4\pi\mathbf{P}^\text{G}&(3.2\text{b})\\[1em]\nabla\cdot\mathbf{E}^\text{G}=4\pi\rho^\text{G}&(3.3\text{b})\\[1em]\nabla\cdot\mathbf{D}^\text{G}=4\pi\rho_f^\text{G}&(3.4\text{b})\end{array}">

From [(2.1)](cgs.md#2.1), (3.1), relation between (3.4a) and (3.4b), and <img src="https://latex.codecogs.com/gif.latex?\rho^\text{SI}=\sqrt{4\pi\varepsilon_0}\rho^\text{G}">, we get that:

- Electric field **E**: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}\overset{\frown}=29979.2458082(22)\;\text{V/m}">
- Electric polarization **P**: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}=1\;\text{statC/cm}^2\overset{\frown}=3.33564095107(25){\times}10^{-6}\;\text{C/m}^2">
- Electric displacement field **D**: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}=1\;\text{statC/cm}^2\overset{\frown}=2.65441872871(20){\times}10^{-7}\;\text{C/m}^2"> <sup>[3]</sup>
- Electric displacement flux Φ<sub>D</sub>: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}\overset{\frown}=2.65441872871(20){\times}10^{-11}\;\text{C}"> (1/4*π* to the electric charge conversion)

### Magnetization and H Field

The [Magnetization](https://en.wikipedia.org/wiki/Magnetization) is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\frac{\text{d}\mathbf{m}}{\text{d}V}">

where **m** is the magnetic dipole moment and *V* is the volume.

The magnetization current density (in SI unit) is: <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J_m}^\text{SI}=\nabla\times\mathbf{M^\text{SI}}\quad(3.5\text{a})">

The total current density is:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=\mathbf{J_f}+\mathbf{J_m}+\mathbf{J_p}">

where **J**<sub>**p**</sub> is the polarization current density: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J_p}=\frac{\partial\mathbf{P}}{\partial{t}}">

The [Magnetic H Field](https://en.wikipedia.org/wiki/Magnetic_field#H-field_and_magnetic_materials) (in SI units) is defined as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}^\text{SI}=\frac{\mathbf{B}^\text{SI}}{\mu_0}-\mathbf{M}^\text{SI}\quad(3.6\text{a})">

And apply [Ampère-Maxwell Equation](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_circuital_law#Extending_the_original_law:_the_Amp%C3%A8re%E2%80%93Maxwell_equation) for **B**:

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}^\text{SI}=\mu_0\mathbf{J}^\text{SI}+\frac{1}{c^2}\frac{\partial\mathbf{E}^\text{SI}}{\partial{t}}\quad(3.7\text{a})">

Then we get Ampère-Maxwell equation for **H**: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}^\text{SI}=\mathbf{J_f}^\text{SI}+\frac{\partial\mathbf{D}^\text{SI}}{\partial{t}}\quad(3.8\text{a})">

The above equations in Gaussian units are:

<img src="https://latex.codecogs.com/gif.latex?\begin{array}{ll}\mathbf{J_m}^\text{G}=c\nabla\times\mathbf{M^\text{G}}&(3.5\text{b})\\[1em]\mathbf{B}^\text{G}=\mathbf{H}^\text{G}+4\pi\mathbf{M}^\text{G}&(3.6\text{b})\\[1em]\nabla\times\mathbf{B}^\text{G}=\dfrac{4\pi}c\mathbf{J}^\text{G}+\dfrac{1}c\dfrac{\partial\mathbf{E}^\text{G}}{\partial{t}}&(3.7\text{b})\\[1em]\nabla\times\mathbf{H}^\text{G}=\dfrac{4\pi}c\mathbf{J_f}^\text{G}+\dfrac{1}c\dfrac{\partial\mathbf{D}^\text{G}}{\partial{t}}&(3.8\text{b})\end{array}">

From [(2.4)](cgs.md#2.4), relation between (3.5a) and (3.5b), relation between (3.8a) and (3.8b), and <img src="https://latex.codecogs.com/gif.latex?\mathbf{J}^\text{SI}=\sqrt{4\pi\varepsilon_0}\mathbf{J}^\text{G}">, we get that: 

- Magnetic **B** field: <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=1.00000000027(8){\times}10^{-4}\;\text{T}">
- Magnetization **M**: <img src="https://latex.codecogs.com/gif.latex?1\;\text{erg/G\;cm}^3=1\;\text{statC/cm}^2\overset{\frown}=999.99999973(7)\;\text{A/m}"> <sup>[6]</sup>
- Magnetic **H** field: <img src="https://latex.codecogs.com/gif.latex?1\;\text{Oe}=1\;\text{statC/cm}^2\overset{\frown}=79.577471524(6)\;\text{A/m}"> <sup>[6]</sup>

### Notes

1. These always hold in all unit systems.
2. [Here](https://en.wikipedia.org/wiki/Polarization_density#Gauss's_law_for_the_field_of_P) is the explanation.
3. [Here](uncertainties/displacement.py) is the calculation.
4. Refer to [here](https://en.wikipedia.org/wiki/Magnetization#Magnetization_current).
5. [Here](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_circuital_law#Proof_of_equivalence) is the proof.
6. [Here](uncertainties/magnetization.py) are the calculations.