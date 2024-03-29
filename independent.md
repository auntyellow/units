## 5. System-Independent Electromagnetic Equations

### Electric Field, Polarization and Displacement

Let's introduce a constant *ε*<sub>0</sub> and a coefficient *λ* in Coulomb's law and Gauss's law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{{\lambda}q_1q_2}{4\pi\varepsilon_0r^2}">

<a name="5.1"></a><img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho}{\varepsilon_0}\quad(5.1)">

which hold in all unit systems, then we have different *ε*<sub>0</sub> for different unit systems:

- SI units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=8.8541878128(13){\times}10^{-12}\text{F/m}">
- ESU, Gaussian, Heaviside-Lorentz and natural units: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1">
- EMU: <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1/c^2">

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

In linear, homogeneous, isotropic dielectric with instantaneous response to changes in electric field: <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon\mathbf{E}=\varepsilon_r\varepsilon_0\mathbf{E}=(1+\lambda\chi_e)\varepsilon_0\mathbf{E}">

where *ε* is the absolute permittivity, *ε*<sub>r</sub> is the relative permittivity (≥ 1) and *χ*<sub>e</sub> is the electric susceptibility (≥ 0).

Although *χ*<sub>e</sub> is dimensionless, it does not have the same value in different systems, according to its definition: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\varepsilon_0\chi_e\mathbf{E}">

### Magnetic B, M and H Fields

Let's introduce a constant *µ*<sub>0</sub> and a coefficient *α*<sub>L</sub> in Ampère's force law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{\lambda\alpha_L^2\mu_0I_1I_2l}{2{\pi}r}">

which holds in all unit systems, then we have different *µ*<sub>0</sub>:

- SI units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1.25663706212(19){\times}10^{-6}\;\text{N/A}^2{\approx}4\pi{\times}10^{-7}\;\text{N/A}^2">
- ESU: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1/c^2">
- EMU, Gaussian, Heaviside-Lorentz and natural units: <img src="https://latex.codecogs.com/gif.latex?\mu_0=1">

and different *α*<sub>L</sub>:

