m1= [
[1,2,3],
[4,5,6],
[7,8,9],
]

i= [
[1,0,0],
[0,1,0],
[0,0,1],
]

p1_3= [
[0,0,1],
[1,0,0],
[0,1,0],
]

p2_3= [
[0,1,0],
[0,0,1],
[1,0,0],
]

p1=[
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
]

p2=[
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
[0,0,1,0],
]

p3=[
[0,0,1,0],
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
]

p4=[
[0,1,0,0],
[1,0,0,0],
[0,0,1,0],
[0,0,0,1],
]

p5=[
[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
]

p6=[
[0,1,0,0],
[0,0,1,0],
[1,0,0,0],
[0,0,0,1],
]

p7=[
[0,1,0,0],
[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
]

p8=[
[0,0,1,0],
[1,0,0,0],
[0,0,0,1],
[0,1,0,0],
]

p9=[
[1,0,0,0],
[0,0,1,0],
[0,0,0,1],
[0,1,0,0],
]

p10=[
[1,0,0,0],
[0,0,1,0],
[0,1,0,0],
[0,0,0,1],
]

p11=[
[0,0,0,1],
[0,0,1,0],
[0,1,0,0],
[1,0,0,0],
]

p12=[
[1,0,0,0],
[0,1,0,0],
[0,0,0,1],
[0,0,1,0],
]

p13=[
[0,0,0,1],
[0,1,0,0],
[0,0,1,0],
[1,0,0,0],
]

p14=[
[0,0,0,1],
[0,0,1,0],
[1,0,0,0],
[0,1,0,0],
]

p15=[
[0,0,1,0],
[0,0,0,1],
[1,0,0,0],
[0,1,0,0],
]





cut_3= [[i,1/3],[p1_3,1/3],[p2_3,1/3]]
yugi_4= [[p1,1/4],[p2,1/12],[p3,1/12],[p4,1/12],[p5,1/8],[p6,1/8],[p7,1/4]]
riffle_4= [[p5,1/6],[p8,1/6],[p9,1/6],[p1,1/6],[p10,1/6],[p3,1/6]]
overhand_4=[[p11,1/8],[p12,1/8],[p13,1/4],[p14,1/4],[p15,1/4]]

def print_matrix(m):
    for l in m:
        print(l)
    print()
    return

def get_neighbor_matrix(p):
    dimension= len(p)
    neighbor_matrix= []
    for i in range(dimension):
        neighbor_matrix= neighbor_matrix + [[]]
        for j in range(dimension):
            coef= 0
            for k in range(dimension):
                coef= coef + p[(j+1)%dimension][(k+1)%dimension]*p[i][k]
            neighbor_matrix[i]= neighbor_matrix[i] + [coef]
    return neighbor_matrix

def matrix_sum(m1,m2):
    dimension= len(m1)
    m3= []
    for i in range(dimension):
        m3= m3 + [[]]
        for j in range(dimension):
            m3[i]= m3[i] + [m1[i][j]+m2[i][j]]
    return m3

def matrix_scal(m,s):
    dimension= len(m)
    new_m= []
    for i in range(dimension):
        new_m= new_m + [[]]
        for j in range(dimension):
            new_m[i]= new_m[i] + [m[i][j]*s]
    return new_m

def get_relative_matrix(shuffle,dim):
    relative_matrix= []
    for i in range(dim):
        relative_matrix= relative_matrix + [[]]
        for j in range(dim):
            relative_matrix[i]= relative_matrix[i] + [0]

    for oc in shuffle:
        relative_matrix= matrix_sum(relative_matrix,matrix_scal(get_neighbor_matrix(oc[0]),oc[1]))
    return relative_matrix

def get_absolute_matrix(shuffle,dim):
    absolute_matrix= []
    for i in range(dim):
        absolute_matrix= absolute_matrix + [[]]
        for j in range(dim):
            absolute_matrix[i]= absolute_matrix[i] + [0]

    for oc in shuffle:
        absolute_matrix= matrix_sum(absolute_matrix,matrix_scal(oc[0],oc[1]))
    return absolute_matrix

def matrix_product(m1,m2,dim):
    new_m= []
    for i in range(dim):
        new_m= new_m + [[]]
        for j in range(dim):
            new_m[i]= new_m[i] + [0]
            for k in range(dim):
                new_m[i][j]= new_m[i][j] + m1[i][k]*m2[k][j]
    return new_m

def dis_equi(m,dim):
    dist= 0
    for i in range(dim):
        for j in range(dim):
            dist= dist + abs(1/dim - m[i][j])
    return dist

def dis_equi_2(m,dim):
    dist= 0
    for i in range(dim):
        for j in range(dim):
            if j != (i+1)%dim:
                dist= dist + abs(1/(dim-1) - m[i][j])
    return dist

def pow_dist(shuffle,dim,scal,pow):
    print("pow:",pow)
    PA= matrix_scal(get_absolute_matrix(shuffle,dim),scal)
    PR= matrix_scal(get_relative_matrix(shuffle,dim),scal)

    PA_pow= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],]
    PR_pow= [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],]
    for i in range(pow):
        PA_pow= matrix_product(PA_pow,PA,dim)
        PR_pow= matrix_product(PR_pow,PR,dim)

    print_matrix(PA_pow)
    print(dis_equi(matrix_scal(PA_pow,(1/scal)**pow),dim))
    print()
    


print("yugi")
#pow_dist(yugi_4,4,24,1)
#pow_dist(yugi_4,4,24,2)
pow_dist(yugi_4,4,24,100)
print("riffle")
#pow_dist(riffle_4,6,24,1)
#pow_dist(riffle_4,6,24,2)
pow_dist(riffle_4,4,6,100)
print("overhand")
#pow_dist(overhand_4,8,24,1)
#pow_dist(overhand_4,8,24,2)
pow_dist(overhand_4,4,8,100)
