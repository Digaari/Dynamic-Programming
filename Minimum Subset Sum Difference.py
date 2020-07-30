arr = [ 3, 1, 4, 2, 2, 1 ]
n = len(arr)
Range = 0
for i in range(n):
    Range += arr[i]

def SubsetSum(arr, n, Range):
    #making an array with False
    t = [[False for x in range(Range+1)] for x in range(n+1)]

    
    #initialisation with
    for i in range(n+1):
        t[i][0]= True
    
    for i in range(1, n+1):
        for j in range(1,Range+1):
            if arr[i-1]<=j:
                t[i][j]= (t[i-1][j-arr[i-1]] or t[i-1][j])
            else: 
                t[i][j]=t[i-1][j]
    
    vec = 0

    for j in range(Range//2, -1,-1):
        if (t[n][j]):
            vec = Range - (2*j)
            break
    return vec
            
    


print(SubsetSum(arr, n, Range))
