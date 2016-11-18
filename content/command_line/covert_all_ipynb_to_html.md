Title: Convert All Jupyter Notebooks In A Folder To Basic HTML Using Bash  
Date: 2016-05-01 12:00  
Category: Command Line  
Tags:  
Slug: covert_all_ipynb_to_html  
Authors: Chris Albon  
Summary: Convert All Jupyter Notebooks In A Folder To Basic HTML Using Bash  

_Note: This code has been commented out. To run the code, remove the comments._


```python
# %%bash
# #!/bin/bash

# sets the working directory to the current directory
# acd "$(dirname "$0")"

# converts all Jupyter Notebook files to basic html
# for f in *.ipynb; do jupyter nbconvert --to html --template basic $f; done
```

    [NbConvertApp] Converting notebook covert_all_ipynb_to_html.ipynb to html
    [NbConvertApp] Writing 2632 bytes to covert_all_ipynb_to_html.html
    [NbConvertApp] Converting notebook list_all_files_and_folders_in_a_directory.ipynb to html
    [NbConvertApp] Writing 2153 bytes to list_all_files_and_folders_in_a_directory.html
    [NbConvertApp] Converting notebook open_ipython_nb_in_nondefault_browser.ipynb to html
    [NbConvertApp] Writing 1552 bytes to open_ipython_nb_in_nondefault_browser.html
