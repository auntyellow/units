## 6. Magnetic Monopole

In this page, we use the [System-Independent Electromagnetic Equations](independent.md); electric charge, charge density and current density are denoted as *q*<sub>e</sub>, *ρ*<sub>e</sub> and **J**<sub>e</sub>; magnetic charge, charge density and current density are denoted as *q*<sub>m</sub>, *ρ*<sub>m</sub> and **J**<sub>m</sub>.

### Duality transformation

The Maxwell's equations and Lorentz force with magnetic monopoles can be derived by [Duality Transformation](https://en.wikipedia.org/wiki/Magnetic_monopole#Duality_transformation) with an angle of 90°:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{E}=\alpha_Lc\mathbf{B'}\\[1em]\mathbf{B}=-\dfrac{\mathbf{E'}}{\alpha_Lc}\end{cases}\quad(6.1)">

Note that the coefficient *α*<sub>L</sub>*c* makes **B** the same dimension as **E**.

Now let's introduce a new coefficient *α*<sub>M</sub> into Gauss's law for magnetism:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{B}=\lambda\alpha_M\rho_m\quad(6.2)">

which can be derived by (6.1) and Gauss's law for electric charge:

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho_e}{\varepsilon_0}\quad(6.3)">

Therefore, the transformation between electric and magnetic charge densities should be:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\rho_e=\alpha_M\alpha_L\varepsilon_0c\;\rho_m'\\[1em]\rho_m=-\dfrac{\rho_e'}{\alpha_M\alpha_L\varepsilon_0c}\end{cases}\quad(6.4)">

Analogously, we have the transformation between electric and magnetic current densities:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{J_e}=\alpha_M\alpha_L\varepsilon_0c\;\mathbf{J_m'}\\[1em]\mathbf{J_m}=-\dfrac{\mathbf{J_e'}}{\alpha_M\alpha_L\varepsilon_0c}\end{cases}\quad(6.5)">

By applying (6.1) and (6.5) on Ampère-Maxwell equation:

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\alpha_L\mu_0\left(\lambda\mathbf{J_e}+\varepsilon_0\frac{\partial\mathbf{E}}{\partial{t}}\right)\quad(6.6)">

we get the Maxwell-Faraday equation with magnetic current density: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{E}=-\alpha_L\left(\lambda\alpha_M\mathbf{J_m}+\frac{\partial\mathbf{B}}{\partial{t}}\right)\quad(6.7)">

We also have the transformation between electric and magnetic charges:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}q_e=\alpha_M\alpha_L\varepsilon_0c\;q_m'\\[1em]q_m=-\dfrac{q_e'}{\alpha_M\alpha_L\varepsilon_0c}\end{cases}\quad(6.8)">

By applying (6.1) and (6.8) on Lorentz force:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F_e}=q_e\left(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B}\right)\quad(6.9)">

we get the Lorentz force for magnetism: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F_m}=\alpha_Mq_m\left(\frac{\mathbf{B}}{\mu_0}-\alpha_L\varepsilon_0\mathbf{v}\times\mathbf{E}\right)\quad(6.10)">

Let's combine (6.9) and (6.10) into one equation:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=q_e\left(\mathbf{E}+\alpha_L\mathbf{v}\times\mathbf{B}\right)+\alpha_Mq_m\left(\frac{\mathbf{B}}{\mu_0}-\alpha_L\varepsilon_0\mathbf{v}\times\mathbf{E}\right)\quad(6.11)">

### In Different Unit Systems

The dimension and unit of magnetic charge *q*<sub>m</sub> can be defined arbitrary, because *α*<sub>M</sub> can be given arbitrary dimension and value. However, we should set proper *α*<sub>M</sub> to make equations simple in different unit systems.

#### Gaussian and Natural Units

In Gaussian and natural units where **B** has the same dimension as **E**, we can just set *α*<sub>M</sub> = 1 to make *q*<sub>m</sub> the same dimension as *q*<sub>e</sub>.

In Gaussian units:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\nabla\cdot\mathbf{E}=4\pi\rho_e&(6.3\text{g})\\[1em]\nabla\cdot\mathbf{B}=4\pi\rho_m&(6.2\text{g})\\[1em]\nabla\times\mathbf{E}=-\dfrac{1}c\left(4\pi\mathbf{J_m}+\dfrac{\partial\mathbf{B}}{\partial{t}}\right)&(6.7\text{g})\\[1em]\nabla\times\mathbf{B}=\dfrac{1}c\left(4\pi\mathbf{J_e}+\dfrac{\partial\mathbf{E}}{\partial{t}}\right)&(6.6\text{g})\\[1em]\mathbf{F}=q_e\left(\mathbf{E}+\dfrac{\mathbf{v}}c\times\mathbf{B}\right)+q_m\left(\mathbf{B}-\dfrac{\mathbf{v}}c\times\mathbf{E}\right)&(6.11\text{g})\end{cases}">

