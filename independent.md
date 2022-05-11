## 5. System-Independent Electromagnetic Equations

### Electric Permittivity, Polarization and Displacement

Let's start from the capacitance of an ideal parallel-plate capacitor: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?C=\frac{{\varepsilon}A}d\quad(5.1)">

where *A* is the area of one plate, *d* is the distance between the plates, and *ε* is the permittivity of the medium between the two plates.

The permittivity is denoted as *ε*<sub>0</sub>. Therefore, the permittivity in dielectric can be denoted as:

<img src="https://latex.codecogs.com/gif.latex?\varepsilon=\varepsilon_0\varepsilon_r\quad(5.2)">

Note that *ε*<sub>0</sub> also exists in Coulomb's law and Gauss's law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q_1q_2}{4\pi\varepsilon_0r^2}\quad(5.3)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac\rho{\varepsilon_0}\quad(5.4)">

Let's assume that (5.1), (5.2), (5.3) and (5.4) hold in all unit systems, then we have different *ε*<sub>0</sub> for different unit systems:

- SI units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=8.8541878128(13){\times}10^{-12}\text{F/m}">
- ESU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1/4\pi">
- EMU: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=c^2/4\pi">
- Lorentz-Heaviside and natural units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1">

Let's introduce a new equation for electric displacement field:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\lambda(\varepsilon_0\mathbf{E}+\mathbf{P})\quad(5.5)">

where the electric polarization **P** is still defined as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\frac{\text{d}\mathbf{p}}{\text{d}V}\quad(5.6)">

and Gauss's law for **P** is still:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b\quad(5.7)">

Let's assume that (5.5), (5.6) and (5.7) still hold in all unit systems, then we have different *λ*:

- SI, Lorentz-Heaviside and natural units: <img src="https://latex.codecogs.com/gif.latex?\lambda=1">
- ESU, EMU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\lambda=4\pi">

### Magnetic B, M and H Fields

Analogously, we have *µ*<sub>0</sub> in Ampère's force law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{\mu_0I_1I_2l}{2{\pi}r}\quad(5.8)">

Let's assume that (5.8), (5.9) and (5.10) holds in all unit systems, then we have different *µ*<sub>0</sub>: <sup>[2]</sup>

- SI units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1.25663706212(19){\times}10^{-6}\;\text{N/A}^2">
- ESU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=4\pi/c^2">
- EMU: <img src="https://latex.codecogs.com/gif.latex?\mu_0=4\pi">
- Lorentz-Heaviside units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2">
- natural units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2=1">

And we have *α*<sub>L</sub> in Lorentz force and Ampère-Maxwell equation:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B})\quad(5.9)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\frac{1}{\alpha_L}\left(\mu_0\mathbf{J}+\frac{1}{c^2}\frac{\partial\mathbf{E}}{\partial{t}}\right)\quad(5.10)">

Let's assume that (5.9) and (5.10) holds in all unit systems, then we have different *α*<sub>L</sub>:

- SI units, ESU and EMU: *α*<sub>L</sub> = 1
- Gaussian and Lorentz-Heaviside units: *α*<sub>L</sub> = 1/*c*
- natural units: *α*<sub>L</sub> = 1/*c* = 1

And we have *α*<sub>H</sub> in magnetic H field:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=\lambda\left(\frac{\alpha_H\mathbf{B}}{\mu_0}-\mathbf{M}\right)\quad(5.11)">

Let's assume that (5.11) holds in all unit systems, then we have different *α*<sub>H</sub>:

- SI and natural units: *α*<sub>H</sub> = 1
- ESU, EMU, Gaussian and Lorentz-Heaviside units: *α*<sub>H</sub> = 1/*c*<sup>2</sup>

Finally we get the Ampère-Maxwell equation for H?

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}=\dfrac{4\pi}c\mathbf{J_f}+\dfrac{1}c\dfrac{\partial\mathbf{D}}{\partial{t}}\quad(5.20)">

### Notes

1. Refer to [here](https://en.wikipedia.org/wiki/Permittivity#Determining_capacitance).
2. We skip discussion of inductance and permeability here because they are more complicated than capacitance and permittivity.