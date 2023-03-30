from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# matrix sizes
N = 4
M = 3
K = 5

# initialize matrices
A = np.random.rand(N, M) if rank == 0 else None
B = np.random.rand(M, K) if rank == 0 else None
C = np.empty((N, K)) if rank == 0 else None

# broadcast matrices
comm.Bcast([A, MPI.DOUBLE], root=0)
comm.Bcast([B, MPI.DOUBLE], root=0)

# compute matrix multiplication
for i in range(N):
    for j in range(K):
        C[i][j] = 0.0
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

# gather results on root process
comm.Gather([C, MPI.DOUBLE], None if rank != 0 else [C, MPI.DOUBLE])

if rank == 0:
    print("A = ")
    print(A)
    print("B = ")
    print(B)
    print("A * B = ")
    print(C)
