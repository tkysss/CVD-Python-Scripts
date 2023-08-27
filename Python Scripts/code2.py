from scipy import optimize

def value(vector):
    #compute the value of a branching verctor
    def h(x):
        return sum([x**-v for v in vector]) -1
    return optimize.brenth(h, 1, 2)

def join(x, y):
    return [u + v for u in x for v in y]

def add(a, x):
    return join([[a]],x)

def find_Hv(depth, order):
    
    if depth<=0:
        return [[(0,0)]]
    if Hv_branches.__contains__((depth,order)):
        return Hv_branches[(depth,order)]
    
    #generate the branchings according to VC.1 - 8  
    res = [];
    for i in range(order,10): 
        if i==0:
            res = res + add((1,0), find_Hv(depth-1,i)) #VC-3
        elif i==1:
            res = res + add((2,0), find_Hv(depth-2, i))  #VC-4
        elif i==2:
            res = res + add((2,2) , join(find_Hv(depth-2, i),find_Hv(depth-2, i)))  #VC-5
        elif i==3:
            res = res + add((1,5) , join(find_Hv(depth-1, i),find_Hv(depth-5, i)))  #VC-6
        elif i==4:
            res = res + add((1,4) , join(find_Hv(depth-1, i),find_Hv(depth-4, i)))  #VC-6
        elif i==5:
            res = res + add((1,3) , join(find_Hv(depth-1, i),find_Hv(depth-3, i)))  #VC-6
        elif i==6:
            res = res + add((2,3) , join(find_Hv(depth-2, i),find_Hv(depth-3, i)))  #VC-7
        elif i==7:
            res = res + add((2,2) , join(find_Hv(depth-2, i),find_Hv(depth-2, i)))  #VC-7
        elif i==8:
            res = res + add((2,3) , join(find_Hv(depth-2, i),find_Hv(depth-3, i)))  #VC-8
        elif i==9:
            res = res + add((1,2) , join(find_Hv(depth-1, i),find_Hv(depth-2, i)))  #VC-8
    
    Hv_branches[(depth,order)] = res
    return res

#get branching vectors via the tree
def get_vector():
    res=[]
    global count
    tmp = vec[count]
    if tmp==(0,0):
        return [0]
    if tmp[0]!=0:
        count=count+1
        res=[tmp[0] + x for x in get_vector()]
    if tmp[1]!=0:
        count=count+1
        res+=[tmp[1] + x for x in get_vector()]
    return res

#generate the braching trees
Hv_branches = dict()

#find the original branching vectors
vectors3 = find_Hv(3, 0)
vectors3.sort()

# check the lemmas 
for v in vectors3:
    if len(v)>=2 and (v[0]==(1,3) or v[0]==(1,4)) and v[1]==(1,2):
        if v in vectors3 :
            vectors3.remove(v)
    if v[0]!=(1) and v[0]!=(2) and v[0]!=(1,4) and v.count((1,2))!=0:
        if v in vectors3 :
            vectors3.remove(v)


# output 
for vec in vectors3:
    count = 0
    vector = [2] + get_vector()
    if value(vector)>1.74:
        print ('B3 ',vec,' ',vector,' ',value(vector))

    



