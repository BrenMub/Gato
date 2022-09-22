%%
%
% El documento suministrado se publicó como $\texttt{.tex}$ con el archivo
% de estilo $\texttt{matlab2latex.tex}$ mediante el comando

%%
%
%   publish('T1_Murillo','format','latex','stylesheet','matlab2latex.tex')

%%
% *Respuesta Corta*

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



%%
%
% </latex>
% 5a) Para el polinomio p(x) = a_nx^n + ... + a_1x + a_0, si se desea conocer p(x_0) es necesario
% efectuar ... y n sumas. 
% </latex>

%%
%
% 5b)
% Para este algoritmo, se deben realizar en una ca iteración una suma y una
% multiplicación, como son n iteraciones, en total se realizan n sumas y n
% multiplicaciones. 

%%
%
% </latex>
% 6)
% El polinomio de Lagrange para $f(x) = x^2 + 3x +1$ es él mismo, pues es un polinomio, de igual forma si se calcula obtenemos: 
% $$ \frac{x-1}{-1} \frac{x-2}{-2}+ 5\frac{x}{1} \frac{x-2}{1-2} + 15 \frac{x}{2} \frac{x-1}{2-1} = x^2 + 3x +1 $$
% </latex>

%%
% *Desarrollo*

%%
%
% 1)
% Al ejecutar el código suministrado, se obtiene para $n=10$ (note que en este caso se
% ejecuta el código)
n = 10;
f = []; g = [];
f(1)=0;
f(2)=1;
for i=2:(n-1)
    f(i+1)=f(i)+f(i-1);
end

g(n)=f(n);
g(n-1)=f(n-1);
for i=(n-1):-1:2
    g(i-1)=g(i+1)-g(i);
end
disp(g(end)) % imprima el ultimo elemento de g (en comentarios, no usar acentos)

%%
% 2a)
% Como la computadora no tiene implementada la división, entonces debemos
% intentar encontrar otra forma de usar Newton. 
% Note que: f'(x) = \frac{-1}{x^2}, entonces podemos escribir Newton como: 
% $$ c_k = c_{k-1} - x^2(\frac{1}{x} -b) $$
% Al simplificar obtenemos: 
% $$ c_k = c_{k-1} + c_{k-1}(1-bc_{k-1}$$
%
% Para verificar las condiciones, suponga que $\lim_{n \to \infty} x_{n-1} = x$
%Note que 
% $$ \lim{n \to \infty} x_n = \lim{n \to \infty} x_{n-1} + x_{n-1} - bx_{n-1}^2$$
% Entonces
% $$ x = x + x -bx^2 $$
% $\Rightarrow x = \frac{1}{b}$
% 
% Como b no es cero, ..., revisar delta

%%
%
% 2b)
%
%   function c1 = myDivision(c0, b)
%   c1 = c0 + c0*(1 -b*c0);
%   while(abs(c1-c0)>=eps)
%   c0 = c1;    
%   c1 = c0 + c0*(1 -b*c0);
%   
%   end
%   end 
%%
%
% 2c)
b = pi; 
c0= linspace(0,1,1e5); %valores que toman los c0

c1 = myDivision(c0, b);

%Valor de convergencia en función de c0

xx = c0;
yy = nan(size(xx));

for i = 1: numel(xx)
    yy(i) = myDivision(xx(i), b);
end

figure 
semilogx(xx,yy, 'MarkerSize', 20)

%Titulo
title('Gráfico 1 :Convergencia en función de c0')

%Nombrar ejes
xlabel('$x_0$ : valores iniciales', 'Interpreter', 'latex')
ylabel('Valores de convergencia', 'Interpreter', 'latex')

% Se debe garantizar...

%%
%
% 2d)

%% 
%
%</latex>
% 3a)
%Note que por conmutatividad del producto se sigue que 
%\begin{align}
%    \prod_{i=1}^{N_c} f(y_i, \theta) &= \prod_{i}^{N_c} \binom{n_i}{y_i} \prod_{i}^{N_c} \theta^{y_i} \prod_{i}^{N_c} (1- \theta)^{n_i - y_i} \\
%    & \prod_{i}^{N_c} \binom{n_i}{y_i} \theta^{H} (1 - \theta)^{M}
%\end{align}

