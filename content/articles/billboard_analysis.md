Title: Billboard Hot 100 Analysis
Date: 2016-11-23 12:00
Category: Articles
Tags: Article
Slug: billboard_analysis
Authors: Nate Hall
Summary: What genres and artists are most correlated in rankings?


##Here is some open ended analysis using pandas to show the power of this library for handling literally anything that can be thrown at it.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

### Pandas to read in data


```python
data = pd.read_csv('../data/billboard.csv')
df = pd.DataFrame(data)
df.head()
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
    <tr>
      <th>1</th>
      <td>2000</td>
      <td>Santana</td>
      <td>Maria, Maria</td>
      <td>4:18</td>
      <td>Rock</td>
      <td>2000-02-12</td>
      <td>2000-04-08</td>
      <td>15</td>
      <td>8.0</td>
      <td>6.0</td>
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
    <tr>
      <th>2</th>
      <td>2000</td>
      <td>Savage Garden</td>
      <td>I Knew I Loved You</td>
      <td>4:07</td>
      <td>Rock</td>
      <td>1999-10-23</td>
      <td>2000-01-29</td>
      <td>71</td>
      <td>48.0</td>
      <td>43.0</td>
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
    <tr>
      <th>3</th>
      <td>2000</td>
      <td>Madonna</td>
      <td>Music</td>
      <td>3:45</td>
      <td>Rock</td>
      <td>2000-08-12</td>
      <td>2000-09-16</td>
      <td>41</td>
      <td>23.0</td>
      <td>18.0</td>
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
    <tr>
      <th>4</th>
      <td>2000</td>
      <td>Aguilera, Christina</td>
      <td>Come On Over Baby (All I Want Is You)</td>
      <td>3:38</td>
      <td>Rock</td>
      <td>2000-08-05</td>
      <td>2000-10-14</td>
      <td>57</td>
      <td>47.0</td>
      <td>45.0</td>
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
<p>5 rows × 83 columns</p>
</div>



### Renaming column names


```python
df.columns = [col.replace('.week', '') for col in df.columns]
df.columns = [col.replace('x', '') for col in df.columns]
df.columns = [col.replace('st', '') for col in df.columns]
df.columns = [col.replace('nd', '') for col in df.columns]
df.columns = [col.replace('rd', '') for col in df.columns]
df.columns = [col.replace('th', '') for col in df.columns]
#df.columns = ufo.columns.str.replace(' ', '_')
```

### Describe your data: check the value counts + descrisptive stats


```python
#We will first drop 'year' since all the songs are from 2000
df.drop('year', axis=1, inplace=True)
#basic describe
df.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
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
      <th>count</th>
      <td>317.000000</td>
      <td>312.000000</td>
      <td>307.000000</td>
      <td>300.000000</td>
      <td>292.000000</td>
      <td>280.000000</td>
      <td>269.000000</td>
      <td>260.000000</td>
      <td>253.000000</td>
      <td>244.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>79.958991</td>
      <td>71.173077</td>
      <td>65.045603</td>
      <td>59.763333</td>
      <td>56.339041</td>
      <td>52.360714</td>
      <td>49.219331</td>
      <td>47.119231</td>
      <td>46.343874</td>
      <td>45.786885</td>
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
    <tr>
      <th>std</th>
      <td>14.686865</td>
      <td>18.200443</td>
      <td>20.752302</td>
      <td>22.324619</td>
      <td>23.780022</td>
      <td>24.473273</td>
      <td>25.654279</td>
      <td>26.370782</td>
      <td>27.136419</td>
      <td>28.152357</td>
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
    <tr>
      <th>min</th>
      <td>15.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>5.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
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
    <tr>
      <th>25%</th>
      <td>74.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
    <tr>
      <th>50%</th>
      <td>81.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
    <tr>
      <th>75%</th>
      <td>91.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
    <tr>
      <th>max</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>99.000000</td>
      <td>100.000000</td>
      <td>99.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
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
<p>8 rows × 76 columns</p>
</div>




```python
df2 = pd.melt(df, id_vars=['arti.inverted', 'track', 'time', 'genre', 'date.entered','date.peaked'],
                  var_name='week', value_name='rank')
```


```python
#checking function that was run
print df2.shape
print df2.columns
```

    (24092, 8)
    Index([u'arti.inverted', u'track', u'time', u'genre', u'date.entered',
           u'date.peaked', u'week', u'rank'],
          dtype='object')



```python
#We now the data formated to plot ranking over time for each track.
#We will use other methods to determine which tracks to plot.
df3 = df2[df2['track'] == 'I Wanna Know']
plt.plot(df3['rank'])
plt.ylabel('Weekly Rank')
plt.axis([0,18000,100, 0])
plt.show()
```

![png]({filename}/images/billboard_100/output_11_0.png)


