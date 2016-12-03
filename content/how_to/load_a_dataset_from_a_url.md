Title: How To: Load A Dataset from A URL
Slug: load_a_dataset_from_a_url
Summary: Use URLlib to load data that is located somewhere on the web.
Date: 2016-11-26 12:00
Category: how_to
Tags:
Authors: Nate Hall

<a href='http://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/python/import_dataset_from_url.ipynb' target='_blank'>Link to the full jupyter notebook.</a><br/>
<a href='http://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/python/import_dataset_from_url_code.ipynb' target='_blank'>Link to the code only jupyter notebook.</a>

We'll bring in data with urllib and then load it into our dataset as a csv.


```python
import urllib
import pandas as pd
```

### 1. Create a variable called "data_url" and paste in the URL as a string
```python
data_url = "http://instantinate.com/data/sales_data.html"
```

### 2. Call the urllib function with the urlretrieve method
The first argument we pass is the variable with the link to the dataset. And the second argument is the name of the dataset.
```python
urllib.urlretrieve (data_url, "sales.data")
```

### 3. Create the "data" variable and use the pandas.read_csv method
Pass the 'sales.data' argument to the read_csv method. Specify the delimiter for the dataset which in this case is spaces.
```python
data = pd.read_csv('sales.data', delimiter='\s+')
```

### 4. Create a dataframe using the the .dataframe method
Pass the data variable which read all the information from the url.
```python
df = pd.DataFrame(data)
```

### 5. Print out the .head( ) to confirm the dataset was loaded correctly.
```python
df.head()
```

### Here is the full code.


```python
data_url = "http://instantinate.com/data/sales_data.html"
urllib.urlretrieve (data_url, "sales.data")
data = pd.read_csv('sales.data', delimiter='\s+')
df = pd.DataFrame(data)
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>volume_sold</th>
      <th>2015_margin</th>
      <th>2015_q1_sales</th>
      <th>2016_q1_sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.420760</td>
      <td>93.802281</td>
      <td>337166.53</td>
      <td>337804.05</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.776510</td>
      <td>21.082425</td>
      <td>22351.86</td>
      <td>21736.63</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16.602401</td>
      <td>93.612494</td>
      <td>277764.46</td>
      <td>306942.27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.296111</td>
      <td>16.824704</td>
      <td>16805.11</td>
      <td>9307.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.156023</td>
      <td>35.011457</td>
      <td>54411.42</td>
      <td>58939.90</td>
    </tr>
  </tbody>
</table>
</div>
