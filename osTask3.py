#Name : Nagham Maali
#ID : 1212312
#Sec. : 2

import pandas as Pd  #pandas is a Python library used for working with data sets , It has functions for analyzing , cleaning , exploring , and manipulating data .

print("\t *Detection Algorithm* \n")

#Read Allocation.csv file :
Allocation = Pd.read_csv("Allocation.csv")
print("*Allocation Matrix :\n")
print("*****************************************************************")
print(Allocation)

#Read Request.csv file :
Request = Pd.read_csv("Request.csv")
print("*Request Matrix :\n")
print("*****************************************************************")
print(Request)

#ensure that the dimensions are consistent(number of processes in Allocation.csv and Request.csv are the same) :
if Allocation.shape[0] == Request.shape[0] :
    N = Allocation.shape[0]  #shape is an attribute in pandas to get the dimensions of an array
    print("\nThe dimensions are consistent.")
    print("\nNumber of processes :")
    print(N)
    
    print("\nwe can apply the Detection Algorithm.")
    print("\nwe just need Available vector ... ")
    
    #Read Available.csv file :
    Available = Pd.read_csv("Available.csv" , index_col = False)  #read_csv is a pandas function to read CSV file
    print("\n*Available vector :\n")
    print("**********************************************************")
    print(Available)
    
    M = Available.shape[1]  #number of Resources
    
    print("\nDetection Algorithm Execution...")
    
    #Initialize work and finish vectors :     
    work = Available.to_numpy().flatten().astype(int)  #convert Available to integer and store into work     
    finish = [False] * N                               #flatten method is used to return a flattened version of an array int 1D array
                                                       #to_numpy is a pandas method that is used to convert a dataframe to a NumPy array
                                                       
    Safe_Sequence = []  #the sequence of processes that are in the safe state
    
    while True :
        isfound = False
        
        for i in range(N) :                                                                  
            if not finish[i] and (Request.iloc[i , 1 :].values.astype(int) <= work).all() :  #astype method is used to cast the elements of an array to a specified data type
                work += Allocation.iloc[i , 1 :].values.astype(int)  #iloc method is used to select rows and columns by integer location
                finish[i] = True                                     # values is a pandas attribute
                Safe_Sequence.append(i + 1)  #add p to the Safe Sequence by append method which is used to append values to a list
                isfound = True
                break
        if not isfound :
            break        
            
    DeadlockedP = [i + 1 for i in range(N) if not finish[i]]  #the sequence of processes that are in the deadlock state
    
    if DeadlockedP :
        print("\nDeadlock Detected!!!") 
        print(f"\nDeadlocked processes : {DeadlockedP}")
    else :
        print("\nNo Deadlock Detected.")
        print("\nThe system is in the safe state.")
        print(f"\nSafe sequence : < {' , '.join(map(str , Safe_Sequence))} >")  #join is a string method that concatenates elements of an iterable using a specified separator
                                                                                #map function is used to apply a specified function to all the items in an input list
else :
    print("\nOpps! The dimensions are NOT consistent. ")
    print("\nsorry , we can't apply the Detection Algorithm.") 
    print("\ntry different files later ... Bye.")
    exit()  #end the program
    
#This Python code implements a deadlock detection algorithm using the Banker's algorithm. 
#It reads matrices representing resource allocation (Allocation), resource requests (Request), and available resources (Available) from CSV files. 
#The algorithm checks for consistency in the number of processes between Allocation.csv and Request.csv. 
#If the dimensions are consistent, it initializes variables and executes the Banker's algorithm to determine whether the system is in a safe state. 
#The result, indicating the presence or absence of deadlocks, along with details such as the deadlocked processes or the safe sequence, is printed accordingly. 
#If the dimensions are inconsistent, an error message is displayed, and the program exits.    

#the system in in the deadlock state 
#example to make the system be in the safe state : Available : 2 0 5 5 6