Here are steps to calculate:

<img src="https://latex.codecogs.com/gif.latex?F(x)=\int\frac{x^3}{\sqrt{(x^2+y^2)(x^2+(y-d)^2)}^3}\text{d}x">

**Step 1:** Set *X* = *x*<sup>2</sup>, then we get:

<img src="https://latex.codecogs.com/gif.latex?{F(x)=\frac{1}2\int\frac{x^2}{\sqrt{(x^2+y^2)(x^2+(y-d)^2)}^3}\text{d}x^2=\frac{1}2\int\frac{X}{\sqrt{(X+y^2)(X+(y-d)^2)}^3}\text{d}X=\frac{1}2\int\frac{X}{\sqrt{X^2+(y^2+(y-d)^2)X+y^2(y-d)^2}^3}\text{d}X}">

**Step 2:** Set <img src="https://latex.codecogs.com/gif.latex?R=\sqrt{X^2+bX+c}"> where <img src="https://latex.codecogs.com/gif.latex?b=y^2+(y-d)^2"> and <img src="https://latex.codecogs.com/gif.latex?c=y^2(y-d)^2">, then we find:

<img src="https://latex.codecogs.com/gif.latex?\int\frac{X}{R^3}\text{d}X=-\frac{2bX+4c}{(4c-b^2)R}">

from [this](https://en.wikipedia.org/wiki/List_of_integrals_of_irrational_functions#Integrals_involving_R_=_%E2%88%9Aax2_+_bx_+_c) table of integrals.

**Step 3:** Replace *b*, *c*, *R* and *X*:

<img src="https://latex.codecogs.com/gif.latex?F(x)=\int\frac{X}{R^3}\text{d}X=-\frac{bX+2c}{(4c-b^2)R}=-\frac{(y^2+(y-d)^2)x^2+2y^2(y-d)^2}{d^2(2y-d)^2\sqrt{(x^2+y^2)(x^2+(y-d)^2)}}">