## 5. System-Independent Electromagnetic Equations

### Electric Permittivity, Polarization and Displacement

Let's start from the capacitance of an ideal parallel-plate capacitor: <sup>[1,2]</sup>

<img src="https://latex.codecogs.com/gif.latex?C=\frac{{\varepsilon}A}d">

where *A* is the area of one plate, *d* is the distance between the plates, and *ε* is the permittivity of the medium between the two plates.

The permittivity in vacuum is denoted as *ε*<sub>0</sub>. Therefore, the permittivity in linear, homogeneous, isotropic dielectric can be denoted as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\varepsilon=\varepsilon_r\varepsilon_0=(1+\chi_e)\varepsilon_0">

where *ε*<sub>r</sub> is the relative permittivity (≥ 1) and *χ*<sub>e</sub> is the electric susceptibility (≥ 0).

Let's introduce another constant *λ* in Coulomb's law and Gauss's law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{{\lambda}q_1q_2}{4\pi\varepsilon_0r^2}">

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho}{\varepsilon_0}\quad(5.1)">

which hold in all unit systems, then we have different *ε*<sub>0</sub> for different unit systems:

- SI units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=8.8541878128(13){\times}10^{-12}\text{F/m}">
- ESU, Gaussian and Heaviside-Lorentz units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1">
- EMU: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1/c^2">
- natural units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1/c^2=1">

and different *λ*:

- SI, Heaviside-Lorentz and natural units: <img src="https://latex.codecogs.com/gif.latex?\lambda=1">
- ESU, EMU and Gaussian units: <img src="https://latex.codecogs.com/gif.latex?\lambda=4\pi">

The electric polarization is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\frac{\text{d}\mathbf{p}}{\text{d}V}">

and Gauss's law for **P** is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b\quad(5.2)">

where *ρ*<sub>b</sub> is the bound charge density and the total charge density is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\rho=\rho_f+\rho_b\quad(5.3)">

Let's define the electric displacement field as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon_0\mathbf{E}+\lambda\mathbf{P}\quad(5.4)">

which also holds in all unit systems.

After applying (5.1), (5.2) and (5.3) on (5.4), we get the macroscopic form of Gauss's law:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{D}=\lambda\rho_f">

