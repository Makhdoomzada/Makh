



# In[1]:

import numpy as np 
import time


# 
# Using `NumPy`'s linear algebra module, develop a function `problem1(A,b)` that returns `True` if the linear equation system $\mathbf{Ax} = \mathbf{b}$ has a unique solution and `False` otherwise.

# In[ ]:


def problem1(A,b):
    if A.ndim!=2 and b.ndim!=1:
        return(False)
    elif A.shape[0]!=A.shape[1]:
        return(False)
    elif b.shape[0]!=A.shape[1]:
        return(False)
    elif abs(np.linalg.det(A)) < 1e-15:
        return(False)
    else: 
        return(True)
        
        
        
    



# 
# Using `NumPy`'s linear algebra module and your solution to Problem 1, develop a function `problem2(A,b,method)` that returns the elapsed time (seconds) required to solve the linear equation system $\mathbf{Ax} = \mathbf{b}$ using (i) Gaussian Elimination if `method = "ge"` (`linalg.solve()`) or (ii) the inverse ($\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$) method if `method = "inv"`. If the linear equation system does not have a unique solution or is not solvable, return `None`.

# In[ ]:

def problem2(A,b,method):
 
   
    prob1= problem1(A,b)
    if prob1== True:
        if method == "ge":
            start = time.perf_counter()
            y = np.linalg.solve(A, b)       
            end = time.perf_counter()
            return end-start
        elif method =="inv":
            start = time.perf_counter()
            y = np.linalg.inv(A)
            np.dot(y,b)
            end = time.perf_counter()
            return end-start
    else:
        return None
            





# Use the `NumPy` functions `polyfit()`, `random.random()`, and your solution to Problem 2 to develop a function `problem3(n_array, method)` that returns a `array` of the coefficients of the best-fit polynomial $t(n)$ for the runtime of Gaussian elimination or the inverse matrix method depending on the value of `method` (`"ge"` or `"inv"`). The runtime should be fit to a third order polynomial:
# 
# $t(n) = a_0 + a_1 n + a_2 n^2 + a_3 n^3$
# 
# where $t(n)$ is the runtime of the method for solving a linear system of size $n$. The input argument `n_array` specifies the dimensions of the linear systems that should be used as a sample set to measure runtimes which are then used to determine a best-fit. The best fit $t(n)$ provides us with an approximation of the runtime versus linear system size for the specified method (`"ge"` or `"inv"`).
# 
# The `random.random()` function should be used to generate the linear equation systems of different dimensions (specified by `n_array`) which, in turn, will be used to create timing data points $(n, t)$ for fitting to the polynomial.

# In[ ]:



def problem3(n_array, method):
    z = []
    for i in n_array:
        a1= np.random.random((i,i))
        a2= np.random.random((i,1))
        A= np.matrix(a1)
        b= np.matrix(a2)
        t= problem2(A,b, method)
        z.append(t)
    ta= np.array(z)
    c = np.polyfit(n_array,ta,3)
    return c
