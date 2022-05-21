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

### Poynting's Theorem

Let's focus on the time-varying of the energy density:

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial{u}}{\partial{t}}=\frac{\partial}{2\lambda\partial{t}}\left(\varepsilon_0|\mathbf{E}|^2+\frac{1}{\mu_0}|\mathbf{B}|^2\right)=\frac{\varepsilon_0}{\lambda}\mathbf{E}\cdot\frac{\partial\mathbf{E}}{\partial{t}}+\frac{1}{\lambda\mu_0}\mathbf{B}\cdot\frac{\partial\mathbf{B}}{\partial{t}}">

Apply Ampère-Maxwell equation and Maxwell-Faraday: <sup>[5]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial\mathbf{E}}{\partial{t}}=\frac{1}{\alpha_L\varepsilon_0\mu_0}\nabla\times\mathbf{B}-\frac\lambda{\varepsilon_0}\mathbf{J}">

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial\mathbf{B}}{\partial{t}}=-\frac{1}{\alpha_L}\nabla\times\mathbf{E}">

then we get:

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial{u}}{\partial{t}}=\frac{1}{\lambda\alpha_L\mu_0}\mathbf{E}\cdot\nabla\times\mathbf{B}-\mathbf{E}\cdot\mathbf{J}-\frac{1}{\lambda\alpha_L\mu_0}\mathbf{B}\cdot\nabla\times\mathbf{E}">

Apply the trick: <sup>[6]</sup>

<img src="https://latex.codecogs.com/gif.latex?\mathbf{B}\cdot\nabla\times\mathbf{E}-\mathbf{E}\cdot\nabla\times\mathbf{B}=\nabla\cdot(\mathbf{E}\times\mathbf{B})">

then we get [Poynting's Theorem](https://en.wikipedia.org/wiki/Poynting%27s_theorem): <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?\frac{\partial{u}}{\partial{t}}+\nabla\cdot\mathbf{S}+\mathbf{J}\cdot\mathbf{E}=0">

where **S** is the [Poynting vector](https://en.wikipedia.org/wiki/Poynting_vector) and represents the directional energy flux (the energy transfer per unit area per unit time) or power flow of an electromagnetic field:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{S}=\frac{1}{\lambda\alpha_L\mu_0}\mathbf{E}\times\mathbf{B}">

The momentum density of an electromagnetic field is:

<img src="https://latex.codecogs.com/gif.latex?\mathbf{g}=\frac{1}{c^2}\mathbf{S}=\frac{\alpha_L\varepsilon_0}\lambda\mathbf{E}\times\mathbf{B}">

In all unit systems, the dimension of **S** is *M**T*<sup>-3</sup> and the dimension of **g** is *M**L*<sup>-2</sup>*T*<sup>-1</sup>. In natural units, the dimension of **S** and **g** is 4 (eV<sup>4</sup>).

### Notes

1. These always hold in all unit systems.
2. Refer to [(5.1)](independent.md#5.1) and [(5.6)](independent.md#5.6).
3. These only hold in electrostatic or magnetostatic situation.
4. However, we assume this holds in time-varying fields.
5. Refer to [(5.6)](independent.md#5.6) and [(5.5)](independent.md#5.5).
6. Refer to [the first page in Jackson 1999](diagrams/vector-formulas.png).