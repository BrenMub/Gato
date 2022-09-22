function [ck,k] = biseccion3(f,ak,bk,tol)
%minIter = ceil(log((bk-ak)/tol)/log(2)-1);
%for j = 1:minIter
k = 1;
ck = (ak+bk)/2;
minIter = ceil(log((bk-ak)/tol)/log(2)-1);
while(abs(f(ck))>tol || k<minIter)
    if(f(ck)*f(bk)<0)
        ak = ck;% bk = bk;
    else
        bk = ck; %ak = ak;
    end
    ck = (ak+bk)/2;
    k = k + 1;
end
end