In natural units:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\nabla\cdot\mathbf{E}=\rho_e&(6.3\text{n})\\[1em]\nabla\cdot\mathbf{B}=\rho_m&(6.2\text{n})\\[1em]\nabla\times\mathbf{E}=-\mathbf{J_m}-\dfrac{\partial\mathbf{B}}{\partial{t}}&(6.7\text{n})\\[1em]\nabla\times\mathbf{B}=\mathbf{J_e}+\dfrac{\partial\mathbf{E}}{\partial{t}}&(6.6\text{n})\\[1em]\mathbf{F}=q_e\left(\mathbf{E}+\mathbf{v}\times\mathbf{B}\right)+q_m\left(\mathbf{B}-\mathbf{v}\times\mathbf{E}\right)&(6.11\text{n})\end{cases}">

#### SI Units

In SI units, there are some conventions for *α*<sub>M</sub>:

- *α*<sub>M</sub> = 1 makes Gauss's law for magnetism and Maxwell-Faraday equation simple, where the unit of the magnetic charge is **weber**;
- *α*<sub>M</sub> = *µ*<sub>0</sub> makes Lorentz force simple, where the unit of magnetic charge is **ampere-metre**;
- *α*<sub>M</sub> = *µ*<sub>0</sub>*c* makes magnetic charge the same dimension as electric charge, where the unit of magnetic charge is **coulomb**.

Weber convention:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\nabla\cdot\mathbf{E}=\dfrac{\rho_e}{\varepsilon_0}&(6.3\text{w})\\[1em]\nabla\cdot\mathbf{B}=\rho_m&(6.2\text{w})\\[1em]\nabla\times\mathbf{E}=-\mathbf{J_m}-\dfrac{\partial\mathbf{B}}{\partial{t}}&(6.7\text{w})\\[1em]\nabla\times\mathbf{B}=\mu_0\mathbf{J_e}+\mu_0\varepsilon_0\dfrac{\partial\mathbf{E}}{\partial{t}}&(6.6\text{w})\\[1em]\mathbf{F}=q_e\left(\mathbf{E}+\mathbf{v}\times\mathbf{B}\right)+q_m\left(\dfrac{\mathbf{B}}{\mu_0}-\varepsilon_0\mathbf{v}\times\mathbf{E}\right)&(6.11\text{w})\end{cases}">

Ampere-metre convention:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\nabla\cdot\mathbf{E}=\dfrac{\rho_e}{\varepsilon_0}&(6.3\text{a})\\[1em]\nabla\cdot\mathbf{B}=\mu_0\rho_m&(6.2\text{a})\\[1em]\nabla\times\mathbf{E}=-\mu_0\mathbf{J_m}-\dfrac{\partial\mathbf{B}}{\partial{t}}&(6.7\text{a})\\[1em]\nabla\times\mathbf{B}=\mu_0\mathbf{J_e}+\mu_0\varepsilon_0\dfrac{\partial\mathbf{E}}{\partial{t}}&(6.6\text{a})\\[1em]\mathbf{F}=q_e\left(\mathbf{E}+\mathbf{v}\times\mathbf{B}\right)+q_m\left(\mathbf{B}-\dfrac{1}{c^2}\mathbf{v}\times\mathbf{E}\right)&(6.11\text{a})\end{cases}">

Coulomb convention:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\nabla\cdot\mathbf{E}=\dfrac{\rho_e}{\varepsilon_0}&(6.3\text{c})\\[1em]\nabla\cdot\mathbf{B}=\mu_0c\rho_m&(6.2\text{c})\\[1em]\nabla\times\mathbf{E}=-\mu_0c\mathbf{J_m}-\dfrac{\partial\mathbf{B}}{\partial{t}}&(6.7\text{c})\\[1em]\nabla\times\mathbf{B}=\mu_0\mathbf{J_e}+\mu_0\varepsilon_0\dfrac{\partial\mathbf{E}}{\partial{t}}&(6.6\text{c})\\[1em]\mathbf{F}=q_e\left(\mathbf{E}+\mathbf{v}\times\mathbf{B}\right)+q_m\left(c\mathbf{B}-\dfrac{1}c\mathbf{v}\times\mathbf{E}\right)&(6.11\text{c})\end{cases}">

