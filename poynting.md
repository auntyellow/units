## Poynting Vector: System-Independent Form

### Energy stored in electric and magnetic fields

Let's calculate the electric potential energy by: <sup>[1,2]</sup>

<img src="https://latex.codecogs.com/gif.latex?U_e=\frac{1}2\int\rho{\phi}dV">

Use the trick mentioned [here](https://en.wikipedia.org/wiki/Electric_potential_energy#Energy_stored_in_an_electrostatic_field_distribution_in_vacuum), where electric potential follows: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\phi=\mathbf{E}">

and Gauss's law is: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho}{\varepsilon_0}">

Then we get: <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?u_e=\frac{dU_e}{dV}=\frac{\varepsilon_0}{2\lambda}|\mathbf{E}|^2">

Analogously, the magnetic potential energy is: <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?U_m=\frac{\alpha_L}2\int\mathbf{J}\cdot\mathbf{A}dV">

Apply the magnetic vector potential: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{A}=\mathbf{B}">

and Ampère's circuital law: <sup>[2,3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\lambda\alpha_L\mu_0\mathbf{J}">

then we get: <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?u_e=\frac{dU_m}{dV}=\frac{1}{2\lambda\alpha_L\mu_0}|\mathbf{B}|^2">

### Notes

1. These always hold in all unit systems.
2. These only hold in electrostatic or magnetostatic situation.
3. Refer to (5.1) and (5.5) mentioned [here](independent.md).