## Introduction to Units, Physical Constants and Uncertainties

Although SI units are preferred in most publications, Gaussian and other units are still widely used in some fields, such as chapter 11-16 in [Jackson 1999](https://en.wikipedia.org/wiki/Classical_Electrodynamics_(book)). One reason is:

> Explicit factors of *c* appear in a natual manner in these units, making them more appropriate than SI units for relativistic phenomena.

Another reason is to make equations simpler, for example:

- Electromagnetic tensor: <img src="https://latex.codecogs.com/gif.latex?F^{\mu\nu}={\begin{bmatrix}0&-E_x&-E_y&-E_z\\E_x&0&-B_z&B_y\\E_y&B_z&0&-B_x\\E_z&-B_y&B_x&0\end{bmatrix}"> (Gaussian, Heaviside-Lorentz, natural)
- Klein-Gordon equation: <img src="https://latex.codecogs.com/gif.latex?\left(\partial_t^2-\nabla^2+m^2\right)\psi(t,\mathbf{x})=0"> (natural)
- Schrödinger equation for hydrogen atom: <img src="https://latex.codecogs.com/gif.latex?\left(-\frac{1}2\nabla^2-\frac{1}r\right)\psi=E\psi">
(atomic)

Conversions between different unit systems can be found in many textbooks (e.g. appendix in Jackson 1999). However, I'd like to provide a more straight-forward method to make the process easy to understand.

The results here may be far from other materials, because the definition of SI units changed in 2019, which made some physical constants have different uncertainties between SI units and other units.

- [x] 1. [Methodology](methodology.md) of Unit Conversion
- [x] 2. [CGS Units](cgs.md): ESU, EMU and Gaussian
- [x] 3. [Polarization and Magnetization](polarization.md)
- [ ] 4. Natural Units
- [ ] 5. Atomic Units

Appendix

- [ ] A. SI and CGS Mechanical Units
- [ ] B. Energy Conversions
- [ ] C. Physical Constants (CODATA 2018)
- [ ] D. Non-SI Physical Units
- [ ] E. Imperial Units