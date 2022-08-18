#!/usr/bin/env python
# coding: utf-8

# # Appendix C: Creating interactive environments through Binder

# ## Interactive web-hosted environments
# 
# To run a code, the correct environment must be available. To ensure that this is the case, an internet-hosted environment can be created and accessed by anyone with the right link. There are several options for such environments including (but not limited to):
# - Binder
# - Google Colab
# - Kaggle Kernels
# 
# I could go over the pros and cons of these, but I don't feel like it right now. Instead I'll just talk about Binder because it's what I have used the most.
# 
# The pros of Binder include that it's free, it has easy integration with GitHub and JupyterBooks, and it opens up your notebooks in a JupyterLab environment, making it easy to work with. The cons include the limited RAM (2 GB) and its tendency to time out in 5 minutes of inactivity. It is therefore meant primarily for active use. Binder environments can be accessed and used on many different devices, including cell phones!
# 
# ## Creating a Binder environment
# 
# If you have not already, start by making a (free) GitHub account and download the desktop client.
# 
# 1. In the online version of GitHub, create a new repository. Give it a name (e.g., my_binder_environment), set it to be public,  check off "Add a README file," and click, "Create repository."
# 
# 2. In the desktop verion, clone this repository to your desktop.
# 
# 3. Make changes to the cloned repository on your desktop as you see fit.
# 
# 4. Create a document in the repository entitled "requirements.txt" and enter the programs you want included and (optionally) version numbers. For example: \
# numpy==1.18.1 \
# matplotlib==3.1.3 \
# scipy==1.4.1 \
# pandas==1.0.1 
# 
# 4. When you want changes to be pushed to the online, publically-available version, open the desktop app, press "commit to main" to put these in your main branch, and then press "Push origin" to send them online. The online repository will then be udpated.
# 
# 5. Go to mybinder.org to create your binder environment. Input the repository location next to where it says "GitHub." This should be something like username/my_repo.
# 
# 6. Press "Launch" to create the environment. Whenever large changes are made to the repository, the first build after these changes may take a while. Subsequent access of a "built" environment will be substantially faster.
# 
# 7. Access the binder environment at the link provided, which should be something like: https://mybinder.org/v2/gh/username/my_repo/HEAD. Note that you can actually skip steps 5 and 6 by directly entering this URL, which will force Binder to try to create the environment.
# 
# 8. To make it easy to access this Binder directly from the GitHub repo page, consider adding the following to your README.md file:
# 
# <pre>
# Click the button below to access these files in an online JupyterLab environment.
# 
# [![Binder:master](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/username/my_repo/HEAD)</pre>
# 
# For further details, you may start with the "Zero-to-Binder" link on mybinder.org.

# In[ ]:




