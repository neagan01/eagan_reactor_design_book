#!/usr/bin/env python
# coding: utf-8

# # Appendix Z: Creating your own Jupyter Book textbook
# 
# Here the procedure used to develop this textbook (created 2022-2023) is described. This was created on a Windows 10 machine. This is by no means the best way to do this, it is simply the way it was done here.
# 
# **Creating the book**
# 1. Install Anaconda from https://www.anaconda.com/
# 2. Create new Python 3.7 environment was created in Anaconda by going to the Environments tab and selecting "create". Call it "py37". This may help with Windows compatibility issues.
# 3. Run Anaconda Prompt (found in Programs/Anaconda3 (64-bit)/)
# 4. Load environment with "activate py37"
# 5. Install jupyter books with the command "conda install -c conda-forge jupyter-book". It may take a bit to successfully install.
# 6. Navigate to the folder where you will create your book--I did this in my GitHub folder and will refer to it as such throughout.
# 7. Create a template book with "jupyter-book create bookname"
# 8. Build the book with command "jupyter-book build bookname"
# 9. With an appropriate editor (e.g., Notebook++), modify your title and other details in the "_config.yml" file.
# 10. Move your book contents into the "bookname" folder.
# 11. Define the organization of your book by editing the "_toc.yml" file
# 12. Open book by navigating to "bookname/_build/html" and opening an html file to jump to that chapter of the book.
# 
# **Editing the book**
# After the book has been created, the content can be updated at any time but will not be instantly reflected in the book's html pages. **To update the book,** simply build it again by stepping out of the folder and using the command "jupyter-book build bookname."
# 
# **Making the book available online through GitHub**
# 1. Create a GitHub account if you have not already. You will create a username with it.
# 2. Create a new repository. It must be public, and you should have it generate a README file. Name it whatever you like; for this case, we will call it "book_draft"
# 3. In Anaconda, install "git" into your 3.7 environment.
# 4. In Anaconda prompt (3.7 environment), install the GitHub pages import tool with command "pip install ghp-import"
# 5. In Anaconda prompt (in 3.7), navigate to your GitHub folder (or whichever you prefer) and clone your repository. Do this by first finding the url of your repository which will be something like https://github.com/username/book_draft. In the prompt enter the command "git clone https://github.com/username/book_draft" or whatever URL is appropriate.
# 6. Copy the contents of the book you previously created into this folder. Assuming that you are in the GitHub folder and that both "bookname" and "book_draft" are as well, use the command "cp -r bookname/* book_draft/" to recursively (-r) copy (cp) all contents (star) in the bookname folder (bookname/) to your new repository (book_draft/).
# 7. Enter the book_draft folder. In it you should see a "_build" folder which holds your html files.
# 8. Enter the command "ghp-import -n -p -f _build/html" to create your book.
# 9. To find the url for your new book, first go to your repository online. Then click "settings" along the top bar under your repository location, then click "pages" along the left toolbar, and there you will see the url. Anyone can access your book at this link. **Note: it can take a few minutes to upload**
# 
# **Updating your book**
# You can upload a new version of your book at any time by rebuilding it as noted above and then re-importing it by again entering the main folder and using the command "ghp-import -n -p -f _build/html". Note that it can take a few minutes to update.

# ## Additional resources for building Jupyter notebooks and textbooks for chemical engineering courses
# 
# 1. Jupyter book current documentation: https://jupyterbook.org/en/stable/intro.html
# 2. Dominguez et al., 2021, Teaching chemical engineering using Jupyter notebook: Problem generators and lecturing tools. https://doi.org/10.1016/j.ece.2021.06.004
# 3. A useful video for generating a Jupyter textbook: https://www.youtube.com/watch?v=lZ2FHTkyaMU&list=PLqHWxCzYzDAZOZJ90O-biMvc54qoCTtOu&index=8
# 

# In[ ]:




