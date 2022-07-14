#!/usr/bin/env python
# coding: utf-8

# # Appendix A: Code templates
# 
# Here templates are provided for various codes useful in reactor design:
# 
# 1. Non-linear system of equations solver
# 2. Ordinary differential equations system solver

# ## 1. Non-linear algebraic equations system solver

# In[1]:


########## Non-linear system of equations solver ##########

###### Import packages

import numpy as np
import pandas as pd
import scipy.optimize as opt

###### Specify known values

### Constants
Kc  = 0.1      # mol / L
yA_0 = 1.0     # mol / mol
P   = 10.0      # atm
R   = 0.082    # atm L / mol K
T   = 340      # K

###### Define system of equations

def alg(U):
    
    ### Redefine inputs
    CA0 = U[0]
    Xe = U[1]
    
    ### Define equations
    setzero = np.zeros(len(U))
    setzero[0] = CA0-yA_0*P/R/T
    setzero[1] = Xe - (Kc*(1-Xe)/(4*CA0))**0.5
    
    ### Reorganize list to fit required dimensions 
    setzero = np.array(setzero).tolist()
    
    return setzero

###### Solve based on initial guesses

### Initial guesses
varguess = [0.5,0.5]

### Solver
U = opt.fsolve(alg,varguess)   # Enter function vollowed by variable guesses
U = np.array(U)                # Convert to numpy array for convenience

### Verify that solution was achieved
zerocheck = alg(U)
print("Zerocheck: ",zerocheck)

### Save results in dataframe
soln = pd.DataFrame(['Var 1','Var 2'],columns = ['Variables'])
soln[['Values']] = pd.DataFrame(U)
soln


# ## 2. Ordinary differential equations system solver

# In[ ]:


########## Ordinary differential equations system solver ##########

###### Import packages

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

###### Specify known values

c1 = 1
c2 = 0.2

###### Set initial conditions of independent variables U

U0 = [10,0] # In this example U0[0] is variable A and U0[1] is variable B

###### Determine integration limits via independent variable array tlim
tlim = (0,10)
tlist = np.linspace(tlim[0],tlim[1],num=101) # Not essential--specifies intervals along tlim to store U values

###### Define differential equations along with additional required calculations

def diff(t,U):
    
    # Assign values to inputs if desired
    A = U[0]
    B = U[1]
    
    # Define equations
    dU=np.zeros(len(U))
    dU[0] = c1 - c2 * A**0.5
    dU[1] = c2 * A**0.5
    
    # Reorganize list to fit required dimensions 
    dU = np.array(dU).tolist()
    
    return dU

###### Integrate

soln = solve_ivp(diff,tlim,U0,t_eval=tlist)

### Obtain output dependent variable array U and independent variable array t

U = soln.y.T # T makes transpose; not essential but easy for input to dataframe
t = soln.t

A = U[:,0] # Define individual variables within U if desired
B = U[:,1]

### Define pandas dataframe with outputs

soln_df = pd.DataFrame(t,columns = ['Time (s)'])
soln_df[['A (units)','B (units)']] = pd.DataFrame(U)

### Save dataframe to a csv
soln_df.to_csv('ODE_solver_output.csv')

### Report dataframe
soln_df


# In[ ]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

fig = make_subplots(rows=3,cols=1,specs=[[{"secondary_y": True}],[{"secondary_y": True}],[{"secondary_y": True}]])

xvals = np.array([1,2,3,4,5])
yvals = xvals**2

fig.append_trace(go.Scatter(x=xvals,y=yvals,name='name of stuff'),row=1,col=1)

fig.show()


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

xvals = np.array([1,2,3,4,5])
yvals = xvals**2
plt.plot(xvals,yvals)

plt.show()


# In[ ]:




