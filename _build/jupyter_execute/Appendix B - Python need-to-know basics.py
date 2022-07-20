#!/usr/bin/env python
# coding: utf-8

# # Appendix B: Python need-to-know basics

# *Need just some basic understanding to use Python for simple chemical engineering problem? Here's all you really "need" to know.*
# 
# ## What is Python?
# 
# Python is a high-level computing language--a way of executing and interpreting commands--that prioritizes human readibility. It does not on its own include much "functionality" since it is simply a "language." In order to use Python, you will need "packages" which consist of codes written in Python and other languages that allow you to do more complex work such as high-level math, plotting, data sorting, etc.
# 
# ## How is this different from MATLAB?
# 
# Many in chemical engineering who are new to Python are likely transitioning from MATLAB, the main software originally introduced throughout the curriculum. MATLAB is different from Pythong in a few key ways. Not only is it a language (based on C/C++), it is also a full program that includes a wide array of packages already downloaded. Additionally, MATLAB includes its own interface. Python, on the other hand, is used with a variety of "integrated development environments," or IDEs. Popular choices include Spyder (which has a fairly MATLAB-esque feel), Jupyter Notebooks (which allows for codes to be provided alongside outputs and interchanged with long text blocks), JupyterLab (an evolution of Jupyter Notebook which brings multiple utilities together), PyCharm, IDLE, Atom, and Thonny.
# 
# ## What are some pros and cons of Python compared to MATLAB?
# 
# The simplest benefit to Python is that it is free, while MATLAB requires a license which can cost as much as $2,000 or more unless you have lower-cost access through a university.
# 
# One key difference that has both pros and cons is that Python is not really "built" for anything other than being "intuitive." MATLAB, on the other hand, is built deliberately for computational work, and in many ways it is "optimized" for chemical engineering work. Everything you need is available and meant to work when downloaded. Python, on the other hand, is commonly used for not only computation/data science but also for software development, website creation, design, etc. The fact that Python is "open-source" can on one hand make it difficult to find the exact solution to your problem, but on the other hand allows for a large community to come up with solutions and easily share them on forums such as Stack Overflow.
# 
# The major "pro" for Python that comes from these facts is its adaptability. Those who learn Python can use it anywhere, while those who use MATLAB have to hope they can find a license (or pay for one) to use it. Furthermore, those who learn how to work with Python can apply their knowledge to problems outside the traditional chemical engineering scope. Such skills could enhance communication, foster collaboration, or facilitate a role transition.
# 
# All of these benefits are very clearly understood by the broader community. The TIOBE organization specializes in evaluating software quality and as of 2022 ranked Python the #1 programming language while MATLAB is listed at only #24 (https://www.tiobe.com/tiobe-index/). Other languages of note inlcude C, Java, and C++.
# 
# ## Do I need to care about the Python version?
# 
# Yes. While some syntax is the same between different versions, some can vary drastically. A slightly older Python 2 code will likely not function the same way if run in Python 3.
# 
# Fortunately, there are ways to simulate a Python 2 environment if you want to use a Python 2 code.
# 
# ## Where should I start?
# 
# A good place to start is Anaconda.com. Anaconda is a "distribution" of Python meaning that it includes the code, packages, IDEs, and various utilities to manage packages. The installation is free.
# 
# Once you download Anaconda, it is best to start with some of their simple tutorials. One will be added here eventually. If you are coming from MATLAB, it may be best to start with Spyder. My preference is JupyterLab (which I'm actively writing this with).
# 
# **Important note:** there are likely multiple different Python environments on your computer between one the one Anaconda installs, one you or another may have installed, or ones that computer programs create for their own use. To access Python in a command line manner and access the packages you downloaded with Anaconda, you **need to use the Anaconda prompt, not the normal command prompt.** The regular command prompt does not know about the packages you downloaded in Anaconda and will not work correctly.
# 
# ## What packages do I absolutely need?
# 
# Here are some essentials for chemical engineering work:
# 
# - NumPy: Numerical Python. Arrays, matrices, numerical operations.
# - SciPy: Scientific algorithms like derivatives, optimization, etc.
# - MatPlotLib: The most basic plotting package.
# 
# Here are some others that can be very helpful:
# 
# - Pandas: Data structures that allow for data to be easily sorted, manipulated, imported, and exported.
# 
# ## Which Python programs will I use most when translating from MATLAB?
# 
# | MATLAB | Python |
# | :--- |:---|
# | matrices | numpy.array |
# | plot | matplotlib.pyplot |
# | function | def |
# | ode45 | scipy.integrate.solve_ivp(...method='RK45')|
# | fsolve | scipy.optimize.fsolve |
# | nlinfit | scipy.optimize.curve_fit |
# | fprintf | print |

# In[ ]:




