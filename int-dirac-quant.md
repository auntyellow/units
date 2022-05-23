Here are the steps to calculate this integral (assume *d* > 0):

<img src="https://latex.codecogs.com/gif.latex?\int_{-\infty}^{+\infty}\int_0^{+\infty}\frac{x^3}{\sqrt{(x^2+y^2)(x^2+(y-d)^2)}^3}\text{d}x\text{d}y">

**Step 1:** Calculate antiderivative about *x*:

<img src="https://latex.codecogs.com/gif.latex?F(x)=\int\frac{x^3}{\sqrt{(x^2+y^2)(x^2+(y-d)^2)}^3}\text{d}x">

Set *X* = *x*<sup>2</sup>, then we get:

<img src="https://latex.codecogs.com/gif.latex?{F(x)=\frac{1}2\int\frac{x^2}{\sqrt{(x^2+y^2)(x^2+(y-d)^2)}^3}\text{d}x^2=\frac{1}2\int\frac{X}{\sqrt{(X+y^2)(X+(y-d)^2)}^3}\text{d}X=\frac{1}2\int\frac{X}{\sqrt{X^2+(y^2+(y-d)^2)X+y^2(y-d)^2}^3}\text{d}X}">

Set <img src="https://latex.codecogs.com/gif.latex?R=\sqrt{X^2+bX+c}"> where <img src="https://latex.codecogs.com/gif.latex?b=y^2+(y-d)^2"> and <img src="https://latex.codecogs.com/gif.latex?c=y^2(y-d)^2">, then we find:

<img src="https://latex.codecogs.com/gif.latex?\int\frac{X}{R^3}\text{d}X=-\frac{2bX+4c}{(4c-b^2)R}">

from [this](https://en.wikipedia.org/wiki/List_of_integrals_of_irrational_functions#Integrals_involving_R_=_%E2%88%9Aax2_+_bx_+_c) table of integrals.

Replace *b*, *c*, *R* and *X*:

<img src="https://latex.codecogs.com/gif.latex?F(x)=\frac{1}2\int\frac{X}{R^3}\text{d}X=-\frac{bX+2c}{(4c-b^2)R}=-\frac{(y^2+(y-d)^2)x^2+2y^2(y-d)^2}{d^2(2y-d)^2\sqrt{(x^2+y^2)(x^2+(y-d)^2)}}">

**Step 2:** Calculate improper integral about *x*:

<img src="https://latex.codecogs.com/gif.latex?{g(y)=\int_0^{+\infty}\frac{x^3}{\sqrt{(x^2+y^2)(x^2+(y-d)^2)}^3}\text{d}x=\lim\limits_{x\rightarrow+\infty}F(x)-F(0)=\frac{y^2+(y-d)^2}{d^2(2y-d)^2}-\frac{2y^2(y-d)^2}{d^2(2y-d)^2|y(y-d)|}=\begin{cases}\dfrac{1}{(2y-d)^2}&(y{\le}0\;\text{or}\;y{\ge}d)\\[1em]\dfrac{1}{d^2}&(0{\le}y{\le}d)\end{cases}}">

**Step 3:** Calculate antiderivative about *y*:

<img src="https://latex.codecogs.com/gif.latex?\begin{cases}G_1(y)=\displaystyle\int\dfrac{1}{(2y-d)^2}\text{d}y=\dfrac{1}{2d-4y}&(y{\le}0\;\text{or}\;y{\ge}d)\\[1em]G_2(y)=\displaystyle\int\dfrac{1}{d^2}\text{d}y=\dfrac{y}{d^2}&(0{\le}y{\le}d)\end{cases}">

**Step 4:** Calculate improper integral about *y*:

<img src="https://latex.codecogs.com/gif.latex?{\int_{-\infty}^{+\infty}g(y)\text{d}y=\left[\lim\limits_{y\rightarrow+\infty}G_1(y)-G_1(d)\right]+\left[G_2(d)-G_2(0)\right]+\left[G_1(0)-\lim\limits_{y\rightarrow-\infty}G_1(y)\right]=\left[0-\left(-\frac{1}{2d}\right)\right]+\left[\frac{1}d-0\right]+\left[\frac{1}{2d}-0\right]=\frac{2}d}">