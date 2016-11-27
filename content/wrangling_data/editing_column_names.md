Title: Editing Column Names 
Slug: editing_column_names
Summary: Either renaming all columns, replacing values in some column names, or changing the name of one column.
Date: 2016-11-27 12:00
Category: wrangling_data
Tags:
Authors: Nate Hall

<a href='http://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/editing_column_names.ipynb'>Link to the full jupyter notebook.</a><br/>
<a href='http://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/wrangling_data/editing_column_names_code.ipynb'>Link to the code only jupyter notebook.</a>

In this example we'll be working with the billboard hot 100 dataset. The overall structure of this dataset could be setup better for what we need to do with some interesting correlations so we'll be using it for a lot of dataset manipulation examples.

One method for organizing a data table is for each row to represent the "lowest level" of data available. Here we have each row representing a song, but if you notice the column names there is one for each week. And if you look at the shape of our data we have 83 columns total. Can you guess what the lowest level of data really is for this dataset then?


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



### Lowest level of data as rows.
If you guessed the lowest level would be each a pair combo of each week for each song then you'd be correct.
##### Goal: To get each row to represent the week performance of a song.

## 1. Get the week performance column names to be just numbers
This will allow us to convert them into integers and sort them later.
Now its as easy as looking for the things that are in those week columns that are not numbers and removing them.
We will take all our edits and apply them to the "df.columns" variable. This will overwrite the column names in our dataframe.
```python
df.columns =
```
Since df.columns is a list of column names we have to pass it a list back so we start our function with brackets.
```python
df.columns = [ ]
```
### Remove values with .replace
Next we get to say what we want to happen to the list we are going to pass back to df.column to replace its current list of column names. One way to remove values and get down to numbers is to replace the values with just blanks and thereby remove the values. So we use the "col.replace" method to define what values in the column header list we're going to replace.
```python
df.columns = [col.replace( )
```
Now we get to tell df.columns what we want its new names to be. So what do you think is the first thing we can remove? It looks like ".week" is on every column name so lets take that out and see what we have left.
NOTE: We are using a list comprehension so the values at the beginning of the list are what we will get back. In this case it will be all the columns in df.columns but with the ".week" removed(replaced with blanks).
```python
df.columns = [col.replace('.week', '') for col in df.columns]
```
Cool! That's gone now what? What's the next thing to be removed? Looks, like they all have "x" in front of them (for whatever reason...). Lets replace that with blanks.
```python
df.columns = [col.replace('.week', '') for col in df.columns]
df.columns = [col.replace('x', '') for col in df.columns]
```
Now we're getting somewhere. We are just left with the values that come after the 1, 2, 3, and 4. This part might be tedious but since from 4 onward every value ends with a "th" it's not too bad. So we run the list comprehension another four times to replace these values with blanks.


```python
df.columns = [col.replace('.week', '') for col in df.columns]
df.columns = [col.replace('x', '') for col in df.columns]
df.columns = [col.replace('st', '') for col in df.columns]
df.columns = [col.replace('nd', '') for col in df.columns]
df.columns = [col.replace('rd', '') for col in df.columns]
df.columns = [col.replace('th', '') for col in df.columns]
```

Check your work to make sure it worked as expected. You only need to load one row since we are looking at columns.


```python
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



## Success!!!! Or... so it seems...
Can you spot the one thing we inadvertedly did by focusing on the number values and running our replace method across the entire column header list?

It looks like the "artist.inverted" column name had the "st" removed when we applied our replace function to remove the value after the 1.

Luckily this is easily fixable and introduces us to another useful column editing method called ".rename".

## 2. Fix the "artist.inverted" column name
This is powerful function that we will use again in other contexts. But for columns it is very useful. Remember that dictionaries contain a key and a value. For this application we are telling pandas to go through all our columns and find the ones that match the "key" in our dictionary and when it does to replace it with the "value" in our dictionary. So this is less flexible than other dictionaries but very useful for our applications.

The .rename method can be applied to both rows and columns so it actually goes with the entire datafarme instead of just the columns like the .replace function we used earlier. It also is different because it doesn't have to be used with a list comprehension it takes arguments that can be found in the <a href='http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html'>pandas documentation here.</a>

So we start by applying the .rename method to the dataframe and add ( ) at the end because it takes arguments.
```python
df.rename()
```
What do you think we should pass to it as an argument? If you look at the pandas documentation you'll see all kinds of things you can make the .rename() method do.
For our application we're going to pass it a dictionary like list of column names. So we use the columns= argument.
```python
df.rename(columns=)
```
Remember we're passing it a dictionary like list. So we don't use brackets [ ] like normal lists. It has to be the dictionary brackets { }.
```python
df.rename(columns={ })
```
Now we tell the rename method which columns to look for by giving it "keys".
```python
df.rename(columns={'arti.inverted': })
```
Then all we have to do is say what we want to change the column name to. To make the nameing scheme simpler we'll make it be just "artist".


```python
#The [:1] is slicing this data to only load one row since we're just interested in columns right now.
#Notice it gives the same result as the df.head(1) we used earlier.

df.rename(columns={'arti.inverted':'artist'})[:1]
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



Check your work to make sure it applied like you expect.


```python
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



## Huh? What happened? Why isn't it changed?
Like all debugging, lets backtrack. What happens when you run the code without the df.head() after it.


```python
df.rename(columns={'arti.inverted':'artist'})[:1]
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



## Ok, it works then, what's going on?
Pandas is a very smart and powerful tool. Notice when we first used the .replace function we were applying it to the df.columns variable. This was physically changing the list that was already at that variable and writing over it with a new list that we gave it.
Do you see any of that type of thing happening with the .rename() method? Are we writing over something as explicitly as redeclaring a variable?
Because pandas does not see you declaring something so explicitly it assumes(BY DEFAULT) that you are not intending to apply the change to the original dataframe and are just interested in running the function in a sort of alternate dimension dataframe.
##### Wait... I thought you said it was smart? That doesn't sound very smart...
What would happen if pandas over wrote everything you did and you wanted to do something either as an experiment or as a step in a process? You would have to COPY the entire dataset A LOT. And some of these things can get really big. So instead it creates this one alternate universe result of the method and you get to decide if you want to use it to overwrite the current dataframe or use it as an experiment or step in process with a no harm no foul safety net. Neat huh?

## Use the inplace argument
To get every method that can be applied to a dataframe object to write over the existing dataframe you have to say that you want inplace=True (it defaults to False). This will write over your original dataframe in the place where you apply a method and argument to it.

## 2a. Fix the arti.inverted column with inplace=True


```python
df.rename(columns={'arti.inverted':'artist'}, inplace=True)
```

Now, check your work again.


```python
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



## Yay! Success!!!


## BONUS: You can rename more than one column at a time.
Note that we removed the "." from "artist.inverted" when we renamed it. However, "date.entered" and "date.peaked" still have them. From what we know about dictionaries that have have many keys and values so why not simply add a comma after the first key value pair and then type in another one?


```python
df.rename(columns={'date.entered':'entered', 'date.peaked':'peaked'}, inplace=True)
```

Check your work and see what happens.


```python
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



## Success!! Way to go!
