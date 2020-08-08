
def hashsort(array):
    
    # get biggest element from array
    # create array of the size 'max_elem + 1' with 0
    
    # for each element in the input-array, add one to the 
    # element with the index (of the created array) which matches the value 
    # contained in in input_array - for each occurence of it

    max_elem = max(array) 
    table = [0] * (max_elem + 1) 
    
    # n operations

    for i in range(0,len(array)):
        table[array[i]] += 1

    # max elem operations

    for i in range(0,max_elem + 1):
        if(table[i]): 
            for j in range(0, table[i]): # size of i operations 
                print(i)                 # max: len(array) => n 

if __name__ == "__main__":
   arr = [92,23,21,1,7000,54,32,122,54,32]

   hashsort(arr)


    # k = largest element in array

    # N + N * k

    # hashsort: O(N) < O(N**2) for all k < N 
