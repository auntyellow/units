## Methodology of Unit Conversion

Let's take [Coulomb's Law](https://en.wikipedia.org/wiki/Coulomb%27s_law) as an example. In SI units:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q_1q_2}{4\pi\varepsilon_0r^2}\quad\text{(Eq.\,1)}">

where <img src="https://latex.codecogs.com/gif.latex?\varepsilon_0=8.854\;187\;8128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2">

In electrostatic or Gaussian units, however, it has a simpler form:

<img src="https://latex.codecogs.com/gif.latex?F=\frac{q_1q_2}{r^2}\quad\text{(Eq.\,2)}">

The unit of electrical charge here is:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{statC}=1\;\text{dyn}^{1/2}\text{cm}\quad\text{(Eq.\,3)}">

To establish the relationship between Eq.1 and Eq.2, we should rewrite them as:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}F=\dfrac{q^\text{SI}_1q^\text{SI}_2}{4\pi\varepsilon_0r^2}&\text{(Eq.\,1')}\\[1em]F=\dfrac{q^\text{G}_1q^\text{G}_2}{r^2}&\text{(Eq.\,2')}\end{cases}">

Let's assume <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=kq^\text{G}">, which means both <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}_1=kq^\text{G}_1"> and <img src="https://latex.codecogs.com/gif.latex?q^\text{SI}_2=kq^\text{G}_2"> hold in Eq. 1' and Eq. 2'. By dividing Eq. 1' and Eq. 2' we get <img src="https://latex.codecogs.com/gif.latex?k=\sqrt{4\pi\varepsilon_0}"> or

<img src="https://latex.codecogs.com/gif.latex?q^\text{SI}=\sqrt{4\pi\varepsilon_0}q^\text{G}\quad\text{(Eq.\,4)}">

Now we have a question: How many **statC** does a **Coulumb** equal (correspond) to?

Let's apply Eq. 4 as:

<img src="https://latex.codecogs.com/gif.latex?1\;\text{C}=\sqrt{4\pi\varepsilon_0}\;x\;\text{statC}\quad\text{(Eq.\,5)}">

Then we have:

<img src="https://latex.codecogs.com/gif.latex?{x=\frac{1\;\text{C}}{\sqrt{4\pi\varepsilon_0}\;\text{statC}}=\frac{1\;\text{C}}{\sqrt{4\pi{\times}8.8541878128(13){\times}10^{-12}\text{C}^2/\text{Nm}^2}\;\text{dyn}^{1/2}\text{cm}}=\dots=2997924580.82(22)}">

Here we use Eq. 3 and the conversions <img src="https://latex.codecogs.com/gif.latex?1\;\text{dyn}=10^{-5}\text{N}"> and <img src="https://latex.codecogs.com/gif.latex?1\;\text{cm}=10^{-2}\text{m}">. <sup>[1]</sup>

We represent Eq. 5 as: <sup>[2,3]</sup>

<img src="https://latex.codecogs.com/gif.latex?1\;\text{C}\overset{\frown}=2997924580.82(22)\;\text{statC}">

### Notes

1. [Here](uncertainties/coulomb.py) is the calculation;
2. This is for electric charge only. For electric flux, Eq. 4 does not work; 
3. Before 2019, <img src="https://latex.codecogs.com/gif.latex?1\;\text{C}\overset{\frown}=2997924580\;\text{statC}"> exactly.