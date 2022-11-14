# A Dynamic Programming solution for 'sum of subset' problem.
# Returns true if there is a subset of set[]

def isSubsetSum(set, n, sum):

    subset = ([ [False for i in range(sum+1)]
                for i in range(n+1) ] )
    
    # if sum == 0, -> answer == true.
    for i in range(n+1):
        subset[i][0] = True

        # If sum is not 0 and set is empty,
        # then answer in false
        for i in range(1, sum+1):
            subset[0][i] = False
        
        # Fill the subset table in bottom up manner
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if j < set[i-1]:
                    subset[i][j] = subset[i-1][j]
                
                if j >= set[i-1]:
                    subset[i][j] = (subset[i-1][j] or subset[i-1][j-set[i-1]])

    return subset[n][sum]

def Solve(set, n, desired_sum):
    len(set)

    sel = [[0] * n for i in range(n+1)]

    k = 0
    crnt_sum = 0
    found = 0

    sel[0] = 1

    while(True):
        if( k < n and sel[k] == 1 ):
            # 현재 셀 더하면 원하는 합이 되면 
            if( crnt_sum + set[k] == desired_sum ):
                found += 1

                answer_list = []

                for i in range(n):
                    if ( sel[i] == 1 ):
                        answer_list.append(set[i])

                print(found, ' : ',  answer_list)
                
                sel[k] = 0
            
            elif( crnt_sum + set[k] < desired_sum ):
                crnt_sum += set[k]
            
            else:
                sel[k] = 0

    
        else:
            k -= 1
            while( k>=0 and sel[k]==0):
                k-=1

            if( k < 0 ):
                break

            sel[k] = 0

            crnt_sum-=set[k]

        k+=1

        if(k<n):
            sel[k] = 1
    
    if(found == 0):
        print("Not possible subsets!")


                    

if __name__=='__main__':
    set = [15,3,7,2,17,23,25,29,14,2]
    sum = 27

    Solve(set, len(set), sum)