#### Future Exploratory options... the world is yours with pandas.
- Look at time it takes to get to the top. (time entered, to time peak)
- Also add a column called time in top 100.
- Compare the three columns.

### That was interesting... now lets wrangle this dataset for some cool correlations.

# Data wrangling for the most correlated genres


```python
#create a new dataframe for manipulation.
df7 = df2
```

### Group the data


```python
df7 = df7.groupby(['week' , 'genre'], as_index=False).mean()
#check that the group by function worked.
df7.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>week</th>
      <th>genre</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Country</td>
      <td>82.405405</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Electronica</td>
      <td>84.500000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Gospel</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Jazz</td>
      <td>89.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Latin</td>
      <td>73.222222</td>
    </tr>
  </tbody>
</table>
</div>



### Create a pivot table


```python
#Use the pivot table function to get to something that can be correlated.
df7 = df7.pivot(index='week', columns='genre', values='rank')
```


```python
#Moving the week column from the index back into a column position on the data table.
df7.reset_index(inplace=True)
df7.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>genre</th>
      <th>week</th>
      <th>Country</th>
      <th>Electronica</th>
      <th>Gospel</th>
      <th>Jazz</th>
      <th>Latin</th>
      <th>Pop</th>
      <th>R&amp;B</th>
      <th>Rap</th>
      <th>Reggae</th>
      <th>Rock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>82.405405</td>
      <td>84.500000</td>
      <td>76.0</td>
      <td>89.0</td>
      <td>73.222222</td>
      <td>79.222222</td>
      <td>84.086957</td>
      <td>85.172414</td>
      <td>72.0</td>
      <td>76.116788</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>52.377049</td>
      <td>55.750000</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>43.250000</td>
      <td>43.571429</td>
      <td>63.866667</td>
      <td>53.380952</td>
      <td>75.0</td>
      <td>35.895238</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11</td>
      <td>51.016949</td>
      <td>53.250000</td>
      <td>66.0</td>
      <td>NaN</td>
      <td>49.625000</td>
      <td>50.142857</td>
      <td>62.538462</td>
      <td>52.538462</td>
      <td>84.0</td>
      <td>36.048077</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>50.714286</td>
      <td>59.750000</td>
      <td>68.0</td>
      <td>NaN</td>
      <td>35.285714</td>
      <td>58.250000</td>
      <td>67.000000</td>
      <td>50.000000</td>
      <td>92.0</td>
      <td>33.734694</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>52.301887</td>
      <td>49.333333</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>39.285714</td>
      <td>58.333333</td>
      <td>59.666667</td>
      <td>53.235294</td>
      <td>85.0</td>
      <td>34.125000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Sorting the data inside week after it is converted to a string.
df7['week'] = df7.week.astype(int)
df7.sort('week')
df7.head()
```

    /anaconda/lib/python2.7/site-packages/ipykernel/__main__.py:3: FutureWarning: sort(columns=....) is deprecated, use sort_values(by=.....)
      app.launch_new_instance()





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>genre</th>
      <th>week</th>
      <th>Country</th>
      <th>Electronica</th>
      <th>Gospel</th>
      <th>Jazz</th>
      <th>Latin</th>
      <th>Pop</th>
      <th>R&amp;B</th>
      <th>Rap</th>
      <th>Reggae</th>
      <th>Rock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>82.405405</td>
      <td>84.500000</td>
      <td>76.0</td>
      <td>89.0</td>
      <td>73.222222</td>
      <td>79.222222</td>
      <td>84.086957</td>
      <td>85.172414</td>
      <td>72.0</td>
      <td>76.116788</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>52.377049</td>
      <td>55.750000</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>43.250000</td>
      <td>43.571429</td>
      <td>63.866667</td>
      <td>53.380952</td>
      <td>75.0</td>
      <td>35.895238</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11</td>
      <td>51.016949</td>
      <td>53.250000</td>
      <td>66.0</td>
      <td>NaN</td>
      <td>49.625000</td>
      <td>50.142857</td>
      <td>62.538462</td>
      <td>52.538462</td>
      <td>84.0</td>
      <td>36.048077</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>50.714286</td>
      <td>59.750000</td>
      <td>68.0</td>
      <td>NaN</td>
      <td>35.285714</td>
      <td>58.250000</td>
      <td>67.000000</td>
      <td>50.000000</td>
      <td>92.0</td>
      <td>33.734694</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>52.301887</td>
      <td>49.333333</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>39.285714</td>
      <td>58.333333</td>
      <td>59.666667</td>
      <td>53.235294</td>
      <td>85.0</td>
      <td>34.125000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Remove the pesky column and index names that will mess up the correlation formula later.
df7.index.name = None
df7.columns.name = None
```


```python
#Remove the week column since we sorted by it already.
df7.drop('week', inplace=True, axis=1)
```


