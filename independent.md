## 5. System-Independent Electromagnetic Equations

### Electric Permittivity, Polarization and Displacement

Let's start from the capacitance of an ideal parallel-plate capacitor: <sup>[1,2]</sup>

<img src="https://latex.codecogs.com/gif.latex?C=\frac{{\varepsilon}A}d">

where *A* is the area of one plate, *d* is the distance between the plates, and *ε* is the permittivity of the medium between the two plates.

The permittivity in vacuum is denoted as *ε*<sub>0</sub>. Therefore, the permittivity in dielectric can be denoted as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\varepsilon=\varepsilon_0\varepsilon_r">

Note that *ε*<sub>0</sub> also exists in Coulomb's law and Gauss's law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q_1q_2}{4\pi\varepsilon_0r^2}\quad(5.1)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac\rho{\varepsilon_0}\quad(5.2)">

Let's assume that (5.1) and (5.2) hold in all unit systems, then we have different *ε*<sub>0</sub> for different unit systems:

- SI units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=8.8541878128(13){\times}10^{-12}\text{F/m}">
- ESU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1/4\pi">
- EMU: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=c^2/4\pi">
- Lorentz-Heaviside and natural units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1">

The electric polarization **P** is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\frac{\text{d}\mathbf{p}}{\text{d}V}">

and Gauss's law for **P** is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b\quad(5.3)">

where *ρ*<sub>b</sub> is the bound charge density and the total charge density is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\rho=\rho_f+\rho_b\quad(5.4)">

Let's introduce a new equation for electric displacement field:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\lambda(\varepsilon_0\mathbf{E}+\mathbf{P})\quad(5.5)">

Let's assume that (5.5) holds in all unit systems, then we have different *λ*:

- SI, Lorentz-Heaviside and natural units: <img src="https://latex.codecogs.com/gif.latex?\lambda=1">
- ESU, EMU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\lambda=4\pi">

After applying (5.2), (5.3) and (5.4) on (5.5), we get the macroscopic form of Gauss's law:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{D}=\lambda\rho_f">

### Magnetic B, M and H Fields

Analogously, we have *µ*<sub>0</sub> in Ampère's force law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{\mu_0I_1I_2l}{2{\pi}r}\quad(5.6)">

Let's assume that (5.6) holds in all unit systems, then we have different *µ*<sub>0</sub>: <sup>[3]</sup>

- SI units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1.25663706212(19){\times}10^{-6}\;\text{N/A}^2">
- ESU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=4\pi/c^2">
- EMU: <img src="https://latex.codecogs.com/gif.latex?\mu_0=4\pi">
- Lorentz-Heaviside units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2">
- natural units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2=1">

And we have *α*<sub>L</sub> in Lorentz force, Maxwell–Faraday equation and Ampère-Maxwell equation:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B})\quad(5.7)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{E}=-\alpha_L\frac{\partial\mathbf{B}}{\partial{t}}\quad(5.8)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\frac{\mu_0}{\alpha_L}\left(\mathbf{J}+\varepsilon_0\frac{\partial\mathbf{E}}{\partial{t}}\right)\quad(5.9)">

The magnetization is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\frac{\text{d}\mathbf{m}}{\text{d}V}">

Then we found that *α*<sub>L</sub> also exists in the magnetization equation: <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J_m}=\frac{1}{\alpha_L}\nabla\times\mathbf{M}\quad(5.10)">

where **J**<sub>**m**</sub> is the magnetization current density and the total current density is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=\mathbf{J_f}+\mathbf{J_m}+\mathbf{J_p}\quad(5.11)">

where **J**<sub>**p**</sub> is the polarization current density: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J_p}=\frac{\partial\mathbf{P}}{\partial{t}}\quad(5.12)">

Let's assume that (5.7), (5.8), (5.9) and (5.10) hold in all unit systems, then we have different *α*<sub>L</sub>:

- SI units, ESU and EMU: *α*<sub>L</sub> = 1
- Gaussian and Lorentz-Heaviside units: *α*<sub>L</sub> = 1/*c*
- natural units: *α*<sub>L</sub> = 1/*c* = 1

Let's introduce a new equation for magnetic **H** field:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=\lambda\left(\frac{\alpha_L^2\mathbf{B}}{\mu_0}-\mathbf{M}\right)\quad(5.13)">

After applying (5.5), (5.9), (5.10), (5.11) and (5.12) on (5.13), we get the macroscopic form of Ampère-Maxwell equation:

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}=\alpha_L\left(\lambda\mathbf{J_f}+\frac{\partial\mathbf{D}}{\partial{t}}\right)">

### Notes

1. These always hold in all unit systems.
2. Refer to [here](https://en.wikipedia.org/wiki/Permittivity#Determining_capacitance).
3. We skip discussion of inductance and permeability here because they are more complicated than capacitance and permittivity.
4. *α*<sub>L</sub> is always at **B** side. However, here *α*<sub>L</sub> is at **J**<sub>**m**</sub> side because the dimension of magnetic dipole moment **m** is "energy" / "magnetic B field".