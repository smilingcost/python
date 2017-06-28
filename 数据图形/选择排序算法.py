# -*- coding: cp936 -*-
data_set = [ 9,1,22,31,45,3,6,2,11 ]
 
smallest_num_index = 0 #初始列表最小值,默认为第一个

loop_count = 0
for j in range(len(data_set)):
    for i in range(j,len(data_set)):
        if data_set[i] < data_set[smallest_num_index]: #当前值 比之前选出来的最小值 还要小,那就把它换成最小值
            smallest_num_index = i
        loop_count +=1
    else:
        print("smallest num is ",data_set[smallest_num_index])
        tmp = data_set[smallest_num_index]
        data_set[smallest_num_index] =  data_set[j]
        data_set[j] = tmp

    print(data_set)
    print("loop times", loop_count)
    # 先确定元祖中最小的数放在第一位，然后按顺序依次确定