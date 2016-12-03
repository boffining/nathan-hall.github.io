Title: How To: Unpivot Columns
Slug: unpivot_columns
Summary: Reverse pivot columns to be added as new rows in a dataframe.
Date: 2016-11-27 12:00
Category: how_to
Tags:
Authors: Nate Hall

<a href="http://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/unpivoting_columns.ipynb" target="_blank">Link to the full jupyter notebook.</a><br/>
<a href="https://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/unpivoting_columns_code.ipynb" target="_blank">Link to the code only jupyter notebook.</a>

- We'll be using the billboard hot 100 dataset as the example.
- We wanted to get the dataset to have rows representing the lowest level of data possible.
- <a href="./editing_column_names.html", target="_blank">We cleaned up the column names in this article.</a>
- Now to finish the the final step to accomplish the goal below.
## Goal: To get each row to represent the week performance of a song.


```python
import pandas as pd
```


```python
data = pd.read_csv('../data/billboard_weeks_edited.csv')
df = pd.DataFrame(data)
df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>entered</th>
      <th>peaked</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>...</th>
      <th>67</th>
      <th>68</th>
      <th>69</th>
      <th>70</th>
      <th>71</th>
      <th>72</th>
      <th>73</th>
      <th>74</th>
      <th>75</th>
      <th>76</th>
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




```python
#Check the shape of the dataset we're starting with.
df.shape
```




    (317, 83)



We know that we have 317 rows and 83 columns. If we are "unpivoting" this to be fewer columns we can expect the rows to increase substantially. Remember this for when we check the shape again later.

## Melt its face off!
We will use the ".melt" function to accomplish what we need for this dataset. More information on it can be found in the <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html", target="_blank"> documentation here.</a>

### Notes on pd.melt
First off we see that it is not applied to a dataframe, so we don't do "df.melt" it actually gets passed the entire dataframe object as an argument and is called by starting with "pd."
```python
pd.melt(df)
```

## Create a new dataframe
Simply for the ease of still being able to track back to our original csv in case something doesn't work. We will then declare a new dataframe that will take on the results of the pd.melt( ) function.
```python
df2 = pd.melt(df)
```

## id_vars=[ ]
We already passed the dataframe. The id_vars argument will be the columns that will be retained in the dataframe so we'll declare that by listing the columns we want to keep. Note that this argument is taking on a list so we can pass the columns to it with all the columns list methods that we know. For this example i'll just list out the columns since there are so few.
```python
df2 = pd.melt(df, id_vars=['year', 'artist', 'track', 'time', 'genre', 'entered', 'peaked'])
```
## value_vars=[ ]
This argument says it is for stating all the columns to "unpivot". Phew, we have a lot of weeks... do we have to list them all? That's the beauty of this function. If we simply leave this blank it will default to unpivot all of the columns that are not listed in the "id_vars=[ ]" argument. SWEET!!!
## var_name=[ ]
So we have this tricky thing to do with unpivoting... we'll have all the week columns get turned into row cells and they will need a column header. To do this we declare the "var_name=[ ]" argument with the column header we want.
```python
df2 = pd.melt(df, id_vars=['year', 'artist', 'track', 'time', 'genre', 'entered', 'peaked'], var_name='week')
```
## value_name[ ]
Now what about all the values that are listed in each week column right now? Where are those supposed to go? Glad you asked that. These are the values that we are "unpivoting" but they to will need a column header since we just took the week columns away. We know that those values represent the weekly ranking of a song during that week so we'll "unpivot" those values to a new column called "rank"


```python
df2 = pd.melt(df, id_vars=['year', 'artist', 'track', 'time', 'genre', 'entered', 'peaked'],
              var_name='week', value_name='rank')
```

Check your work.


```python
df2.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>entered</th>
      <th>peaked</th>
      <th>week</th>
      <th>rank</th>
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
      <td>1</td>
      <td>78.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>Santana</td>
      <td>Maria, Maria</td>
      <td>4:18</td>
      <td>Rock</td>
      <td>2000-02-12</td>
      <td>2000-04-08</td>
      <td>1</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>Savage Garden</td>
      <td>I Knew I Loved You</td>
      <td>4:07</td>
      <td>Rock</td>
      <td>1999-10-23</td>
      <td>2000-01-29</td>
      <td>1</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>Madonna</td>
      <td>Music</td>
      <td>3:45</td>
      <td>Rock</td>
      <td>2000-08-12</td>
      <td>2000-09-16</td>
      <td>1</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>Aguilera, Christina</td>
      <td>Come On Over Baby (All I Want Is You)</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>2000-08-05</td>
      <td>2000-10-14</td>
      <td>1</td>
      <td>57.0</td>
    </tr>
  </tbody>
</table>
</div>



## Cool! It worked!
We now have the rows representing the lowest level of data in our dataset. What did this do to the shape of our table? Remember what it was at the beginning? Lets check it again to see what happened.


```python
df2.shape
```




    (24092, 9)



## Woah. That is MUCH longer.
Nothing to worry about though. You'll find that pandas can handle this length of a data table easily. Most importantly we have our dataset setup in a way where we can work with it much better.
