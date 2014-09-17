def _w((r, n), (r2, v)): return [(r,n),(r+r2,n-v)][n-v>=0]
_a=lambda (y, x): reduce(_w,
   [(y, x)] + zip('M.CM.D.CD.C.XC.L.XL.X.IX.V.IV.I'.split('.'),
       [i*j for j in [100,10,1] for i in [10,9,5,4]] + [1]))
y=_,x=_a(('',long(raw_input("number>>>"))))
while x:y=_,x=_a(y)
print y[0]
