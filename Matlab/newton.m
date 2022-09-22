


function [c1,k] = newton(f,df,c0,tol)
    k = 1; %numero de iteraciones
    c1 = c0 - f(c0)/df(c0);
    disp(c1)
    while(abs(c1-c0)>tol)
        c0 = c1;    
        c1 = c0 - f(c0)/df(c0);
        k = k+1;
    end
end


for k = 1:10
    a(k) = ( secS(k)*secS(k+2) - (c(k+1)^2) )\ (c(k) + c(k+2) - 2*c(k+1));
    disp(k)
end 