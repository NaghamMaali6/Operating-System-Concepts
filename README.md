# Operating-System-Concepts: Deadlock

This project about deadlock detection using the Banker's algorithm in python.

The code reads matrices representing resource allocation (Allocation), resource requests (Request), and available resources (Available) from CSV files. 

The algorithm checks for consistency in the number of processes between Allocation.csv and Request.csv. 

If the dimensions are consistent, it initializes variables and executes the Banker's algorithm to determine whether the system is in a safe state. 

The result, indicating the presence or absence of deadlocks, along with details such as the deadlocked processes or the safe sequence, is printed accordingly. 

If the dimensions are inconsistent, an error message is displayed, and the program exits.
