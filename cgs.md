## 2. CGS Units: ESU, EMU and Gaussian

### Electrostatic Units (ESU)

Electrostatic Units (ESU) come from [Coulomb's Law](https://en.wikipedia.org/wiki/Coulomb%27s_law):

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q^\text{ES}_1q^\text{ES}_2}{r^2}">

The unit of **electrical charge** in ESU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}=1\;\text{dyn}^{1/2}\text{cm}">

From [here](methodology.md) we know that <img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}\overset{\frown}=3.33564095107(25){\times}10^{-10}\;\text{C}">.

#### Basic Electric Quantities

- Electric Current *I*: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statA}=1\;\text{statC\;s}\overset{\frown}=3.33564095107(25){\times}10^{-10}\;\text{A}">
- Electric Potential *φ* or Voltage *V*: <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV}=1\;\text{erg/statC}\overset{\frown}=299.792458082(22)\;\text{V}">
- Resistance *R*: <img src="https://latex.codecogs.com/gif.latex?1\;\text{s/cm}=1\;\text{statV/statA}=1\;\text{erg\;s/statC}^2\overset{\frown}=8.9875517923(13){\times}10^{11}\;\Omega">
- Capacitance *C*: <img src="https://latex.codecogs.com/gif.latex?1\;\text{cm}=1\;\text{statC/statV}=1\;\text{statC}^2/\text{erg}\overset{\frown}=1.11265005545(17){\times}10^{-12}\;\text{F}">
- Inductance *L*: <img src="https://latex.codecogs.com/gif.latex?1\;\text{s}^2/\text{cm}=1\;\text{statV\;s/statA}=1\;\text{erg\;s}^2/{\text{statC}^2\overset{\frown}=8.9875517923(13){\times}10^{11}\;\text{H}">

#### Electric Field

The [Electric Field](https://en.wikipedia.org/wiki/Electric_field#Electrostatics) is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{E}=\frac{\mathbf{F_{electric}}}q">

So the unit of electric field in ESU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}=1\;\text{dyn/statC}=1\;\text{dyn}^{1/2}\text{cm}^{-1}\quad(2.1)">

### Electromagnetic Units (EMU)

**Electromagnetic Units** (EMU) come from [Ampère's Force Law](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_force_law): <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?F=\frac{2I^\text{EM}_1I^\text{EM}_2l}r">

The unit of **current** here is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}=1\;\text{dyn}^{1/2}">

The conversion between Ampere and abA can be derived like (1.1a') and (1.1b') mentioned [here](methodology.md):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}F=\dfrac{\mu_0I^\text{SI}_1I^\text{SI}_2l}{2{\pi}r}\\[1em]F=\dfrac{2I^\text{EM}_1I^\text{EM}_2l}r\end{cases}">

By dividing them we get:

<img src="https://latex.codecogs.com/gif.latex?I^\text{EM}=\sqrt\frac{\mu_0}{4\pi}I^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}=\sqrt\frac{\mu_0}{4\pi}\;x\;\text{A}">: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?{x=\sqrt\frac{4\pi}{\mu_0}\frac{\text{abA}}{\text{A}}=\sqrt\frac{4\pi}{1.25663706212(19){\times}10^{-6}\;\text{N/A}^2}\frac{\text{dyn}^{1/2}}{\text{A}}=\dots=9.9999999973(7)}">

So we have: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}\overset{\frown}=9.9999999973(7)\;\text{A}">

#### Magnetic B Field

