## Poynting Vector: System-Independent Form

### Energy Density in Electromagnetic Field

Let's calculate the electric potential energy by: <sup>[1,3]</sup>

<img src="https://latex.codecogs.com/gif.latex?U_e=\frac{1}2\int\rho{\phi}dV">

Use [this trick](https://en.wikipedia.org/wiki/Electric_potential_energy#Energy_stored_in_an_electrostatic_field_distribution_in_vacuum), where electric potential follows: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\phi=\mathbf{E}">

and Gauss's law is: <sup>[2]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\cdot\mathbf{E}=\frac{\lambda\rho}{\varepsilon_0}">

Then we get: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?u_e=\frac{dU_e}{dV}=\frac{\varepsilon_0}{2\lambda}|\mathbf{E}|^2">

Analogously, the magnetic potential energy is: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?U_m=\frac{\alpha_L}2\int\mathbf{J}\cdot\mathbf{A}dV">

Apply the magnetic vector potential: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{A}=\mathbf{B}">

and Ampère's circuital law: <sup>[2,3]</sup>

<img src="https://latex.codecogs.com/gif.latex?\nabla\times\mathbf{B}=\lambda\alpha_L\mu_0\mathbf{J}">

then we get: <sup>[3]</sup>

<img src="https://latex.codecogs.com/gif.latex?u_m=\frac{dU_m}{dV}=\frac{1}{2\lambda\mu_0}|\mathbf{B}|^2">

Finally, we get the energy density in electromagnetic field: <sup>[4]</sup>

<img src="https://latex.codecogs.com/gif.latex?u=\frac{1}{2\lambda}\left(\varepsilon_0|\mathbf{E}|^2+\frac{1}{\mu_0}|\mathbf{B}|^2\right)">

### Notes

1. These always hold in all unit systems.
2. Refer to [(5.1)](independent.md#5.1) and [(5.5)](independent.md#5.5).
3. These only hold in electrostatic or magnetostatic situation.
4. However, we assume this holds in time-varying fields.