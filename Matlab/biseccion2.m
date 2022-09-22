function [ck,k] = biseccion2(f,ak,bk,tol)
%minIter = ceil(log((bk-ak)/tol)/log(2)-1);
%for j = 1:minIter
k = 1;
ck = (ak+bk)/2;
while(abs(f(ck))>tol)
    if(f(ck)*f(bk)<0)
        ak = ck;% bk = bk;
    else
        bk = ck; %ak = ak;
    end
    ck = (ak+bk)/2;
    k = k + 1;
end
end
