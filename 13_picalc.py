from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
# master process
if rank == 0:
    n = 1000000 # number of terms in leibniz formula
    # broadcast n to all processes
    comm.bcast(n, root=0)
else: # slave processes
    n = comm.bcast(None, root=0) # receive n from master process
pi = 0.0
# compute pi in parallel
for i in range(rank, n, size):
    pi += 1.0 / (2 * i + 1) * (-1) ** i
# reduce pi to master process
pi = comm.reduce(pi, op=MPI.SUM, root=0)
if rank == 0:
    pi *= 4
    print(pi)

# mpiexec -n 4 python test.py