The [Magnetic B Field](https://en.wikipedia.org/wiki/Magnetic_field#The_B-field) is defined by [Lorentz Force](https://en.wikipedia.org/wiki/Lorentz_force#Equation_in_cgs_units): <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F_{magnetic}}=q(\mathbf{v}\times\mathbf{B})">

So the unit of magnetic B field in EMU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{G}=\frac{1\;\text{dyn}}{\text{abA\;s\;cm/s}}=1\;\text{dyn}^{1/2}\text{cm}^{-1}\quad(2.2)">

### Gaussian Units

From (2.1) and (2.2) we get the fact that electric field in ESU and magnetic B field in EMU share the same dimension and unit. This is an advantage of **Gaussian Units**, where only magnetic quantities (B and H fields, magnetization, vector potential, flux and dipole moment) come from EMU and the others (including inductance *L*) come from ESU.

There are many equations containing *c* in Gaussian units, such as Lorentz force:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q^\text{G}(\mathbf{E^\text{G}}+\frac{1}c\mathbf{v}\times\mathbf{B^\text{G}})">

and Biot-Savart law:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}^\text{G}=\frac{1}c\int_C\frac{I^\text{G}\text{d}\boldsymbol\ell\times\mathbf{\hat{r}}}{r^2}">

#### Magnetic B Field

The conversion between Tesla and Gauss can be derived from:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{F_{magnetic}}=q^\text{SI}(\mathbf{v}\times\mathbf{B}^\text{SI})&(2.3\text{a})\\\mathbf{F_{magnetic}}=q^\text{G}(\dfrac{1}c\mathbf{v}\times\mathbf{B^\text{G}})&(2.3\text{b})\end{cases}">

By dividing them and applying <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=\sqrt{4\pi\varepsilon_0}q^\text{G}"> we get:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}^\text{G}=\sqrt{4\pi\varepsilon_0}\;c\;\mathbf{B}^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}=\sqrt{4\pi\varepsilon_0}\;c\;x\;\text{T}">: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{G}}{\sqrt{4\pi\varepsilon_0}\;c\;\text{T}}=\frac{1\;\text{dyn}^{1/2}\text{cm}^{-1}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;299792458\;\text{m/s}\;\text{Ns/Cm}}=\dots=1.00000000027(8){\times}10^{-4}}">

So we have: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=1.00000000027(8){\times}10^{-4}\;\text{T}\quad(2.4)">

#### Magnetic Vector Potential

The [Magnetic Vector Potential](https://en.wikipedia.org/wiki/Magnetic_vector_potential) **A** is defined by: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}=\nabla\times\mathbf{A}">

The unit of magnetic vector potential here is G cm or statV s/cm.

From (2.4) we get <img src="https://latex.codecogs.com/gif.latex?1\;\text{G\;cm\;(or\;statV\;s/cm)}\overset{\frown}=1.00000000027(8){\times}10^{-6}\;\text{T\;m\;(or\;V\;s/m)}">.

This conversion can also be derived from the definition along with the electric potential *φ*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{E}^\text{SI}=-\nabla\phi^\text{SI}-\dfrac{\partial\mathbf{A}^\text{SI}}{\partial{t}}\\[1em]\mathbf{E}^\text{G}=-\nabla\phi^\text{G}-\dfrac{1}c\dfrac{\partial\mathbf{A}^\text{G}}{\partial{t}}\end{cases}">

By dividing them and applying <img src="https://latex.codecogs.com/gif.latex?\mathbf{E}^\text{SI}=\frac{1}{\sqrt{4\pi\varepsilon_0}}\mathbf{E}^\text{G}"> we get:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{A}^\text{G}=\sqrt{4\pi\varepsilon_0}\;c\;\mathbf{A}^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{statV\;s/cm}=\sqrt{4\pi\varepsilon_0}\;c\;x\;\text{V\;s/m}">: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{statV\;s/cm}}{\sqrt{4\pi\varepsilon_0}\;c\;\text{V\;s/m}}=\frac{1\;\text{dyn}^{1/2}\text{s/cm}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;299792458\;\text{m/s}\;\text{Ns/C}}=\dots=1.00000000027(8){\times}10^{-6}}">

So we have:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statV\;s/cm}\overset{\frown}=1.00000000027(8){\times}10^{-6}\;\text{V\;s/m}">

#### Magnetic Flux

The [Magnetic Flux](https://en.wikipedia.org/wiki/Magnetic_flux) Φ is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\Phi=\mathbf{B}\cdot\mathbf{S}">

The unit of magnetic flux here is <img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}=1\;\text{G\;cm}^2">.

