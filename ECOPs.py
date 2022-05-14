from sympy import  mod_inverse

def ADD(A, B, E):
    
    x1 = A[0]
    y1 = A[1]
    x2 = B[0] 
    y2 = B[1]
    a = E[0]
    b = E[1]
    p = E[2]

    if x1 == x2 and y1 == y2:
        _lambda = (3*x1*x1 + a) * (mod_inverse(2*y1, p))
    else:
        _lambda = (y2 - y1)*(mod_inverse((x2 - x1), p))

    x3 = _lambda*_lambda - x1 - x2
    y3 = _lambda*(x1 - x3) - y1

    x3 = x3 % p
    y3 = y3 % p

    while(x3 < 0):
        x3 = x3 + p

    while(y3 < 0):
        y3 = y3 + p
    
    R=[x3,y3]
    return R

def Double_and_Add(A,E,k):
    A_=A
    
    Binary_k = bin(k) 
    Binary_k = Binary_k[2:len(Binary_k)] 
    
    
    for i in range(1, len(Binary_k)):
        currentBit = Binary_k[i: i+1]
        #always apply doubling
        A_ = ADD(A_, A_, E)
        
        if currentBit == '1':
            #add base point
            A_ = ADD(A_, A, E)
    
    return A_