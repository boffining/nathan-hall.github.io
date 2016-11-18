Title: List All Files And Folders In A Directory
Date: 2016-05-01 12:00
Category: Command Line
Tags:
Slug: list_all_files_and_folders_in_a_directory
Authors: Chris Albon
Summary: List All Files And Folders In A Directory

```python
%%bash --out output
# Line above: Run bash, with the output being a python variable called 'output'

# Change the working directory to the current directory
cd "$(dirname "$0")"

# For all filenames, print the filename, then end
for f in *; do echo "$f"; done
```


```python
# Print the variable with the filenames
print(output)
```

    list_all_files_and_folders_in_a_directory.ipynb
