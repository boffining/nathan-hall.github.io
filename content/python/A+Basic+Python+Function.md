Title: A Basic Python Function
Slug: a_basic_python_function
Summary: The basics to making a python function.
Date: 2016-11-23 12:00
Category: python
Tags:
Authors: Nate Hall

<a href='http://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/python/A%20Basic%20Python%20Function.ipynb'>Link to the full jupyter notebook.</a><br/>
<a href='https://nbviewer.jupyter.org/github/nathan-hall/nathan-hall.github.io/blob/pelican/content/python/A%20Basic%20Python%20Function%20Code.ipynb'>Link to the code only jupyter notebook.</a>

## What do dictionaries and baking cakes have in common? Read below to find out.

### First we'll load in some data below.
This is a list of dictionaries that contains information about different movies.


```python
#Loading in a movie ratings data set.
movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
```

### It starts with a def
 Every function needs a definition. Think of it like a normal dictionary. If you were to go look up a certain word you would need to know the first few letters to find it. But there also would only be one possible definition for that word in the dictionary. Python functions are the same in this regard, they need a unique name so that you can find it later.
#### We're going to definie our function below:
```python
def genre_avg(cat):
```
### Wait a minute?! What's that "cat" thing in there?!?! (Your ingredients)
That is a scary thing called a "parameter". It is basically the ingredients to your recipe. If you want to bake a cake you put ingredients into it and out comes a delicious cake. For parameters you "pass" these ingredients and then tell the function what to do with them and hopefully [crossesfingers] we get cake.
### Create an empty list. (Get out a mixing bowl)
The genre_avg list will hold all the results of our function.
```python
def genre_avg(cat):
    genre_avg = []
```
### For Loop or not to For Loop (Measure the ingredients)
We have the ingredients and the mixing bowl... so now we need to measure the ingredients. The for loop in this function goes through each statement in the dictionary above and measures it against the "parameter" we passed it. In this case we're interested only in movies that fall in the Action genre. So we measure out all the action movies from our dataset and then what? Can you see what happens next?
```python
def genre_avg(cat):
    genre_avg = []
    for x in movies:
        if cat == x["category"]:
```
### Append (Mix the ingredients)
This takes all the ingredients (parameters) that you just measured and mixes them together. And where do you mix things? In the mixing bowl of course! So now all our ingredients have been measured and are back in our mixing bowl all neat and unbaked... hmm... I wonder what the next step is.
```python
def genre_avg(cat):
    genre_avg = []
    for x in movies:
        if cat == x["category"]:
            genre_avg.append(x['imdb'])
```
### Return (Bake it!!!!)
Now we bake all those nice ingredients to get the most perfect cake we ever could ask for. In this case, a perfect average of score of a particular genre in our movie dataset.
```python
def genre_avg(cat):
    genre_avg = []
    for x in movies:
        if cat == x["category"]:
            genre_avg.append(x['imdb'])
    return sum(genre_avg)/len(genre_avg)
```
### Now for the magic.
This is not just any cake baking exercise. This is a magical cake machine that can give you any kind of cake you want so long as you give it the ingredients with the right "parameter". That's what is going on in the last statement after the function is defined. We reference that function and give it some ingredients and instantly we have some magic cake! How about that.
```python
genre_avg("Action")
```

## Here's the whole code.


```python
def genre_avg(cat):
    genre_avg = []
    for x in movies:
        if cat == x["category"]:
            genre_avg.append(x['imdb'])
    return sum(genre_avg)/len(genre_avg)
```


```python
genre_avg("Action")
```




    6.3
