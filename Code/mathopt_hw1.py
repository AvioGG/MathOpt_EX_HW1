# -*- coding: utf-8 -*-
"""
Hasan Nazım Biçer
12.11.2020
"""
import numpy as np

def insert_sort_string(A):    
    print(A)
    B=list(A)
    for i in range(1,len(B)):
        temp=B[i]
        j=i
        while(j>0 and temp<B[j-1]):
            B[j]=B[j-1]
            j=j-1
        B[j]=temp
        print("".join(B))
    return "".join(B)

def insert_sort_number(A):
    print(A)    
    for i in range(1,len(A)):
        temp=A[i]
        j=i
        while(j>0 and temp<A[j-1]):
            A[j]=A[j-1]
            j=j-1
        A[j]=temp
        print(A)
    return A

def magic_function(n):
    result=0
    for i in range(0,n):
        result=result+(2*i+1)
    return result

def mult_table(n):
    A=np.zeros((n,n))    
    for i in range(0,n):
        for j in range(0,n):
            A[i,j]=i*j
    return A

def opt_mult_table(n):
    a= np.array(range(n))
    return a.reshape((-1, 1))*a

def mult_table3D(n):
    A=np.zeros((n,n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                A[i,j,k]=i*j*k
    return A           

def opt_mult_table3D(n):
    A= np.array(range(n))
    return np.reshape(np.outer(np.outer(A,A),A),(n,n,n))

def function_1(A,value):
    n= A.shape[0]
    for i in range(0,n):
        if A[i] == value:
            return i
    return -1

def function_2(A,value):
    n=A.shape[0]
    low=0
    high=n-1
    while(low <= high):
        mid=(low+high)/2
        if(A[mid]>value):
            high=mid-1
        elif A[mid]<value:
            low=mid+1
        else:
            return mid
    return -1

if __name__ == "__main__":
           
    #EXERCISE 1    
    #a
    STR1="FEDCBA"
    insert_sort_string(STR1)
    print("-------------------------------------------------------------")
    #b
    STR2="ABCDEF"
    insert_sort_string(STR2)
    print("-------------------------------------------------------------")
    #c
    STR3="ERLANGEN"
    insert_sort_string(STR3)
    print("-------------------------------------------------------------")
    #EXERCISE 2
    #a
    # calculated the magic function for X=[0,....,n-1]
    n=8
    for i in range(0,n):
        print(magic_function(i))
    #b
    # magic_function simply squares the input to that function
    print("-------------------------------------------------------------")
    
    #EXERCISE 3    
    # function mult_table and opt_mult_table is defined above
    
    # function mult_table simply iterates over each element
    # and multiplies the indexes of that element
    
    # function opt_mult_table is more optimized since it
    # only multiplies one column vector with its own 
    # transpose. (very fast in numpy, O(nlogn) as far as I know)
    
    n=6
    RES=mult_table(n)
    print(RES)
    RES2=opt_mult_table(n)
    print(RES2)      
    print("-------------------------------------------------------------")
    
    
    
    #EXERCISE 4
    STR4="HASANNAZIM"
    insert_sort_string(STR4)
    print("-------------------------------------------------------------")
    
    #EXERCISE 5
    
    #a
    # First function_1 is simply a linear search. It searches all of the 
    # array A one by one and if it finds the value, it returns 
    # its index, it there is no "value" in array A, it returns
    # -1.
    #
    # Second, function_2 is a binary search. It searches the sorted array A
    # and eliminates half of the array at each iteration depending on the
    # comparison of middle value of the array.
    # In other words, if the value is higher than the middle value of array
    # A, it simply eliminates lower half of the array (and the middle value).
    # It continues to do this until it either reaches the value and returns
    # its index, or never finds it and returns -1.
    
    
    
    #b
    # First function does work even if the entries of A are not sorted.
    # Because it simply iterates over each element of array A and never
    # exploits the sortedness of array A
    #
    # Second function does NOT work for unsorted arrays. It uses the sortedness
    # of array A to eliminate half of the array A at each iteration. It will
    # fail if the array is not sorted.
          
    
    #c
    #
    # First function has runtime O(n). As mentioned before it iterates over
    # each element until it finds the value.
    #
    #Second function has runtime O(log(n)). For each iteration it eliminates
    # half of the array. Hence runtime O(log(n))
    #-------------------------------------------------------------------------
    
    #EXERCISE 6
    #
    # Similar to before mult_table3D is a function that creates a 3-D
    # multiplication table by iterating over each element and filling each
    # entry
    #
    # opt_mult_table3D is an optimized function that basically cross products
    # each vector and creates a 3D cube(matrix) where each element is the
    # multiplication of its 3 indexes.
    n=3
    RES=mult_table3D(n)
    print(RES)
    print("-------------------------------------------------------------")
    RES2=opt_mult_table3D(n)
    print(RES2)      
    print("-------------------------------------------------------------")

        
    
