> [!常用Fourier变换]
> 
| 相关函数 | 谱密度 |
| :---: | :---: |
|  $e^{-\alpha\vert\tau\vert}$   |$\frac{2\alpha}{\alpha^2+\omega^2}$|
|$e^{-\alpha\tau^2}$|$\sqrt{\frac{\pi}{\alpha}}e^{-\frac{\omega^2}{4\alpha}}$|
|$e^{-\alpha\vert\tau\vert}\cos\beta\tau$|$a[\frac{1}{(\omega-\beta)^2+\alpha^2}+\frac{1}{(\omega+\beta)^2+\alpha^2}]$|
|$e^{-\alpha\tau^2}\cos{\beta\tau}$|$\frac{1}{2}\sqrt{\frac{\pi}{\alpha}}\left[e^{-\frac{(\omega-\beta)^2}{4\alpha}}+e^{-\frac{(\omega+\beta)^2}{4\alpha}}\right]$|
|$e^{-\alpha\vert\tau\vert}(1+\alpha\vert\tau\vert)$|$\frac{4\alpha^3}{(\omega^2+\alpha^2)^2}$|
|$R_X(\tau)=\begin{cases}1-\vert\tau\vert,&\vert\tau\vert\leq1\\0,&\vert\tau\vert>1\end{cases}$|$\left[ \frac{\sin(\omega/2)}{\omega/2}\right ]^2$|
|$\cos\omega_0\tau$|$\pi[\delta(\omega+\omega_0)+\delta(\omega-\omega_0)]$|
|$\alpha\frac{\sin{\beta\tau}}{\pi\tau}$|$S_X(\omega)=\begin{cases}\alpha,&\vert\omega\vert\leq\beta\\0,&\vert\omega\vert>\beta\end{cases}$|
|$e^{-\alpha\vert\tau\vert}\left[\cos\beta\tau+\frac{\alpha}{\beta}\sin\beta\vert\tau\vert\right]$|$\frac{4\alpha(\alpha^2+\beta^2)}{(\omega^2+\alpha^2-\beta^2)^2+4\alpha^2\beta^2}$|
|$\frac{\sin^2\alpha\tau}{\tau^2}$|$\begin{cases}\pi(\alpha-\frac{\vert\omega\vert}{2}),&\vert\omega\vert\leq2\alpha\\0,&\vert\omega\vert>2\alpha\end{cases}$|
|$\begin{cases}e^{-\beta\tau},&\tau\geq0\\0,&\tau<0\end{cases}$|$\frac{1}{\beta+j\omega}$|

> [!频域卷积定理]
> $$\mathcal{F}[f_1\cdot f_2]=\frac{1}{2\pi}\cdot\mathcal{F}[f_1]*\mathcal{F}[f_2]$$
> 任意信号与冲激信号的卷积公式：
> $$f(t)*\delta(t)=f(t)$$