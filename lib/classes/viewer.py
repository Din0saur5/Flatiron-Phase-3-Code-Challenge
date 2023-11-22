
from lib.classes.review import Review
class Viewer:
    users = []
    def __init__(self, username):
        self.username = username
        type(self).users.append(username)

# username property goes here! 
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username,str) and  6<= len(username)<=16:
            if username not in self.users:
                self._username = username
            else:
                raise Exception("username already exists")
        else:
            raise Exception("username must be str btn 6-16 characters")
        
# all reviews associated with viewer
    def reviews(self):
        return [review for review in Review.all if review.viewer is self]
        
    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    def reviewed_movie(self, movie):
        return True if movie in self.reviewed_movies() else False
                       
    
    def rate_movie(self, movie, rating):
        if self.reviewed_movie(movie):
            reviewL = [review for review in self.reviews() if review.movie is movie]
            review = reviewL.pop()
            review.rating = rating
        else:
            review = Review(self,movie,rating)

