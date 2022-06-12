MIN,MAX=-1000,1000
def minmax(depth,nodeIndex,maximumPlayer,values,alpha,beta):
    if(depth==3):
        return values[nodeIndex]
    if maximumPlayer:
        best=MIN
        for  i in range(2):
            val=minmax(depth+1,nodeIndex*2+i,False,values,alpha,beta)
            best=max(val,best)
            alpha=max(alpha,best)
            if(beta<=alpha):
                break
        return best
    else:
        best=MAX
        for i in range(2):
            val=minmax(depth+1,nodeIndex*2+i,True,values,alpha,beta)
            best=min(val,best)
            beta=min(beta,val)
            if(beta<=alpha):
                 break
        return best
values=[3,5,6,9,1,2,0,-1]
print(minmax(0,0,True,values,MIN,MAX))