From (2.4) we get <img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}\overset{\frown}=1.00000000027(8){\times}10^{-8}\;\text{Wb}">.

This conversion can also be derived from [Faraday's Law of Induction](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathcal{E}^\text{SI}=-\dfrac{\text{d}\Phi^\text{SI}}{\text{d}t}\\[1em]\mathcal{E}^\text{G}=-\dfrac{1}c\dfrac{\text{d}\Phi^\text{G}}{\text{d}t}\end{cases}">

By dividing them and applying <img src="https://latex.codecogs.com/gif.latex?\mathcal{E}^\text{SI}=\frac{1}{\sqrt{4\pi\varepsilon_0}}\mathcal{E}^\text{G}"> we get:

<img src="https://latex.codecogs.com/gif.latex?\Phi^\text{G}=\sqrt{4\pi\varepsilon_0}\;c\;\Phi^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}=\sqrt{4\pi\varepsilon_0}\;c\;x\;\text{Wb}">: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{Mx}}{\sqrt{4\pi\varepsilon_0}\;c\;\text{Wb}}=\frac{1\;\text{dyn}^{1/2}\text{cm}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;299792458\;\text{m/s}\;\text{Nm/A}}=\dots=1.00000000027(8){\times}10^{-8}}">

So we have: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}\overset{\frown}=1.00000000027(8){\times}10^{-8}\;\text{Wb}">

#### Magnetic Dipole Moment

The [Magnetic Dipole Moment](https://en.wikipedia.org/wiki/Electric_field#Electrostatics) **m** is defined by: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{\tau}=\mathbf{m}\times\mathbf{B}">

where ***τ*** is the torque acting on the dipole.

The unit of magnetic dipole moment here is erg/G or statC cm.

From (2.4) we get <img src="https://latex.codecogs.com/gif.latex?1\;\text{erg/G}\overset{\frown}=0.99999999973(7){\times}10^{-3}\;\text{J/T}\;(\text{or\;Am}^2)">.

This conversion can also be derived from [Amperian loop model](https://en.wikipedia.org/wiki/Magnetic_moment#Amperian_loop_model):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{m}^\text{SI}=I^\text{SI}\mathbf{S}\\\mathbf{m}^\text{G}=\dfrac{1}cI^\text{G}\mathbf{S}\end{cases}">

By dividing them and applying <img src="https://latex.codecogs.com/gif.latex?I^\text{SI}=\sqrt{4\pi\varepsilon_0}I^\text{G}"> we get:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{m}^\text{G}=\frac{1}{\sqrt{4\pi\varepsilon_0}\;c}\mathbf{m}^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{statC\;cm}=\frac{x}{\sqrt{4\pi\varepsilon_0}c}\text{Am}^2">: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{statC\;cm}\sqrt{4\pi\varepsilon_0}\;c}{\text{Am}^2}=\frac{1\;\text{dyn}^{1/2}\text{cm}^2\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;299792458\;\text{m/s}}{\text{Am}^2}=\dots=0.99999999973(7){\times}10^{-3}">

So we have:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statC\;cm}\overset{\frown}=0.99999999973(7){\times}10^{-3}\;\text{Am}^2">

### Notes

1. These always hold in all unit systems.
2. Ampère's force law in ESU is <img src="https://latex.codecogs.com/gif.latex?F=2I^\text{ES}_1I^\text{ES}_2l/c^2r">.
3. [Here](uncertainties/ampere.py) is the calculation.
3. This also holds in ESU and SI units (2.3a), but does not hold in Gaussian units (2.3b).
4. [Here](uncertainties/gauss.py) are the calculations.
5. Before 2019, <img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}\overset{\frown}=10\;\text{A}">, <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=10^{-4}\;\text{T}"> and <img src="https://latex.codecogs.com/gif.latex?1\;\text{Mx}\overset{\frown}=10^{-8}\;\text{Wb}"> exactly.