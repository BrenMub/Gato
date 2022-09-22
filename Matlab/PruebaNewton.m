f = @(x) nthroot(x^100,1);
c0 = 2;
tol = 1e-6;
% f crece rápidamente cerca de 2018
% detener iteracion con kmin no es lo mejor

[c1,k1] = newton(f,@df,c0, tol);

disp(f(c1))

c0 + c0.*(-b.*c0 +1)