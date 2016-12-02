Title: Filter Out Columns
Slug: filter_out_columns
Summary: Filter columns out of dataset with different types of criteris.
Date: 2016-11-27 12:00
Category: wrangling_data
Tags:
Authors: Nate Hall

<a href="https://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/filter_out_columns.ipynb" target="_blank">Link to the full jupyter notebook.</a><br/>
<a href="https://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/filter_out_columns_code.ipynb" target="_blank">Link to the code only jupyter notebook.</a>

This is a slightly more complicated application of filtering out columns than the standard df.drop method you may have seen. But if you stick with each element I promise it will begin to make sense.


```python
import pandas as pd
```


```python
data = pd.read_csv('../data/billboard.csv')
df = pd.DataFrame(data)
df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist.inverted</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>date.entered</th>
      <th>date.peaked</th>
      <th>x1st.week</th>
      <th>x2nd.week</th>
      <th>x3rd.week</th>
      <th>...</th>
      <th>x67th.week</th>
      <th>x68th.week</th>
      <th>x69th.week</th>
      <th>x70th.week</th>
      <th>x71st.week</th>
      <th>x72nd.week</th>
      <th>x73rd.week</th>
      <th>x74th.week</th>
      <th>x75th.week</th>
      <th>x76th.week</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Destiny's Child</td>
      <td>Independent Women Part I</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>2000-09-23</td>
      <td>2000-11-18</td>
      <td>78</td>
      <td>63.0</td>
      <td>49.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 83 columns</p>
</div>



## Filter out columns that contain a keyword
Remember what method we use to drop columns or rows in a dataset? We will be using the same one again here. So we begin our function by saying...
```python
df.drop( )
```
Now remember in the <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html" target="_blank">documentation</a> what we can pass this method to drop? It says it can take on a "list-like" set of items to be dropped.
## Conceptualize what to filter
Conceptually lets lay out what we're trying to accomplish. We want the .drop method to get automatically populated with a list of columns that match some type of filter criteria. To get a list of columns that match a criteria we would use a for loop. However, that is too cumbersome to try to embed in the .drop method which is why <a href="https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions" target="_blank">list comprehensions</a> are very useful to be placed in arguments.
## Use list comprehension to return the columns to be dropped
Remember that list comprehensions you start by declaring what variable you will be getting and then go on to declare the function setup. For our example we're going to say give me all the columns that are in our dataframe if they have the number "6" in them. (No real reason behind 6 this is purely for example purposes). We put our comprehension in brackets since its returning a list and declare the first variable we're getting back "col".
```python
[col]
```
Next we need to give it the for loop (what we want it to look through). In this case we want it to give all the "col" values that match our filter so we say "for col in df.columns" since we're looking through all the columns.
```python
[col for col in df.columns]
```
Lastly, we get to delcare our filtering criteria, which we said was columns that have the number "6" in them. Note, that all the columns are strings so we need to put the 6 in quotations when declaring what to filter. At any rate, we are looking at all the "col" so we want all the ones if "6" is in them.
```python
[col for col in df.columns if "6" in col]
```
And that's it we have our filter setup with a easy logic filtering test to apply to all the columns. We can place this straight into the df.drop method and add the other arguments for the column axis and inplace being set to true so we apply this to our dataframe.


```python
df.drop([col for col in df.columns if "6" in col], axis=1, inplace=True)
#Check your work
df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist.inverted</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>date.entered</th>
      <th>date.peaked</th>
      <th>x1st.week</th>
      <th>x2nd.week</th>
      <th>x3rd.week</th>
      <th>...</th>
      <th>x55th.week</th>
      <th>x57th.week</th>
      <th>x58th.week</th>
      <th>x59th.week</th>
      <th>x70th.week</th>
      <th>x71st.week</th>
      <th>x72nd.week</th>
      <th>x73rd.week</th>
      <th>x74th.week</th>
      <th>x75th.week</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Destiny's Child</td>
      <td>Independent Women Part I</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>2000-09-23</td>
      <td>2000-11-18</td>
      <td>78</td>
      <td>63.0</td>
      <td>49.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 66 columns</p>
</div>



## Cool!
We see when we scroll over that all the columns from the sixties are removed and the ones like 56. Everything with a 6 is gone you powerful data scientist you.

## Filter out columns that start with "__"
Because we did a logical argument with the list comprehension the sky is the limit for what we want it to return. In the below example I am asking it to take it one step further and look at the first letter of all the columns, if the letter is an "x" then it should drop that column.


```python
df.drop([col for col in df.columns if col[:1] == 'x'], axis=1, inplace=True)
#Check your work
df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist.inverted</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>date.entered</th>
      <th>date.peaked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Destiny's Child</td>
      <td>Independent Women Part I</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>2000-09-23</td>
      <td>2000-11-18</td>
    </tr>
  </tbody>
</table>
</div>



## Bam!
You can now conquer any mangy dataset columns you come across.