```python
df7.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Electronica</th>
      <th>Gospel</th>
      <th>Jazz</th>
      <th>Latin</th>
      <th>Pop</th>
      <th>R&amp;B</th>
      <th>Rap</th>
      <th>Reggae</th>
      <th>Rock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>82.405405</td>
      <td>84.500000</td>
      <td>76.0</td>
      <td>89.0</td>
      <td>73.222222</td>
      <td>79.222222</td>
      <td>84.086957</td>
      <td>85.172414</td>
      <td>72.0</td>
      <td>76.116788</td>
    </tr>
    <tr>
      <th>1</th>
      <td>52.377049</td>
      <td>55.750000</td>
      <td>59.0</td>
      <td>NaN</td>
      <td>43.250000</td>
      <td>43.571429</td>
      <td>63.866667</td>
      <td>53.380952</td>
      <td>75.0</td>
      <td>35.895238</td>
    </tr>
    <tr>
      <th>2</th>
      <td>51.016949</td>
      <td>53.250000</td>
      <td>66.0</td>
      <td>NaN</td>
      <td>49.625000</td>
      <td>50.142857</td>
      <td>62.538462</td>
      <td>52.538462</td>
      <td>84.0</td>
      <td>36.048077</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50.714286</td>
      <td>59.750000</td>
      <td>68.0</td>
      <td>NaN</td>
      <td>35.285714</td>
      <td>58.250000</td>
      <td>67.000000</td>
      <td>50.000000</td>
      <td>92.0</td>
      <td>33.734694</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52.301887</td>
      <td>49.333333</td>
      <td>61.0</td>
      <td>NaN</td>
      <td>39.285714</td>
      <td>58.333333</td>
      <td>59.666667</td>
      <td>53.235294</td>
      <td>85.0</td>
      <td>34.125000</td>
    </tr>
  </tbody>
</table>
</div>



# Data wrangling for the most correlated artist rankings


```python
df8 = df2
```

### Group the data


```python
df8 = df8.groupby(['week' , 'arti.inverted'], as_index=False).mean()
df8.shape
```




    (17328, 3)




```python
df8 = df8[np.isfinite(df8['rank'])]
df8.shape
```




    (3989, 3)




```python
counts = df8['arti.inverted'].value_counts()
```


```python
##Removing any artists that have less than 15 datapoints on the rankings.
df8 = df8[df8['arti.inverted'].isin(counts[counts > 30].index)]
```

### Create a pivot table


```python
df8 = df8.pivot(index='week', columns='arti.inverted', values='rank')
```


```python
#Moving the week column from the index back into a column position on the data table.
df8.reset_index(inplace=True)
```


```python
#Sorting the data inside week after it is converted to a string.
df8['week'] = df8.week.astype(int)
df8.sort('week')
df8.head()
```

    /anaconda/lib/python2.7/site-packages/ipykernel/__main__.py:3: FutureWarning: sort(columns=....) is deprecated, use sort_values(by=.....)
      app.launch_new_instance()





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>arti.inverted</th>
      <th>week</th>
      <th>3 Doors Down</th>
      <th>Aaliyah</th>
      <th>Anthony, Marc</th>
      <th>BBMak</th>
      <th>Braxton, Toni</th>
      <th>Creed</th>
      <th>Destiny's Child</th>
      <th>Hill, Faith</th>
      <th>Joe</th>
      <th>Jordan, Montell</th>
      <th>Lonestar</th>
      <th>Nelly</th>
      <th>Pink</th>
      <th>Savage Garden</th>
      <th>Vertical Horizon</th>
      <th>matchbox twenty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>78.5</td>
      <td>71.5</td>
      <td>79.5</td>
      <td>99.0</td>
      <td>79.0</td>
      <td>82.5</td>
      <td>78.333333</td>
      <td>82.0</td>
      <td>85.5</td>
      <td>92.0</td>
      <td>82.666667</td>
      <td>100.0</td>
      <td>55.0</td>
      <td>73.0</td>
      <td>67.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>56.0</td>
      <td>23.0</td>
      <td>44.5</td>
      <td>18.0</td>
      <td>21.0</td>
      <td>65.5</td>
      <td>12.333333</td>
      <td>49.0</td>
      <td>53.0</td>
      <td>24.0</td>
      <td>33.333333</td>
      <td>36.0</td>
      <td>11.5</td>
      <td>16.5</td>
      <td>22.5</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11</td>
      <td>56.0</td>
      <td>23.0</td>
      <td>43.0</td>
      <td>19.0</td>
      <td>27.0</td>
      <td>63.5</td>
      <td>10.333333</td>
      <td>42.0</td>
      <td>52.5</td>
      <td>24.0</td>
      <td>33.000000</td>
      <td>37.0</td>
      <td>10.0</td>
      <td>19.0</td>
      <td>20.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>55.0</td>
      <td>22.5</td>
      <td>43.5</td>
      <td>15.0</td>
      <td>29.0</td>
      <td>68.0</td>
      <td>7.666667</td>
      <td>46.0</td>
      <td>54.5</td>
      <td>20.0</td>
      <td>31.666667</td>
      <td>30.0</td>
      <td>11.0</td>
      <td>22.5</td>
      <td>19.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>54.0</td>
      <td>22.0</td>
      <td>50.0</td>
      <td>18.0</td>
      <td>32.0</td>
      <td>70.5</td>
      <td>2.666667</td>
      <td>55.5</td>
      <td>54.0</td>
      <td>19.0</td>
      <td>35.000000</td>
      <td>23.0</td>
      <td>12.0</td>
      <td>25.0</td>
      <td>19.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Remove the pesky column and index names that will mess up the correlation formula later.
df8.index.name = None
df8.columns.name = None
```


