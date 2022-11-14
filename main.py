import random
import csv

import matplotlib.pyplot as plt
import numpy as np
import math
from tqdm import tqdm
import timeit

plt.rcParams['figure.figsize'] = [10, 6] # set size of plot


def Solve(set, desired_sum):
    n = len(set)
    sel = [[0] * n for i in range(n+1)]

    k = 0
    crnt_sum = 0
    found = 0

    subset_list = []

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

                # print(found, ' : ',  answer_list)
                subset_list.extend(answer_list)
                
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

    return found


def write_tsv_File(file_path):
    f = open(file_path, 'w', encoding='utf-8')

    for _ in range(100000):
        data = "%d\t" % random.randrange(1, 30)
        f.write(data)

    f.close()


def load_tsv_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')

    reader = csv.reader(f, delimiter='\t')

    raw_data = list(reader)

    raw_data = raw_data[0]

    num_list = []
    for data in raw_data:
        if data != '':
            num_list.append(int(data))

    return num_list
 
if __name__=='__main__':
    # Use tsv file. 
    write_tsv_File('/Users/ajin/Desktop/2022/2022 2학기/알고리즘/Active_Learning/Sum_of_subsets/input.tsv')
    num_list = load_tsv_file('/Users/ajin/Desktop/2022/2022 2학기/알고리즘/Active_Learning/Sum_of_subsets/input.tsv')


    ns = []
    for n in range(10, 40):
        ns.append(n)

    # print(ns)

    ts = []

    sol = []

    for n in tqdm(ns, desc="dataset"):
        start_time = timeit.default_timer() # 시작 시간 체크

        sample = num_list[:n]
        sample_sum = random.randrange(n, n*15)

        sol_amount = Solve(sample, sample_sum)
        sol.append(sol_amount)

        end_time = timeit.default_timer() # 종료 시간 체크

        # 실행 시간
        terminate_time = end_time - start_time
        ts.append(terminate_time)

    print(ts)

    # plt.plot(ns, ts, 'b-')
    # plt.show()
    # plt.plot(ns, sol, 'r--')
    # plt.show()


    fig = plt.figure()

    #Graph
    fig, axes = plt.subplots(nrows=3, ncols=1)

    axe_0 = plt.subplot(1,2,1)
    axe_0.plot(ns, ts, 'b-')

    axe_1 = plt.subplot(1,2,2)
    axe_1.plot(ns, sol, 'r--')


    plt.show()



    
