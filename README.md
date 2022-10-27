# Numerical-methods Labs

## Lab1

1) Применить схему единственного деления метода Гаусса (учитывая контроль!) найти решение $\overline{x^{\star}}$, следующего СЛАУ $A\overline{x}=\overline{f}$
2) Вычислить $\left\| \overline{r} \right\|_{\infty,1,2}=\left\| A\overline{x}^*-\overline{f} \right\|\_{\infty,1,2}$
3) Применяя преобразования метода Гаусса вычислить $detA$
4) Вычислить $\left\| A \right\|_{\infty,1}$

$$(D+KC)*\overline{x}=\overline{f}$$

$$
K=2
$$

$$
D = \begin{bmatrix}
6.22 & 1.42 & -1.72 & 1.91 \\
1.44 & 5.33 & 1.11 & -1.82 \\
-1.72 & 1.11 & 5.24 & 1.42 \\
1.91 & -1.82 & 1.42 & 6.55 \\
\end{bmatrix}
~~
С = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
~~
\overline{f} = \begin{pmatrix}
7.53 & 6.06 & 8.05 & 8.06 \\
\end{pmatrix}^{T}
$$

$$
A = D+KC
$$

## Lab2

1) Применить схему единственного деления метода Гаусса найти $A^{-1}$, где $A$ - матрица из Lab1  
Приверить равенство $AA^{-1}=E$
2) $condA = \left\| A \right\|_{\infty,1}\left\| A^{-1} \right\|\_{\infty,1}$

## Lab3 

Методом квадратных корней найти решение СЛАУ: $A\overline{x}=\overline{f}$

1) Проверить является ли матрици системы $A=A^{T}>0$, если да, то
2) Разложить $A=LL^{T}$
3) $L\overline{y}=\overline{f}$, $L^{T}\overline{x}=\overline{y}$ (применить обратный ход метода Гаусса) - найти $x$
4) Вычислить $\left\| \overline{r} \right\|_{\infty,1,2}=\left\| A\overline{x}^{*} - f \right\|\_{\infty,1,2}$

$$
A = \begin{bmatrix}
3.3 & 1 & 2.1 \\
1 & 3.8 & 2.1 \\
2.1 & 2.1 & 4.4 \\
\end{bmatrix}
~~
\overline{f} = \begin{pmatrix}
2.1 & 1 & 1.1 \\
\end{pmatrix}^{T}
$$

## Lab4 

1) Привести СЛАУ $A\overline{x}=\overline{f}$ к системе с диагональным преобладанием.   
2) Построить сходящийся итерационный процесс и найти с точностью $ε = 0.5 * 10^{-4}$ решение методом Якоби.  
3) Вывести все итерации  $\{\overline{x}^{(n)}\}$ , проверить  $\left\| A\overline{x}^{(n)} - \overline{f} \right\|\_{\infty} <= ε$ .

$$
A = \begin{bmatrix}
2 & 1 & 0.2 \\
0.2 & 5 & 0.72 \\
-1.2 & 3 & 1.7 \\
\end{bmatrix}
~~
\overline{f} = \begin{pmatrix}
-2.9 & -0.7 & -9.86 \\
\end{pmatrix}^{T}
$$

## Lab5 

1) Методом Зейделя найти с точностью $ε = 0.5 * 10^{-4}$  решение СЛАУ из Lab4.   
2) Вывести все итерации  $\{\overline{x}^{(n)}\}$ .  
3) Проверить $\left\| \overline{r} \right\|_{\infty}=\left\| A\overline{x}^{(n)} - \overline{f} \right\|\_{\infty} <= ε$ . 

