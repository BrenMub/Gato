function [ck,kmin] = biseccion1(f,ak,bk,tol)
tol2 = 1e-12;
kmin = ceil(log((bk-ak)/tol)/log(2)-1);
    
for k = 1:kmin
    ck = (ak+bk)/2;
    if(abs(f(ck))<tol2) %%% comentario
        return
    end
    if(f(ck)*f(bk)<0)
        ak=ck; 
    else
        bk=ck;
    end
end
end