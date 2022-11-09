import numpy as np
import pulp as pl

def optimal_group_formation(a, C, NM):
    P = a.shape[0]
    M = a.shape[1]
    NC = 2
    prob = pl.LpProblem("CFP", pl.LpMinimize)
    W = []
    for k in range(C):
        for i in range(P):
            for j in range(M):
                var = pl.LpVariable("w_%s_%s_%s" % (i,j,k), 0, 1, pl.LpInteger)
                W.append(var)
        
    Z = []
    for k in range(C):
        for i in range(P):
            var = pl.LpVariable("Z_%s_%s" % (i, k), 0, 1, pl.LpInteger)
            Z.append(var)
        

    Y = []
    for k in range(C):
        for j in range(M):
            var = pl.LpVariable("Y_%s_%s" % (j, k), 0, 1, pl.LpInteger)
            Y.append(var)
        
        
    CF = []
    for k in range(C):
        var = pl.LpVariable("CF_%s" % (k), 0, 1, pl.LpInteger)
        CF.append(var)
        
    Y = np.array(Y)   #jk
    Y=Y.reshape(C, M)

    Z = np.array(Z)   #ik
    Z=Z.reshape(C,P)

    W = np.array(W)   #ijk
    W = W.reshape(C,M*P)

    CF = np.array(CF)
    
    Suma = []
    for k in range(C):
        v = W[k].reshape(P,M)
        Suma.append(v)
        
    Suma1 = []                                #primera sumatoria
    for k in range(C):
        for i in range(P):
            vv = Suma[k][i]*(1-a[i])
            Suma1.append(vv)
            
    Suma2 = []
    for k in range(C):
        for i in range(P):
            vvv = -1*(Suma[k][i]-Z[k][i])
            Suma2.append(vvv)
    
    Suma3 = []                               #segunda sumatoria
    for k in range(C):
        vvvv=Suma2[k*P:(k+1)*P]*a
        Suma3.append(vvvv)
        
    F1=sum(Suma1)  #funcion objetivo
    F2=sum(sum(Suma3))   
    prob += sum(F1)+sum(F2)

    Cont1 = sum(Z)                         # firts constrain
    Contrain1 = []
    for i in range(P):
        c1=Cont1[i]==1
        Contrain1.append(c1)
        
    Cont2 = sum(Y)                         # firts constrain
    Contrain2 = []
    for j in range(M):
        c2=Cont2[j]==1
        Contrain2.append(c2)
        
    Contrain3=sum(CF)>=NC
    Cont4=np.apply_along_axis(sum, 1, Y)
    Contrain4 = []
    for k in range(C):
        c4=Cont4[k] <= CF[k]*NM
        Contrain4.append(c4)
    Cont5 = []
    for k in range(C):
        for i in range(P):
            cc5=W[k][i*M:(i+1)*M]-Z[k][i]-Y[k]+1.5
            Cont5.append(cc5)
    Contrain5 = []
    for l in range(len(Cont5)):
        for j in range(M):
            c5=Cont5[l][j]>=0
            Contrain5.append(c5)
    Cont6 = []
    for k in range(C):
        for i in range(P):
            cc6=1.5*W[k][i*M:(i+1)*M]-Z[k][i]-Y[k]
            Cont6.append(cc6)
            
    Contrain6 = []
    for l in range(len(Cont6)):
        for j in range(M):
            c6=Cont6[l][j]<=0
            Contrain6.append(c6)
            
    for i in range(P):
        prob += Contrain1[i]
    for j in range(M):
        prob += Contrain2[j]
    prob += Contrain3
    for k in range(C):
        prob += Contrain4[k]
    for l in range(M*P*C):
        prob += Contrain5[l]
    for v in range(M*P*C):
        prob += Contrain6[v]
    estado = prob.solve() 
    name_selected = []   # resuelve usando el solucionador predeterminado, que es cbc
    for v in prob.variables():
            if v.varValue==1:
                # print(v.name, "=", v.varValue)
                name_selected.append(v.name)

    objective_value = prob.objective.value()

    return name_selected, objective_value
