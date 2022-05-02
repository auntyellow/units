## CGS Units: ESU, EMU and Gaussian

### Electrostatic Units (ESU)

Electrostatic Units (ESU) start from [Coulomb's Law](https://en.wikipedia.org/wiki/Coulomb%27s_law):

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q^\text{ES}_1q^\text{ES}_2}{r^2}\quad\text{(Eq.\,1)}">

The unit of **electrical charge** in ESU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}=1\;\text{dyn}^{1/2}\text{cm}">

From [here](methodology.md) we know that <img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}\overset{\frown}=3.33564095107(24){\times}10^{-10}\;\text{C}">.

The [Electric Field](https://en.wikipedia.org/wiki/Electric_field#Electrostatics) is defined as: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{E}\equiv\frac{\mathbf{F_{electric}}}q">

So the unit of electric field in ESU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statV/cm}=1\;\text{dyn/statC}=1\;\text{dyn}^{1/2}\text{cm}^{-1}\quad\text{(Eq.\,2)}">

Note that [Ampère's force law](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_force_law) in ESU is:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{2I^\text{ES}_1I^\text{ES}_2l}{c^2r}\quad\text{(Eq.\,3a)}">

which is different from EMU.

### Electromagnetic Units (EMU)

**Electromagnetic Units** (EMU) start from Ampère's force law:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{2I^\text{EM}_1I^\text{EM}_2l}r\quad\text{(Eq.\,3b)}">

The unit of **current** here is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}=1\;\text{dyn}^{1/2}">

Analogously, we know that <img src="https://latex.codecogs.com/gif.latex?1\;\text{abA}\overset{\frown}=9.9999999973(8)\;\text{A}">. <sup>[2]</sup>

The [Magnetic B Field](https://en.wikipedia.org/wiki/Magnetic_field#The_B-field) is defined by [Lorentz Force](https://en.wikipedia.org/wiki/Lorentz_force#Equation_in_cgs_units): <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F_{magnetic}}=q(\mathbf{v}\times\mathbf{B})">

So the unit of magnetic B field in EMU is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{G}=1\;\text{dyn/abA\;cm}=1\;\text{dyn}^{1/2}\text{cm}^{-1}\quad\text{(Eq.\,4)}">

### Gaussian Units

From Eq. 2 and Eq. 4 we get the fact that electric field in ESU and magnetic B field in EMU share the same dimension and unit. This is an advantage of **Gaussian Units**, where only magnetic measurements (B and H fields, magnetization, dipole moment and flux) come from EMU and the others come from ESU.

Just like Eq. 3a, there are many equations containing *c* in Gaussian units, such as Lorentz force:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q^\text{G}(\mathbf{E^\text{G}}+\frac{1}c\mathbf{v}\times\mathbf{B^\text{G}})">

and Biot-Savart law:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}^\text{G}=\frac{1}c\oint\frac{I^\text{G}\times\mathbf{\hat{r}}}{r^2}\operatorname{d}\boldsymbol\ell">

#### Magnetic B Field

The relation between Tesla and Gauss can be found like Eq. 1' and Eq. 2' [here](methodology.md):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{F_{magnetic}}=q^\text{SI}(\mathbf{v}\times\mathbf{B}^\text{SI})&\text{(Eq.\,5)}\\\mathbf{F_{magnetic}}=q^\text{G}(\dfrac{1}c\mathbf{v}\times\mathbf{B^\text{G}})&\text{(Eq.\,6)}\end{cases}">

By dividing them and applying <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=\sqrt{4\pi\varepsilon_0}q^\text{G}"> we get:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}^\text{G}=\sqrt{4\pi\varepsilon_0}\;c\;\mathbf{B}^\text{SI}">

We can solve *x* in <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}=\sqrt{4\pi\varepsilon_0}c\;x\;\text{T}">:

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{G}}{\sqrt{4\pi\varepsilon_0}\;c\;\text{T}}=\frac{1\;\text{dyn}^{1/2}\text{cm}^{-1}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;299792458\;\text{m/s}\;\text{Ns/Cm}}=\dots=1.00000000027(7){\times}10^{-4}}">

So we have: <sup>[4,5]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=1.00000000027(7){\times}10^{-4}\;\text{T}">

### Notes

1. This holds in all unit systems.
2. [Here](uncertainties/ampere.py) is the calculation.
3. This also holds in ESU and SI units, but does not hold in Gaussian units.
4. [Here](uncertainties/gauss.py) is the calculation.
5. Before 2019, <img src="https://latex.codecogs.com/gif.latex?1\;\text{G}\overset{\frown}=1{\times}10^{-4}\;\text{T}"> exactly.