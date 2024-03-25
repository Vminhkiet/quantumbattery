import matplotlib.pyplot as plt
import tqix as tq
from tqix import *
import numpy as np, qiskit
from qiskit.quantum_info import Operator
import base.Gradient as gr
from scipy.linalg import expm
import base.constant as ct
import base.hamiltonian as hm
from qsee.compilation.qsp import QuantumStatePreparation
def ansatz(t,thetas):
 """
    Input:
      t:time
      H1:hamiltonian operator
     Output:
      Return quantum circuit representing the operation e^-(i*t*H1)
 """
 ansatz=QuantumCircuit(ct.N)
 u=expm(-1j*t*hm.h1(thetas))
 ansatz = QuantumStatePreparation.prepare(u) 
 return ansatz
def qc():
 """
   Input:

   Output:
    Returns the quantum circuit with all qubits given each qubit an additional Rx gate
 """
 qc=QuantumCircuit(ct.N)
 qc.rx(np.pi/2,range(ct.N))
 return qc
def aqc(t,thetas):
 """
    Input:

      t:time
      H1:hamiltonian operator
    Output:
      Return quantum circuit = qc + ansatz
 """
 qc1=qc()
 ansatz1=ansatz(t,thetas)
 qc1.compose(ansatz1,range(ct.N),inplace=True)
 
 return qc1