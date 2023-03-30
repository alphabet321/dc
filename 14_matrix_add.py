from mpi4py import MPI
import random

# Initialize MPI environment
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Matrix dimensions
rows = 3
cols = 3

# Randomly generate matrices
if rank == 0:
    matrix1 = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]
    matrix2 = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]
else:
    matrix1 = None
    matrix2 = None

# Broadcast matrices to all processes
matrix1 = comm.bcast(matrix1, root=0)
matrix2 = comm.bcast(matrix2, root=0)

# Initialize result matrix
result_row = [0 for j in range(cols)]

# Compute matrix addition
for j in range(cols):
    result_row[j] = matrix1[rank][j] + matrix2[rank][j]
print(result_row,rank)

# Gather results to root process
results = comm.gather(result_row, root=0)

# Print results from root process
if rank == 0:
    print("Matrix 1:")
    for row in matrix1:
        print(row)
    print("Matrix 2:")
    for row in matrix2:
        print(row)
    print("Result:")
    for i in range(rows):
        print(results[i])