In linear, homogeneous, isotropic dielectric with instantaneous response to changes in electric field: <sup>[1,3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon\mathbf{E}=\varepsilon_r\varepsilon_0\mathbf{E}=(1+\chi_e)\varepsilon_0\mathbf{E}">

### Magnetic B, M and H Fields

Let's introduce two constants *µ*<sub>0</sub> and *α*<sub>L</sub> in Ampère's force law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{\lambda\alpha_L^2\mu_0I_1I_2l}{2{\pi}r}">

which holds in all unit systems, then we have different *µ*<sub>0</sub>:

- SI units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1.25663706212(19){\times}10^{-6}\;\text{N/A}^2{\approx}4\pi{\times}10^{-7}\;\text{N/A}^2">
- ESU: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2">
- EMU, Gaussian and Heaviside-Lorentz units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1">
- natural units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2=1">

and different *α*<sub>L</sub>:

- SI units, ESU and EMU: *α*<sub>L</sub> = 1
- Gaussian and Heaviside-Lorentz units: *α*<sub>L</sub> = 1/*c*
- natural units: *α*<sub>L</sub> = 1/*c* = 1

According to special relativity, <img src="https://latex.codecogs.com/gif.latex?\alpha_L^2\mu_0{\varepsilon_0}c^2=1">, which also holds in all unit systems.

Note that *α*<sub>L</sub> also exists in Lorentz force, Biot-Savart law, Maxwell-Faraday equation, Ampère-Maxwell equation and the magnetization equation, which also hold in all unit systems:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B})">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\frac{\lambda\alpha_L\mu_0}{4\pi}\int_C\frac{I\text{d}\boldsymbol\ell\times\mathbf{\hat{r}}}{r^2}">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{E}=-\alpha_L\frac{\partial\mathbf{B}}{\partial{t}}">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\alpha_L\mu_0\left(\lambda\mathbf{J}+\varepsilon_0\frac{\partial\mathbf{E}}{\partial{t}}\right)\quad(5.5)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{M}=\alpha_L\mathbf{J_m}\quad(5.6)">

where the magnetization is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\frac{\text{d}\mathbf{m}}{\text{d}V}">

and **J**<sub>**m**</sub> is the magnetization current density and the total current density is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=\mathbf{J_f}+\mathbf{J_m}+\mathbf{J_p}\quad(5.7)">

and **J**<sub>**p**</sub> is the polarization current density: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J_p}=\frac{\partial\mathbf{P}}{\partial{t}}\quad(5.8)">

Let's define the magnetic **H** field as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=\frac{\alpha_L^2\mathbf{B}}{\mu_0}-\lambda\mathbf{M}\quad(5.9)">

which also holds in all unit systems.

After applying (5.4), (5.5), (5.6), (5.7) and (5.8) on (5.9), we get the macroscopic form of Ampère-Maxwell equation:

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}=\alpha_L\left(\lambda\mathbf{J_f}+\frac{\partial\mathbf{D}}{\partial{t}}\right)">

In diamagnets and paramagnets, the relation between **B** and **H** is usually linear: <sup>[1,4,5]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\mu\mathbf{H}=\mu_r\mu_0\mathbf{H}=(1+\chi_m)\mu_0\mathbf{H}">

where *µ* is the (absolute) permeability, *µ*<sub>r</sub> is the relative permeability and *χ*<sub>e</sub> is the magnetic susceptibility (negative for diamagnets and positive for paramagnets).

### Summary

We introduced constants *λ* and *α*<sub>L</sub> in different unit systems.

*λ* depends on whether the unit system is rationalized or non-rationalized:

- rationalized unit systems set *λ* = 1, such as SI, Heaviside-Lorentz and natural units, which prefer a clean form for Maxwell's equations.
- nonrationalized unit systems set *λ* = 4*π*, such as ESU, EMU and Gaussian units, which prefer a clean form for Coulomb's law, Ampère's force law and Biot-Savart law.

*α*<sub>L</sub> depends on the definition of magnetic **B** field:

- *α*<sub>L</sub> = 1, such as SI units, ESU and EMU, which defines **B** by Lorentz force.
- *α*<sub>L</sub> = *c*, such as Gaussian and Heaviside-Lorentz units, which makes **B** the same dimension as **E**.
- *α*<sub>L</sub> = *c* = 1, such as natural units, which takes both above advantages.

The differences between ESU and EMU are *ε*<sub>0</sub> and *µ*<sub>0</sub>:

- ESU: *ε*<sub>0</sub> = 1 and *µ*<sub>0</sub> = 1/*c*<sup>2</sup>, prefer Coulomb's law.
- EMU: *ε*<sub>0</sub> = 1/*c*<sup>2</sup> and *µ*<sub>0</sub> = 1, prefer Ampère's force law and Biot-Savart law.

|System           |*ε*<sub>0</sub>  |*µ*<sub>0</sub>  |*λ* |*α*<sub>L</sub>|*k*<sub>C</sub>  |*k*<sub>A</sub>    |
|:----------------|:----------------|:----------------|:---|:--------------|:----------------|:------------------|
|SI               |8.8541878128(13)×10<sup>-12</sup> F/m|1.25663706212(19)×10<sup>-6</sup> N/A<sup>2</sup>|1|1/4*πε*<sub>0</sub>|*µ*<sub>0</sub>/4*π*|
|ESU              |1                |1/*c*<sup>2</sup>|4*π*|1              |1                |1/c<sup>2</sup>    |
|EMU              |1/*c*<sup>2</sup>|1                |4*π*|1              |1/*c*<sup>2</sup>|1                  |
|Gaussian         |1                |1                |4*π*|*c*            |1                |1/*c*<sup>2</sup>  |
|Heaviside-Lorentz|1                |1                |1   |*c*            |1/4*π*           |1/4*π*c<sup>2</sup>|
|Natural          |1                |1                |1   |*c* = 1        |1/4*π*           |1/4*π*             |

Here *k*<sub>C</sub> is the coefficient in Coulomb's law: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?k_C=\frac{\lambda}{4\pi\varepsilon_0}">

<img src="https://latex.codecogs.com/gif.latex?F=\frac{k_Cq_1q_2}{r^2}">

and *k*<sub>A</sub> is the coefficient in Ampère's force law and Biot-Savart law: <sup>[7]</sup>

<img src="https://latex.codecogs.com/gif.latex?k_A=\frac{k_C}{c^2}=\frac{\lambda\alpha_L^2\mu_0}{4\pi}">

<img src="https://latex.codecogs.com/gif.latex?F=\frac{k_AI_1I_2l}{2r}">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\frac{k_A}{\alpha_L}\int_C\frac{I\text{d}\boldsymbol\ell\times\mathbf{\hat{r}}}{r^2}">

where *ε*<sub>0</sub>, *µ*<sub>0</sub> and *α*<sub>L</sub> follow the special relativity:

<img src="https://latex.codecogs.com/gif.latex?\alpha_L^2\mu_0{\varepsilon_0}c^2=1">

The system-independent Maxwell equations are:

- Gauss's law: <img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho}{\varepsilon_0}">
- macroscopic Gauss's law: <img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{D}=\lambda\rho_f">
- Gauss's law for magnetism: <img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{B}=0">
- Maxwell-Faraday equation: <img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{E}=-\alpha_L\frac{\partial\mathbf{B}}{\partial{t}}">
- Ampère-Maxwell equation: <img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\alpha_L\mu_0\left(\lambda\mathbf{J}+\varepsilon_0\frac{\partial\mathbf{E}}{\partial{t}}\right)">
- macroscopic Ampère-Maxwell equation: <img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}=\alpha_L\left(\lambda\mathbf{J_f}+\frac{\partial\mathbf{D}}{\partial{t}}\right)">

Additional equations are:

- total charge density: <img src="https://latex.codecogs.com/gif.latex?\rho=\rho_f+\rho_b">
- electric polarization: <img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b">
- electric displacement field: <img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon_0\mathbf{E}+\lambda\mathbf{P}">
- electric permittivity: <img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon\mathbf{E}=\varepsilon_r\varepsilon_0\mathbf{E}=(1+\chi_e)\varepsilon_0\mathbf{E}">
- total current density: <img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=\mathbf{J_f}+\mathbf{J_m}+\mathbf{J_p}">
- magnetization current density: <img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{M}=\alpha_L\mathbf{J_m}">
- polarization current density: <img src="https://latex.codecogs.com/gif.latex?\mathbf{J_p}=\frac{\partial\mathbf{P}}{\partial{t}}">
- magnetic **H** field: <img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=\frac{\alpha_L^2\mathbf{B}}{\mu_0}-\lambda\mathbf{M}">
- magnetic permeability: <img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\mu\mathbf{H}=\mu_r\mu_0\mathbf{H}=(1+\chi_m)\mu_0\mathbf{H}"> (in diamagnets and paramagnets)
- Lorentz force: <img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B})">

### Notes

1. These always hold in all unit systems.
2. Refer to [here](https://en.wikipedia.org/wiki/Permittivity#Determining_capacitance).
3. In anisotropic dielectric, the permittivity is a second rank tensor.
4. This does not hold for ferromagnets, ferrimagnets and antiferromagnets.
5. We skip discussion of inductance and permeability here because they are more complicated than capacitance and permittivity.
6. Coulomb's law is the combination of Gauss's law and Lorentz force.
7. Ampère's force law is the combination of Biot-Savart law and Lorentz force, and Biot-Savart law is the magnetostatic situation of Ampère-Maxwell equation.