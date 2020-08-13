
def hashsort(array):
   
    
    # get biggest element from array (max_elem)
    # create array of the size 'max_elem + 1' with values initialized to "0"
    
    # for each element in the input array, add 1 to the value of the index 
    # which matches the value of the element in the input array

    # from zero to the size of the biggest element in the input array,
    # if the value at the index in the created array is not 0,
    # output the index as many times as the value is large 


    max_elem = max(array) 
    table = [0] * (max_elem + 1) 
    
    # n operations

    for i in range(0,len(array)):
        table[array[i]] += 1

    # max_elem operations

    for i in range(0,max_elem + 1):
        if(table[i]): 
            for j in range(0, table[i]): # size of i operations 
                print(i)                 # max: len(array) => n 


if __name__ == "__main__":
   arr = [92,23,21,1,7000,54,32,122,54,32]

   hashsort(arr)


    # k = largest element in array

    # N + N * k -> hashsort O(N), for all k < N

    # or 

    # N + n * log(n)


