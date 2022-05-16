## 7. Atomic Units

In [Atomic Units](https://en.wikipedia.org/wiki/Hartree_atomic_units), reduced Planck constant <img src="https://latex.codecogs.com/gif.latex?\hbar">, elementary charge *e*, Coulomb constant 1/4*πε*<sub>0</sub> and electron mass *m*<sub>e</sub> are defined as 1, which make all physical quantities dimensionless.

In computational chemistry, for example, the time-independent Schrödinger equation for a multi-electron atom or ion is:

<img src="https://latex.codecogs.com/gif.latex?{\left\{-\frac{\hbar^2}{2m_e}\sum\limits_{i=1}^N\nabla_i^2-\frac{e^2}{4\pi\varepsilon_0}\left(Z\sum\limits_{i=1}^N\frac{1}{\left|\mathbf{r}_i\right|}-\sum\limits_{i=1}^N\sum\limits_{j=1}^{i-1}\frac{1}{\left|\mathbf{r}_i-\mathbf{r}_j\right|}\right)\right\}\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)=E\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)}">

where *Z* is the nuclear charge number *N* is the number of electrons.

It can be simplified in atomic units as:

<img src="https://latex.codecogs.com/gif.latex?{\left\{-\frac{1}2\sum\limits_{i=1}^N\nabla_i^2-Z\sum\limits_{i=1}^N\frac{1}{\left|\mathbf{r}_i\right|}+\sum\limits_{i=1}^N\sum\limits_{j=1}^{i-1}\frac{1}{\left|\mathbf{r}_i-\mathbf{r}_j\right|}\right\}\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)=E\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)}">

### Uncertainties and Correlation Coefficients

The atomic unit of length is [Bohr radius](https://en.wikipedia.org/wiki/Bohr_radius):

<img src="https://latex.codecogs.com/gif.latex?a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_ee^2}=\frac{\hbar}{c{\alpha}m_e}\quad(7.1)">

where the relative uncertainties of *α* and *m*<sub>0</sub> are 0.15 and 0.30 ppb respectively. However, the relative uncertainty of *a*<sub>0</sub> is 0.15 ppb but not 0.45 ppb. Because *m*<sub>0</sub> is dependent on *α*. <sup>[1]</sup> Actually we have:

<img src="https://latex.codecogs.com/gif.latex?m_e=\frac{2hR_\infty}{c\alpha^2}\quad(7.2)">

where *R*<sub>∞</sub> is the [Rydberg constant](https://en.wikipedia.org/wiki/Rydberg_constant) with the relative uncertainty of 0.0019 ppb. Therefore, we should calculate the uncertainty of Bohr radius by:

<img src="https://latex.codecogs.com/gif.latex?a_0=\frac{\alpha}{4{\pi}R_\infty}\quad(7.3)">

instead of (7.1).

### Mechanical Units

Some conversions of mechanical units are: <sup>[2]</sup>

- angular momentum: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=1.054571817...{\times}10^{-34}\;\text{J\;s}"> (exactly)
- mass: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=9.1093837015(27){\times}10^{-31}\;\text{kg}"> (0.30 ppb, refer to (7.2))
- length: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=5.2917721090(8){\times}10^{-11}\;\text{m}"> (0.15 ppb, refer to (7.3))
- velocity: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=2.18769126364(33){\times}10^{6}\;\text{m/s}"> (0.15 ppb, <img src="https://latex.codecogs.com/gif.latex?e^2/4\pi\varepsilon_0\hbar=c\alpha">)
- time: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=2.418884326586(5){\times}10^{-17}\;\text{s}"> (0.0019 ppb, <img src="https://latex.codecogs.com/gif.latex?a_0/c\alpha=1/4{\pi}cR_\infty">)
- energy: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=4.359744722207(8){\times}10^{-18}\;\text{J}"> (0.0019 ppb, <img src="https://latex.codecogs.com/gif.latex?m_ec^2\alpha^2=4\pi{\hbar}R_\infty">)

### Notes

1. The **Correlation Coefficient** (copy and paste instead of click: https://physics.nist.gov/cgi-bin/cuu/CCValue?me|ShowSecond=&First=alph) between *α* and *m*<sub>0</sub> is close to 1.0.
2. [Here](uncertainties/atomic.py) are the calculations.