class BookMyShow:
    
    def __init__(self):
        self.movieName=None

    def assignMovieName(self):
        self.movieName="DRNDR"

b=BookMyShow()
print(b)
print(b.movieName) # None
b.movieName="TOXIC"
print(b.movieName) # TOXIC
b.assignMovieName()
print(b.movieName) # DRNDR

b1=BookMyShow()
print(b1)
print(b1.movieName) # None
b1.movieName="SALAAR"
print(b1.movieName) # SALAAR
b1.assignMovieName()
print(b1.movieName) # DRNDR

BookMyShow.assignMovieName="KGf"
print(BookMyShow.assignMovieName) #KGF