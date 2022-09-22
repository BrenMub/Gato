%%
%
% El documento suministrado se publicó como $\texttt{.tex}$ con el archivo
% de estilo $\texttt{matlab2latex.tex}$ mediante el comando

%%
%
%   publish('prueba','format','latex','stylesheet','matlab2latex.tex')

%%
% *Respuesta Corta*
a(k) = ( secS(k)*secS(k+2) - (secS(k+1)^2) ) / (secS(k) + secS(k+2) - 2*secS(k+1));

%%
%
% 1) Para aproximar numéricamente la solución de la ecuación $|x^2-1|=0$ es
% iteraciones sucesivas pues .... El método de bisección no es factible
% usarlo pues la función no tiene imagánes negativas, el de Newton tampoco
% pues pueden haber problemas con la derivada y el de secante tampoco...
% 

%%
%
% 2) Al usar el método de Newton en la ecuación $x^100 = 0$ se espera que
% este falle, pues $\frac{d(x^100)}{dx} = 100x^99$, es importante notar que
% conforme se efectúe el proceso, como la raíz de esa ecuación es cero, la
% derivada se va a acercar a cero, por lo que se indefiniría. 
% 

%%
%
% 3)
% La multiplicidad f es el orden de la derivada evaluada en la raiz, el
% orden de la primera derivada que se anule MEJORAAAAR
%%
%
% 4)
% No tiene sentido realizar mas de 52 iteraciones pues note que si
% realizamos 52 iteraciones el error estara dado por:
%%
%</latex>
% $$ e_{52} < \frac{1}{2^{53}}\abs(2-1)$$
% %$$\Rightarrow e_{52} < \frac{1}{2^{53}}
%</latex>
%%
% el cual es menor que el epsilon de la maquina en precision doble. 