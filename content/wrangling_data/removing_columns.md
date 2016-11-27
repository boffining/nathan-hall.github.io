Title: Removing Columns
Slug: removing_columns
Summary: Removing columns and all their associated values.
Date: 2016-11-27 12:00
Category: wrangling_data
Tags:
Authors: Nate Hall

<a href="https://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/removing_columns.ipynb" target="_blank">Link to the full jupyter notebook.</a><br/>
<a href="https://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/removing_columns_code.ipynb" target="_blank">Link to the code only jupyter notebook.</a>

This is a quick introduction to some basic methods for removing columns from a dataset. We will use the billboard hot 100 dataset as an example.


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



## Drop a column
The simplest way to remove a column is with the "df.drop" method from pandas. <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html" target="_blank">See more info at the documentation here.</a>

We specify what dataframe to apply the .drop method. Then we tell it if we're dropping a column or row with the "axis" argument. And finally we use the "inplace" argument to either create the results in an alternate universe or apply it back to our current dataframe.


```python
#Can you guess why I am dropping this column? Its not just for an example. See if you can figure it out.
df.drop('year', axis=1, inplace=True)
df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>entered</th>
      <th>peaked</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
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
      <td>Destiny's Child</td>
      <td>Independent Women Part I</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>2000-09-23</td>
      <td>2000-11-18</td>
      <td>78</td>
      <td>63.0</td>
      <td>49.0</td>
      <td>33.0</td>
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
<p>1 rows × 82 columns</p>
</div>



## Drop multiple columns
Notice that for the "labels" argument in the documentation it says that the elements to drop can be "list-like". Which means that if we want to drop multiple columns we can give it a list of column names since that is how all the column headers are stored in pandas anyways. So the function would be...


```python
#This time we are doing it for example purposes only so note that inplace is set to False to make this abundantly clear.
#It defaults to False automatically but this makes it clear we are not applying it to the original dataframe.

df.drop(['entered', 'peaked'], axis=1, inplace=False)[:1]

#note we aren't using df.head to see how it works. Because df.head shows the original dataframe values.
#since we are not applying this to the original dataframe we can slice the results to show the first row
#only and that acts the same as using df.head(1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>artist</th>
      <th>track</th>
      <th>time</th>
      <th>genre</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
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
      <td>Destiny's Child</td>
      <td>Independent Women Part I</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>78</td>
      <td>63.0</td>
      <td>49.0</td>
      <td>33.0</td>
      <td>23.0</td>
      <td>15.0</td>
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
<p>1 rows × 80 columns</p>
</div>