```python
#Remove the week column since we sorted by it already.
df8.drop('week', inplace=True, axis=1)
```

# Data wrangling for the most correlated song rankings

How would you do this part?


```python
#df9 = df2
```

## Run a correlation function on the dataframes from the wrangling steps.
This is a simple formula that I have been working to improve to work on any data set. It is designed to be a useful alternative to the spray and pray sns.pairplot or scatter matrix methods.
sns.pairplot (on df7) = 14s
corrr_pairs function (on df7) =384ms


```python
def corr_pairs(df_input,coef_percentile): #,mse_percentile
    #from sklearn.metrics import mean_squared_error
    #Get top correlated pairs using Pearson coefficient
    c = df_input.corr()
    s = c.unstack()
    so = s.sort_values(kind="quicksort")
    df_output = pd.DataFrame(so.abs(), columns=['coef'])
    df_output = df_output.reset_index()
    df_output.drop_duplicates('coef', inplace=True)
    df_output.dropna(inplace=True)
    #df_input = df_input.fillna(0.0)
    #Get mean squared error for better accuracy
    #mse_l = []
    #for i in range(len(df_output.iloc[:,0:2])):
        #mse_var = mean_squared_error(df_input[df_output.iloc[i,0]], df_input[df_output.iloc[i,1]])
        #mse_l.append(mse_var)
    #df_output['mse'] = mse_l
    #Filter the results by both Coefficient and MSE for best pairs.
    df_output = df_output[(df_output['coef'] < 1) & (df_output.coef > np.percentile(df_output['coef'],coef_percentile))] #& (df_output.mse < np.percentile(df_output['mse'],mse_percentile))]
    #Plot the best pairs.
    for i in range(len(df_output.iloc[:,0:2])):
        colors = ['r', 'b']
        plt.scatter(df_output.iloc[i,0],df_output.iloc[i,1], data=df_input, c=colors)
        plt.xlabel(df_output.iloc[i,0])
        plt.ylabel(df_output.iloc[i,1])
        plt.legend()
        plt.show()
    return df_output
```

## Showing the most correlated genres in the rankings


```python
corr_pairs(df7, 95)
```

![png]({filename}/images/billboard_100/output_44_0.png)


![png]({filename}/images/billboard_100/output_44_1.png)





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>level_0</th>
      <th>level_1</th>
      <th>coef</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>86</th>
      <td>Electronica</td>
      <td>Country</td>
      <td>0.848179</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Electronica</td>
      <td>R&amp;B</td>
      <td>0.913870</td>
    </tr>
  </tbody>
</table>
</div>



## Showing the most correlated artists in the rankings


```python
corr_pairs(df8, 95)
```

![png]({filename}/images/billboard_100/output_46_0.png)


![png]({filename}/images/billboard_100/output_46_1.png)


![png]({filename}/images/billboard_100/output_46_2.png)


![png]({filename}/images/billboard_100/output_46_3.png)


![png]({filename}/images/billboard_100/output_46_4.png)





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>level_0</th>
      <th>level_1</th>
      <th>coef</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>230</th>
      <td>Creed</td>
      <td>Joe</td>
      <td>0.909992</td>
    </tr>
    <tr>
      <th>232</th>
      <td>Savage Garden</td>
      <td>Aaliyah</td>
      <td>0.949246</td>
    </tr>
    <tr>
      <th>234</th>
      <td>BBMak</td>
      <td>matchbox twenty</td>
      <td>0.954013</td>
    </tr>
    <tr>
      <th>236</th>
      <td>matchbox twenty</td>
      <td>Destiny's Child</td>
      <td>0.965130</td>
    </tr>
    <tr>
      <th>238</th>
      <td>Destiny's Child</td>
      <td>BBMak</td>
      <td>0.982112</td>
    </tr>
  </tbody>
</table>
</div>



## Showing the most correlated songs in the rankings

How would you do this part?