%donde $H = \displaystyle\sum_{i}^{N_c} y_i $ y $M = \displaystyle\sum_{i}^{N_c} n_i - y_i $. 


%Procedemos a calcular $l'(\theta)$ \\
%Note que 
%\begin{align*}
%   l(\theta) = \log(L(y_1, ... , y_N, \theta) = \log\left(\prod_{i=1}^{N_c} f(y_i, \theta)\right)  
%\end{align*}
%Por (1) y (2), se sigue que 
%\begin{align*}
%    \log(L(y_1, ... , y_N, \theta) &= \log \left( \prod_{i}^{N_c} \binom{n_i}{y_i} \theta^{H} (1 - \theta)^{M} \right) \\
%    &= \log\left(\prod_{i}^{N_c} \binom{n_i}{y_i}\right) + H \log(\theta) + M\log( 1-\theta)
%\end{align*}

%Entonces
%\begin{align*}
%    l'(\theta) = \frac{H}{\theta} - \frac{M}{1- \theta}
%\end{align*}
%Al despejar e igualar a 0, obtenemos los puntos críticos de $l(\theta)$
%\begin{align*}
%     l'(\theta) &= \frac{H}{\theta} - \frac{M}{1- \theta} = 0 \\
%     &\Rightarrow \theta = \frac{H}{N}
%\end{align*}

%donde $N = H+ M$. 

%Además, este punto crítico en efecto es el máximo pues $l''(\theta) < 0$ y por el criterio de la segunda derivada podemos asegurar que es el máximo, 
% </latex>

%% 
%
% 3b) 

%Leemos el archivo
T = readtable('data.txt');

%%
%
% 3c) 

%Vectorizamos los datos
m = T.Machos;
h = T.Hembras;

%Procedemos a calcular el valor que maximiza los datos suministrados 

%Cantidad total de machos
suma_m = sum(m);

%Cantidad total de hembras
suma_h = sum(h);

%Valor que maximiza 
maximo = suma_h/(suma_m + suma_h);

%%
%
% 3d)
f = @(x) suma_h/x - suma_m/(1-x);

Secante(f,0.30,0.60)

%%
%
% 5e)



%% 
%
% </latex>
% 4a)
% Por el teorema 2.10 de las notas sabemos que basta con demostrar que una
% función es continua y que el valor absoluto de su derivada se puede
% acotar por una constante menor que 1 para que el proceso de iteración simple converja a su punto fijo. 
% Note que $g(x) = x -(x^2 -3)/2$ es claramente continuo pues es un
% polinomio. 
% Procedemos a analizar la derivada de g
% Note que $|g'(x) |= |1 -x|$, la cual es una función creciente y alcanza
% su máximo en su extremo derecho en el valor de 1, entonces podemos
% asegurar que para todo $x \in (a,b)$ sucede que $|g'(x)| < 1$. 
% </latex>


%%
%
% 4b)

g = @(x) x -(x.^2 -3)./2;
raiz = 1.732050807568877; %Valor de sqrt{3} con 15 decimales

[c, secS] = iterSimple(g, 1.5);

semilogy(1:numel(secS),abs(secS-raiz)/abs(raiz),'.-','MarkerSize',10); 
%plot(xx,yy,'MarkerSize', 10 )

%Titulo
title('Gráfico 2 :Error relativo en función del número de iteraciones')

%Nombrar ejes
xlabel('Cantidad de iteraciones')
ylabel('Error relativo')

% ¿Cuál es la pendiente de la recta en su gráfica? ¿Qué representa dicha
% pendiente?

% Procedemos a calcular la pendiente de la recta...
% 
% La pendiente de la recta representa la velocidad a la que disminuye el
% error, en este caso podemos observar que el error decrece de forma
% lineal. 



%%
%
% 4c)

a = nan(1,79);


for k = 1:79
    a(k) = ( secS(k)*secS(k+2) - (secS(k+1)^2) )\ (secS(k) + secS(k+2) - 2*secS(k+1));
