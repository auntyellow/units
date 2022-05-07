## 5. Atomic Units

In [Atomic Units](https://en.wikipedia.org/wiki/Hartree_atomic_units), reduced Planck constant <img src="https://latex.codecogs.com/gif.latex?\hbar">, elementary charge *e*, Coulomb constant 1/4*πε*<sub>0</sub> and electron mass *m*<sub>0</sub> are defined as 1, whick make all physical quantities dimensionless.

In computational chemistry, for example, the time-independent Schrödinger equation for a multi-electron atom is:

<img src="https://latex.codecogs.com/gif.latex?{\left\{-\frac{\hbar^2}{2m_e}\sum\limits_{i=1}^N\nabla_i^2-\frac{e^2}{4\pi\varepsilon_0}\left(Z\sum\limits_{i=1}^N\frac{1}{\left|\mathbf{r}_i\right|}-\sum\limits_{i=1}^N\sum\limits_{j=1}^{i-1}\frac{1}{\left|\mathbf{r}_i-\mathbf{r}_j\right|}\right)\right\}\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)=E\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)}">

where *Z* is the nuclear charge number *N* is the number of electrons.

It is simplified in atomic units as:

<img src="https://latex.codecogs.com/gif.latex?{\left\{-\frac{1}2\sum\limits_{i=1}^N\nabla_i^2-Z\sum\limits_{i=1}^N\frac{1}{\left|\mathbf{r}_i\right|}+\sum\limits_{i=1}^N\sum\limits_{j=1}^{i-1}\frac{1}{\left|\mathbf{r}_i-\mathbf{r}_j\right|}\right\}\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)=E\Psi\left(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N\right)}">

Some conversions are: <sup>[1]</sup>

- length: <img src="https://latex.codecogs.com/gif.latex?1\overset{\frown}=5.29177210903(80){\times}10^{-11}\;\text{m}"> (Bohr radius <img src="https://latex.codecogs.com/gif.latex?a_0=\hbar/{\alpha}m_ec">)

### Note

1. [Here](uncertainties/atomic.py) are the calculations.