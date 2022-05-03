## 2. CGS Units: ESU, EMU and Gaussian

### Electrostatic Units (ESU)

Electrostatic Units (ESU) start from [Coulomb's Law](https://en.wikipedia.org/wiki/Coulomb%27s_law):

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q^\text{ES}_1q^\text{ES}_2}{r^2}\quad(2.1)">

The unit of **electrical charge** in ESU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}=1\;\text{dyn}^{1/2}\text{cm}">

From [here](methodology.md) we know that <img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}\overset{\frown}=3.33564095107(24){\times}10^{-10}\;\text{C}">.

The [Electric Field](https://en.wikipedia.org/wiki/Electric_field#Electrostatics) is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{E}\equiv\frac{\mathbf{F_{electric}}}q">

So the unit of electric field in ESU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}=1\;\text{dyn/statC}=1\;\text{dyn}^{1/2}\text{cm}^{-1}\quad(2.2)">

Note that [Ampère's force law](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_force_law) in ESU is:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{2I^\text{ES}_1I^\text{ES}_2l}{c^2r}\quad(2.3a)">

which is different from EMU.

### Electromagnetic Units (EMU)

**Electromagnetic Units** (EMU) start from Ampère's force law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{2I^\text{EM}_1I^\text{EM}_2l}r\quad(2.3b)">

The unit of **current** here is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}=1\;\text{dyn}^{1/2}">

Analogously, we know that: <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}\overset{\frown}=9.9999999973(8)\;\text{A}\quad(2.4)">

The [Magnetic B Field](https://en.wikipedia.org/wiki/Magnetic_field#The_B-field) is defined by [Lorentz Force](https://en.wikipedia.org/wiki/Lorentz_force#Equation_in_cgs_units): <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F_{magnetic}}=q(\mathbf{v}\times\mathbf{B})">

So the unit of magnetic B field in EMU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{G}=\frac{1\;\text{dyn}}{\text{abA\;s\;cm/s}}=1\;\text{dyn}^{1/2}\text{cm}^{-1}\quad(2.5)">

### Gaussian Units

From (2.2) and (2.5) we get the fact that electric field in ESU and magnetic B field in EMU share the same dimension and unit. This is an advantage of **Gaussian Units**, where only magnetic measurements (B and H fields, magnetization, dipole moment and flux) come from EMU and the others (including inductance *L*) come from ESU.

Just like (2.3a), there are many equations containing *c* in Gaussian units, such as Lorentz force:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q^\text{G}(\mathbf{E^\text{G}}+\frac{1}c\mathbf{v}\times\mathbf{B^\text{G}})">

and Biot-Savart law:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}^\text{G}=\frac{1}c\oint\frac{I^\text{G}\times\mathbf{\hat{r}}}{r^2}\text{d}\boldsymbol\ell">

#### Magnetic B Field

The relation between Tesla and Gauss can be found like (1.1') and (1.2) [here](methodology.md):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{F_{magnetic}}=q^\text{SI}(\mathbf{v}\times\mathbf{B}^\text{SI})&(2.6)\\\mathbf{F_{magnetic}}=q^\text{G}(\dfrac{1}c\mathbf{v}\times\mathbf{B^\text{G}})&(2.7)\end{cases}">

By dividing them and applying <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=\sqrt{4\pi\varepsilon_0}q^\text{G}"> we get:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}^\text{G}=\sqrt{4\pi\varepsilon_0}\;c\;\mathbf{B}^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}=\sqrt{4\pi\varepsilon_0}c\;x\;\text{T}">:

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{G}}{\sqrt{4\pi\varepsilon_0}\;c\;\text{T}}=\frac{1\;\text{dyn}^{1/2}\text{cm}^{-1}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;299792458\;\text{m/s}\;\text{Ns/Cm}}=\dots=1.00000000027(7){\times}10^{-4}}">

So we have: <sup>[4,5]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=1.00000000027(7){\times}10^{-4}\;\text{T}\quad(2.8)">

#### Magnetic Dipole Moment

The [Magnetic Dipole Moment](https://en.wikipedia.org/wiki/Electric_field#Electrostatics) ***µ*** is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{\tau}=\boldsymbol{\mu}\times\mathbf{B}">

where ***τ*** is the torque acting on the dipole.

The unit of magnetic dipole moment here is <img src="https://latex.codecogs.com/gif.latex?\text{erg/G}">.

From (2.8) we get <img src="https://latex.codecogs.com/gif.latex?1\;\text{erg/G}\overset{\frown}=0.99999999973(7){\times}10^{-3}\;\text{J/T}">.

According to [Amperian loop model](https://en.wikipedia.org/wiki/Magnetic_moment#Amperian_loop_model): <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{\mu}=I\mathbf{S}">

The other unit is <img src="https://latex.codecogs.com/gif.latex?\text{abA\;cm}^2">. 

From (2.4) we get the same conversion <img src="https://latex.codecogs.com/gif.latex?1\;\text{abA\;cm}^2\overset{\frown}=0.99999999973(7){\times}10^{-3}\;\text{Am}^2">.

#### Magnetic Flux

The [Magnetic Flux] https://en.wikipedia.org/wiki/Magnetic_flux Φ is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\Phi=\mathbf{B}\cdot\mathbf{S}">

The unit of magnetic flux here is <img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}=1\;\text{G\;cm}^2">.

From (2.8) we get <img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}\overset{\frown}=1.00000000027(7){\times}10^{-8}\;\text{Wb}">.

This unit can also be derived from [Faraday's Law of Induction](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction):

<img src="https://latex.codecogs.com/gif.latex?\mathcal{E}^\text{G}=-\frac{\text{d}\Phi^\text{G}}{c\text{d}t}">

### Notes

1. These holds in all unit systems.
2. [Here](uncertainties/ampere.py) is the calculation.
3. This also holds in ESU and SI units (2.6), but does not hold in Gaussian units (2.7).
4. [Here](uncertainties/gauss.py) is the calculation.
5. Before 2019, <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=1{\times}10^{-4}\;\text{T}"> exactly.