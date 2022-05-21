## 1. Methodology of Unit Conversion

Let's take [Coulomb's Law](https://en.wikipedia.org/wiki/Coulomb%27s_law) as an example. In SI units:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q_1q_2}{4\pi\varepsilon_0r^2}\quad(1.1\text{a})">

where <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2">

In electrostatic or Gaussian units, however, it has a simpler form:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q_1q_2}{r^2}\quad(1.1\text{b})">

The unit of electrical charge here is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}=1\;\text{dyn}^{1/2}\text{cm}\quad(1.2)">

To establish the relation between (1.1a) and (1.1b), we should rewrite them as:

<a name="1.1'"></a><img src="https://latex.codecogs.com/gif.latex?\begin{cases}F=\dfrac{q^\text{SI}_1q^\text{SI}_2}{4\pi\varepsilon_0r^2}&(1.1\text{a}')\\[1em]F=\dfrac{q^\text{G}_1q^\text{G}_2}{r^2}&(1.1\text{b}')\end{cases}">

Let's assume <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=kq^\text{G}">, which means both <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}_1=kq^\text{G}_1"> and <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}_2=kq^\text{G}_2"> hold in (1.1a') and (1.1b'). By dividing them we get <img src="https://latex.codecogs.com/gif.latex?k=\sqrt{4\pi\varepsilon_0}"> or

<img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=\sqrt{4\pi\varepsilon_0}q^\text{G}\quad(1.3)">

Now we have a question: How many **statC** does a **coulomb** equal (correspond) to?

Let's apply (1.3) as:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{C}=\sqrt{4\pi\varepsilon_0}\;x\;\text{statC}\quad(1.4)">

Then we have: <sup>[1]</sup>

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{C}}{\sqrt{4\pi\varepsilon_0}\;\text{statC}}=\frac{1\;\text{C}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;\text{dyn}^{1/2}\text{cm}}=\dots=2997924580.82(22)}">

Here we use (1.2) and the conversions <img src="https://latex.codecogs.com/gif.latex?1\;\text{dyn}=10^{-5}\text{N}"> and <img src="https://latex.codecogs.com/gif.latex?1\;\text{cm}=10^{-2}\text{m}">.

We represent (1.4) as: <sup>[2,3]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{C}\overset{\frown}=2997924580.82(22)\;\text{statC}">

### Notes

1. [Here](uncertainties/coulomb.py) is the calculation.
2. This is for electric charge only. For electric displacement flux, (1.3) does not work. 
3. Before 2019, <img src="https://latex.codecogs.com/gif.latex?1\;\text{C}\overset{\frown}=2997924580\;\text{statC}"> exactly.