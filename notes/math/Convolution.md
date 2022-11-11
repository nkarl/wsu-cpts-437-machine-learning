#math-background #convolution 

> [!info] Introduction
> In [mathematics](https://www.wikiwand.com/en/Mathematics "Mathematics") (in particular, [functional analysis](https://www.wikiwand.com/en/Functional_analysis "Functional analysis")), **convolution** is a [mathematical operation](https://www.wikiwand.com/en/Operation_(mathematics) "Operation (mathematics)") on two [functions](https://www.wikiwand.com/en/Function_(mathematics) "Function (mathematics)") (f and g) that produces a third function ($f * g$) that expresses how the shape of one is modified by the other.
>
>  The term _convolution_ refers to both the result function and to the process of computing it. It is defined as the [integral](https://www.wikiwand.com/en/Integral "Integral") of the product of the two functions after one is reflected about the y-axis and shifted.
>
>  **NOTE:** The choice of which function is reflected and shifted before the integral does not change the integral result (see [commutativity](https://www.wikiwand.com/en/Convolution#Properties)). The integral is evaluated for all values of shift, producing the convolution function.


## 1. Definition
---
The [convolution](https://www.wikiwand.com/en/Convolution) of $f$ and $g$ is written $f ∗ g$, denoting the operator with the symbol ∗.

It is defined as *the integral of the product of the two functions **after one is reflected about the y-axis and shifted***. As such, it is a particular kind of [integral transform](https://www.wikiwand.com/en/Integral_transform "Integral transform"):
$$
(f * g)(t) := \int_{-\infty}^{\infty} f(\tau)\cdot g(t-\tau)\cdot d\tau
$$

or (due to commutativity):
$$
(f * g)(t) := \int_{-\infty}^{\infty} f(t-\tau)\cdot g(\tau)\cdot d\tau
$$

where **$\boldsymbol{t}$ is the amount at which the function $\boldsymbol{f(\tau)}$ weighted by the function $\boldsymbol{g(-\tau)}$ is shifted**. As $t$ changes, the weighting function $\boldsymbol{g(t-\tau)}$ *emphasizes different parts of the input function* $\boldsymbol{f(\tau)}$:

- **for** $t > 0$:
	- $\boldsymbol{g(t-\tau)=g(-\tau)}$ that shifts by the amount $t$ along the $\tau$-axis towards $+\infty$
- **for** $t < 0$:
	- $\boldsymbol{g(t-\tau)=g(-\tau)}$ that shifts by the amount $|t|$ along the $\tau$-axis towards $-\infty$


## 2. Visual Interpretation
---
> [!summary] Steps
> 1.  Express each function in terms of a dummy variable $\boldsymbol{\tau}$.
>
> 2.  Reflect one of the functions: $\boldsymbol{g(\tau)\to g(−\tau)}$.
>
> 3.  Add a time-offset t, which allows $\boldsymbol{g(−\tau)}$  to slide along the $\boldsymbol{\tau}$-axis.
> > - If $\boldsymbol{t>0}$ , then $\boldsymbol{g(t−\tau)=g(−\tau)}$ that slides along the $\boldsymbol{\tau}$ -axis toward $+\infty$ by the amount of $t$.
> > - If $\boldsymbol{t<0}$ , then $\boldsymbol{g(t−\tau)=g(−\tau)}$ that slides along the $\boldsymbol{\tau}$ -axis toward $-\infty$ by the amount of $|t|$.
>
> 4. Sub-procedures:
> > - Start t at $-\infty$ and slide it all the way to $+\infty$.
> > - *Wherever the two functions intersect*, find the integral of their product.
> > > - In other words, at time $t$, compute the area under the function $\boldsymbol{f(\tau)}$  weighted by the weighting function $\boldsymbol{g(t−\tau)}$.
	
<div align="center">
	<iframe src="https://upload.wikimedia.org/wikipedia/commons/7/79/Convolution3.svg" style="width:600;height:600"></iframe>
</div>


The resulting [waveform](https://www.wikiwand.com/en/Waveform "Waveform") (not shown here) is the convolution of functions $f$ and $g$. If $f(t)$ is a [unit impulse](https://www.wikiwand.com/en/Unit_impulse "Unit impulse"), the result of this process is simply $g(t)$. Formally:
$$
\begin{flalign}
&\int_{-\infty}^{+\infty} \delta(\tau)\cdot g(t-\tau)\cdot d\tau = g(\tau)
\cr
\cr
&\mbox{where}\quad\delta(\tau):\mbox{the unit impuse/Dirac delta function/$\delta$ distribution}
\end{flalign}
</div>

$$

> [!info] Diract delta function
> the **Dirac delta distribution** (**δ distribution**), also known as the **unit impulse**, is a [generalized function](https://www.wikiwand.com/en/Generalized_function "Generalized function") or [distribution](https://www.wikiwand.com/en/Distribution_(mathematics) "Distribution (mathematics)") over the [real numbers](https://www.wikiwand.com/en/Real_numbers "Real numbers"), whose value is zero everywhere except at zero, and whose [integral](https://www.wikiwand.com/en/Integral "Integral") over the entire real line is equal to one.

