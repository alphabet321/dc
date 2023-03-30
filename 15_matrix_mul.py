from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

rows = 3
cols = 3

if(rank == 0):
    matrix1 = [[random.randint(1,10) for j in range(cols)] for i in range(rows)]
    matrix2 = [[random.randint(1,10) for j in range(cols)] for i in range(rows)]
else:
    matrix1 = None
    matrix2 = None

matrix1 = comm.bcast(matrix1,root = 0)
matrix2 = comm.bcast(matrix2,root = 0)

result_row = [0 for j in range(cols)]

for j in range(cols):
    summ = 0
    for k in range(cols):
        summ += matrix1[rank][k] * matrix2[k][j]
    result_row[j] = summ

results = comm.gather(result_row,root = 0)

if rank == 0:
    print('A')
    for row in matrix1:
        print(row)
    print('B')
    for row in matrix2:
        print(row)
    print('results')
    for row in results:
        print(row)