- SI units, ESU and EMU: *α*<sub>L</sub> = 1
- Gaussian and Heaviside-Lorentz units: *α*<sub>L</sub> = 1/*c*
- natural units: *α*<sub>L</sub> = 1/*c* = 1

According to special relativity, <img src="https://latex.codecogs.com/gif.latex?\alpha_L^2\mu_0{\varepsilon_0}c^2=1">, which also holds in all unit systems.

Note that *α*<sub>L</sub> also exists in Lorentz force, Biot-Savart law, Maxwell-Faraday equation, Ampère-Maxwell equation and the magnetization equation, which also hold in all unit systems:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B})">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\frac{\lambda\alpha_L\mu_0}{4\pi}\int_C\frac{I\text{d}\boldsymbol\ell\times\mathbf{\hat{r}}}{r^2}">

<a name="5.5"></a><img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{E}=-\alpha_L\frac{\partial\mathbf{B}}{\partial{t}}\quad(5.5)">

<a name="5.6"></a><img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\alpha_L\mu_0\left(\lambda\mathbf{J}+\varepsilon_0\frac{\partial\mathbf{E}}{\partial{t}}\right)\quad(5.6)">

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{M}=\alpha_L\mathbf{J_m}\quad(5.7)">

where the magnetization is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\frac{\text{d}\mathbf{m}}{\text{d}V}">

and **J**<sub>**m**</sub> is the magnetization current density and the total current density is: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=\mathbf{J_f}+\mathbf{J_m}+\mathbf{J_p}\quad(5.8)">

and **J**<sub>**p**</sub> is the polarization current density: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{J_p}=\frac{\partial\mathbf{P}}{\partial{t}}\quad(5.9)">

Let's define the magnetic **H** field as:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=\frac{\mathbf{B}}{\mu_0}-\lambda\mathbf{M}\quad(5.10)">

which also holds in all unit systems.

After applying (5.4), (5.6), (5.7), (5.8) and (5.9) on (5.10), we get the macroscopic form of Ampère-Maxwell equation:

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}=\alpha_L\left(\lambda\mathbf{J_f}+\frac{\partial\mathbf{D}}{\partial{t}}\right)">

In diamagnets and paramagnets, the relation between **B** and **H** is usually linear: <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\mu\mathbf{H}=\mu_r\mu_0\mathbf{H}=(1+\chi_m)\mu_0\mathbf{H}">

where *µ* is the absolute permeability, *µ*<sub>r</sub> is the relative permeability and *χ*<sub>m</sub> is the magnetic susceptibility (negative for diamagnets and positive for paramagnets).

Although *χ*<sub>m</sub> is dimensionless, it does not have the same value in different systems, according to its definition: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\chi_m\mathbf{H}">

### Summary

We introduced coefficients *λ* and *α*<sub>L</sub> in different unit systems.

*λ* depends on whether the unit system is rationalized or non-rationalized:

- *λ* = 1 (rationalized) prefers simple forms for Maxwell's equations.
- *λ* = 4*π* (non-rationalized) prefers simple forms for Coulomb's law, Ampère's force law and Biot-Savart law.

*α*<sub>L</sub> depends on the definition of magnetic **B** field:

- *α*<sub>L</sub> = 1 defines **B** by Lorentz force.
- *α*<sub>L</sub> = *c* makes **B** the same dimension as **E**.
- *α*<sub>L</sub> = *c* = 1 takes both above advantages.

|                             |*α*<sub>L</sub> = 1|*α*<sub>L</sub> = *c* = 1|*α*<sub>L</sub> = *c*|
|:----------------------------|:------------------|:------------------------|:--------------------|
|*λ* = 1 (rationalized)       |SI                 |Natural                  |Heaviside-Lorentz    |
|*λ* = 4*π* (non-rationalized)|ESU, EMU           |-                        |Gaussian             |

The differences between ESU and EMU are *ε*<sub>0</sub> and *µ*<sub>0</sub>:

- ESU: *ε*<sub>0</sub> = 1 and *µ*<sub>0</sub> = 1/*c*<sup>2</sup>, prefer simple Coulomb's law.
- EMU: *ε*<sub>0</sub> = 1/*c*<sup>2</sup> and *µ*<sub>0</sub> = 1, prefer simple Ampère's force law and Biot-Savart law.

|System           |*ε*<sub>0</sub>  |*µ*<sub>0</sub>  |*λ* |*α*<sub>L</sub>|*k*<sub>C</sub>  |*k*<sub>A</sub>    |
|:----------------|:----------------|:----------------|:---|:--------------|:----------------|:------------------|
|SI               |8.8541878128(13)×10<sup>-12</sup> F/m <sup>[6]</sup>|1.25663706212(19)×10<sup>-6</sup> N/A<sup>2</sup> <sup>[6]</sup>|1|1|1/4*πε*<sub>0</sub>|*µ*<sub>0</sub>/4*π*|
|ESU              |1                |1/*c*<sup>2</sup>|4*π*|1              |1                |1/c<sup>2</sup>    |
|EMU              |1/*c*<sup>2</sup>|1                |4*π*|1              |1/*c*<sup>2</sup>|1                  |
|Gaussian         |1                |1                |4*π*|*c*            |1                |1/*c*<sup>2</sup>  |
|Heaviside-Lorentz|1                |1                |1   |*c*            |1/4*π*           |1/4*π*c<sup>2</sup>|
|Natural          |1                |1                |1   |*c* = 1        |1/4*π*           |1/4*π*             |

Here *k*<sub>C</sub> is the constant in Coulomb's law: <sup>[7]</sup>

<img src="https://latex.codecogs.com/gif.latex?k_C=\frac{\lambda}{4\pi\varepsilon_0}">

<img src="https://latex.codecogs.com/gif.latex?F=\frac{k_Cq_1q_2}{r^2}">

and *k*<sub>A</sub> is the constant in Ampère's force law and Biot-Savart law: <sup>[8]</sup>

<img src="https://latex.codecogs.com/gif.latex?k_A=\frac{k_C}{c^2}=\frac{\lambda\alpha_L^2\mu_0}{4\pi}">

<img src="https://latex.codecogs.com/gif.latex?F=\frac{k_AI_1I_2l}{2r}">

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\frac{k_A}{\alpha_L}\int_C\frac{I\text{d}\boldsymbol\ell\times\mathbf{\hat{r}}}{r^2}">

where *ε*<sub>0</sub>, *µ*<sub>0</sub> and *α*<sub>L</sub> follow the special relativity:

<img src="https://latex.codecogs.com/gif.latex?\alpha_L^2\mu_0{\varepsilon_0}c^2=1">

The system-independent Maxwell equations are:

<table>
  <tr>
    <td></td>
    <td>microscopic</td>
    <td>macroscopic</td>
  </tr>
  <tr>
    <td>Gauss's law</td>
    <td><img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho}{\varepsilon_0}"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{D}=\lambda\rho_f"></td>
  </tr>
  <tr>
    <td>Gauss's law for magnetism</td>
    <td colspan="2"><img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{B}=0"></td>
  </tr>
  <tr>
    <td> Maxwell-Faraday equation</td>
    <td colspan="2"><img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{E}=-\alpha_L\frac{\partial\mathbf{B}}{\partial{t}}"></td>
  </tr>
  <tr>
    <td>Ampère-Maxwell equation</td>
    <td><img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\alpha_L\mu_0\left(\lambda\mathbf{J}+\varepsilon_0\frac{\partial\mathbf{E}}{\partial{t}}\right)"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{H}=\alpha_L\left(\lambda\mathbf{J_f}+\frac{\partial\mathbf{D}}{\partial{t}}\right)"></td>
  </tr>
</table>

Additional equations are:

<table>
  <tr>
    <td></td>
    <td>charge or electric</td>
    <td>current or magnetic</td>
  </tr>
  <tr>
    <td>total density</td>
    <td><img src="https://latex.codecogs.com/gif.latex?\rho=\rho_f+\rho_b"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{J}=\mathbf{J_f}+\mathbf{J_m}+\mathbf{J_p}"></td>
  </tr>
  <tr>
    <td>polarization and magnetization</td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\frac{\text{d}\mathbf{p}}{\text{d}V}"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\frac{\text{d}\mathbf{m}}{\text{d}V}"></td>
  </tr>
  <tr>
    <td>bound charge and magnetization current</td>
    <td><img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{P}=-\rho_b"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{M}=\alpha_L\mathbf{J_m}"></td>
  </tr>
  <tr>
    <td>displacement field and <b>H</b> field</td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon_0\mathbf{E}+\lambda\mathbf{P}"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{H}=\frac{\mathbf{B}}{\mu_0}-\lambda\mathbf{M}"></td>
  </tr>
  <tr>
    <td>permittivity <sup>[2]</sup> and permeability <sup>[4]</sup></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{D}=\varepsilon\mathbf{E}=\varepsilon_r\varepsilon_0\mathbf{E}=(1+\lambda\chi_e)\varepsilon_0\mathbf{E}"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\mu\mathbf{H}=\mu_r\mu_0\mathbf{H}=(1+\lambda\chi_m)\mu_0\mathbf{H}"></td>
  </tr>
  <tr>
    <td>susceptibility <sup>[2,3,4,5]</sup></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{P}=\varepsilon_0\chi_e\mathbf{E}"></td>
    <td><img src="https://latex.codecogs.com/gif.latex?\mathbf{M}=\chi_m\mathbf{H}"></td>
  </tr>
  <tr>
    <td>polarization current density</td>
    <td colspan="2"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial\mathbf{P}}{\partial{t}}=\mathbf{J_p}"></td>
  </tr>
  <tr>
    <td>continuity equation</td>
    <td colspan="2"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial\rho}{\partial{t}}+\nabla\cdot\mathbf{J}=0"></td>
  </tr>
  <tr>
    <td>Poynting vector <sup>[9]</sup></td>
    <td colspan="2"><img src="https://latex.codecogs.com/gif.latex?\mathbf{S}=\frac{1}{\lambda\alpha_L\mu_0}\mathbf{E}\times\mathbf{B}"></td>
  </tr>
  <tr>
    <td>Lorentz force</td>
    <td colspan="2"><img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B})"> or <img src="https://latex.codecogs.com/gif.latex?\mathbf{f}=\rho\mathbf{E}+\alpha_L\mathbf{J}\times\mathbf{B}"></td>
  </tr>
</table>

### Notes

1. These always hold in all unit systems.
2. In anisotropic dielectric, the permittivity and electric susceptibility are second rank tensors.
3. Refer to [here](https://en.wikipedia.org/wiki/Electric_susceptibility#Ambiguity_in_the_definition) and [here](http://bohr.physics.berkeley.edu/classes/221/1112/notes/emunits.pdf) (30,31).
4. In anisotropic materials, the permeability and magnetic susceptibility are second rank tensors. This does not hold for ferromagnets, ferrimagnets and antiferromagnets.
5. Refer to [here](https://en.wikipedia.org/wiki/Magnetic_susceptibility#In_CGS_units) and [here](http://bohr.physics.berkeley.edu/classes/221/1112/notes/emunits.pdf) (36,37).
6. <img src="https://latex.codecogs.com/gif.latex?\mu_0=2h\alpha/e^2c"> and <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=1/\mu_0c^2">, where *e*, *h* and *c* are exact values by SI definition. Before 2019, <img src="https://latex.codecogs.com/gif.latex?\mu_0=4\pi{\times}10^{-7}\;\text{N/A}^2"> exactly.
7. Coulomb's law is the combination of Gauss's law and Lorentz force.
8. Ampère's force law is the combination of Biot-Savart law and Lorentz force, and Biot-Savart law is the magnetostatic situation of Ampère-Maxwell equation.
9. [Here](poynting.md) is the explanation.