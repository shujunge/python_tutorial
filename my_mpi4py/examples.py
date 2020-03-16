from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print ("hello world from process ", rank)

"""
mpiexec -n 5 python helloWorld_MPI.py
"""