end 

%Graficar:

semilogy(1:numel(a),abs(raiz - a)/abs(raiz),'.-','MarkerSize',10); 

%Titulo
title('Gráfico 3 :Error relativo de $a$ en función del número de iteraciones', 'Interpreter', 'Latex')

%Nombrar ejes
xlabel('Cantidad de iteraciones')
ylabel('Error relativo de a','Interpreter', 'Latex' )


%Explicaaaar


%%
%
% 5a)

load('dataPolin.mat')

size(dataX)
size (dataY)

%%
%
% 5b)
pn = polyfit(dataX, dataY, 10);

% La salida pn se interpreta como los coeficientes de un polinomio de grado
% 10, el cual se ajusta a los datos REVISAAAAAR

%% 
% 
% 5c) 

xx = linspace(-1,1);
yy = polyval(pn, xx);

figure
plot(xx,yy), hold on
plot(dataX,dataY,'.', 'MarkerSize', 15)

%Titulo
title('Gráfico 3 :Polinomio de interpolación')

%Nombrar ejes
ylabel('Polinomio pn')
xlabel('Intervalos') %?????????


%%
%
% 5d)

%Creamos dos vectores que contengan los datos de los nodos 1,5,10
nodos_nuevosX = [dataX(1) dataX(5) dataX(10)];
nodos_nuevosY = [dataY(1) dataY(5) dataY(10)];

pn_nuevo = polyfit(nodos_nuevosX, nodos_nuevosY, 2);
yy_1 = polyval(pn_nuevo, xx);

figure
plot(xx,yy_1), hold on
plot(nodos_nuevosX, nodos_nuevosY,'.', 'MarkerSize', 15)

%Titulo
title('Gráfico 4 :Polinomio de interpolación')

%Nombrar ejes
ylabel('Polinomio pn')
xlabel('Intervalos') %?????????

%Cuál es mejor? FALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

%%
% Para opciones más elaboradas en LaTeX, recomiendo usar la siguiente
% escritura:

%%
%
% <latex>
% Procedemos por inducción sobre el grado de $p$. 
% \begin{align*}
% b_{n+2} &= b_{n+1} = 0,\\
% b_k &= c_k + 2x_0 b_{k+1} - b_{k+2}\quad {\rm para }\ k = n,n-1,\ldots,1
% \end{align*}
% </latex>

%%
%
close all

%%
% *Código de funciones*

%%
% 
%  Se colocan al final las funciones que se llaman en el archivo.
%  Incluirlas acá mismo para que la entrega sea solo un archivo .m
% 

function c1 = myDivision(c0, b)
    c1 = c0 + c0.*(1 -b.*c0);
   
    while(abs(c1-c0)>=eps)
        c0 = c1;    
        c1 = c0 + c0.*(1 -b.*c0);
   
    end
end

function [root,seq] = iterSimple(f,x0)
    Tol = eps;
    iterMax = 80;
    k = 1;
    seq = [x0 f(x0)];
    while(Tol && k<iterMax)
        seq = [seq f(seq(end))];
        k = k+1;
    end
    root = seq(end);
end

function [root,seq] = Secante(f,x0,x1)
  Tol = 1e-8;
  iterMax = 100;
  count = 0;
  f0 = f(x0);
  f1 = f(x1);
  if(abs(f0)<Tol)    
      root = x0; seq = x0;
  elseif(abs(f1)<Tol) 
      root = x1; seq = x1;
  else
      seq = zeros(iterMax,1);
      xNew = x1 - f1*(x1-x0)/(f1-f0);
      fNew = f(xNew);
      seq(count+1) = xNew;
      while(count<iterMax && abs(x1-x0)>Tol)
        count = count + 1;
        x0 = x1;
        x1 = xNew;
        f0 = f1;
        f1 = fNew;
        xNew = x1 - f1*(x1-x0)/(f1-f0);
        fNew = f(xNew);
        seq(count+1) = xNew;
      end
      root = xNew;
      seq = seq(1:count+1);
  end
end