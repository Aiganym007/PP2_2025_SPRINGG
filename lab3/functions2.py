# Dictionary of movies

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
#1
def imdb(movie):
    if movie["imdb"]>5.5:
        return True
movie = movies[0]
imdb_r = imdb(movie)
print(imdb_r)

#2
def score(f):
    r=[] 
    for m in f:  
        if m["imdb"] > 5.5:  
            r.append(m)
    for i in r:
        print(i)
score(movies)

#3
def score(f):
    r=[]
    n="Thriller"
    for m in f:  
        if m["category"]==n:  
            r.append(m)
    for i in r:
        print(i)
score(movies)

#4
def average(f):
    c=0
    t=0
    for m in f:  
        c+=m["imdb"]
        t+=1
    a=c/t
    return a

#5
def average(f):
    a=input()
    c=0
    t=0
    for m in f: 
        if m["category"]==a: 
            c+=m["imdb"]
            t+=1
    e=c/t
    return e 