#### Conversions

The conversions between above 5 units of magnetic charge can be derived by comparing 5 unit systems or conventions of the **B** terms in (6.10):

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\mathbf{F}=q_m^\text{G}\mathbf{B}^\text{G}&(6.10\text{g})\\[1em]\mathbf{F}^\text{N}=q_m^\text{N}\mathbf{B}^\text{N}&(6.10\text{n})\\[1em]\mathbf{F}=\dfrac{q_m^\text{W}}{\mu_0}\mathbf{B}^\text{SI}&(6.10\text{w})\\[1em]\mathbf{F}=q_m^\text{A}\mathbf{B}^\text{SI}&(6.10\text{a})\\[1em]\mathbf{F}=cq_m^\text{C}\mathbf{B}^\text{SI}&(6.10\text{c})\end{cases}">

By applying <img src="https://latex.codecogs.com/gif.latex?\mathbf{F}=\mathbf{F}^\text{N}/{\hbar}c"> and <img src="https://latex.codecogs.com/gif.latex?{\hbar}c\sqrt{{\hbar}c/4\pi}\;\mathbf{B}^\text{G}=\mathbf{B}^\text{N}={\hbar}c^2e/\sqrt{4\pi\alpha}\;\mathbf{B}^\text{SI}"> <sup>[2]</sup> on the above equations, we get: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}\sqrt{\dfrac{4\pi}{{\hbar}c}}\;q_m^\text{G}=q_m^\text{N}=\dfrac{e}{\sqrt{4\pi\alpha}\hbar}\;q_m^\text{W}&(6.12)\\[1em]\dfrac{e}{\sqrt{4\pi\alpha}}\;q_m^\text{N}=\dfrac{1}c\;q_m^\text{A}=q_m^\text{C}&(6.13)\end{cases}">

Note that *α* has the relative uncertainty of 0.15 ppb, so the uncertainties of the above conversions follow this diagram:

<img src="diagrams/magnetic-charge.png">

Finally, we get the unit conversions: <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}1\;\text{n.u.}\overset{\frown}=1.586147240...{\times}10^{-9}\;\text{statC}\overset{\frown}=1.99321140787(15){\times}10^{-16}\;\text{Wb}&(6.12')\\[1em]1\;\text{C}\overset{\frown}=2.99792458{\times}10^8\;\text{A\;m}\overset{\frown}=1.89006701537(14){\times}10^{18}\;\text{n.u.}&(6.13')\end{cases}">

### Elementary Magnetic Charge

The [Dirac's Quantization](https://en.wikipedia.org/wiki/Magnetic_monopole#Dirac's_quantization) condition can be expressed as: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?\lambda\alpha_M\alpha_Lq_eq_m=nh">

Then the elementary magnetic charge *g* can be expressed as:

<img src="https://latex.codecogs.com/gif.latex?g=\frac{nh}{\lambda\alpha_M\alpha_Le}\quad(6.14)">

In different unit systems or conventions: <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}g^\text{G}=\dfrac{nhc}{4{\pi}e^\text{G}}=n\;3.29105978385(25){\times}10^{-8}\;\text{statC}&(6.14\text{g})\\[1em]g^\text{N}=\dfrac{2{\pi}n}{e^\text{N}}=n\;20.7487659392(16)\;\text{n.u.}&(6.14\text{n})\\[1em]g^\text{W}=\dfrac{nh}{e^\text{SI}}=n\;4.135667696...{\times}10^{-15}\;\text{Wb}&(6.14\text{w})\\[1em]g^\text{A}=\dfrac{nh}{\mu_0e^\text{SI}}=n\;3.2910597830(5){\times}10^{-9}\;\text{A\;m}&(6.14\text{a})\\[1em]g^\text{C}=\dfrac{nh}{\mu_0ce^\text{SI}}=n\;1.09777937874(16){\times}10^{-17}\;\text{C}&(6.14\text{c})\end{cases}">

In Gaussian (6.14g), natural (6.14n) units and coulomb (6.14c) convention:

<img src="https://latex.codecogs.com/gif.latex?g=\frac{n}{2\alpha}e">

### Notes

1. Here we use the special relativity relation <img src="https://latex.codecogs.com/gif.latex?\alpha_L^2\mu_0{\varepsilon_0}c^2=1"> in addition.
2. [Here](b-field.md) is the explanation.
3. [Here](relations/b-field.py) are the calculations.
4. [Here](uncertainties/magnetic-charge.py) are the calculations.
5. [Here](dirac-quant.md) is the explanation.