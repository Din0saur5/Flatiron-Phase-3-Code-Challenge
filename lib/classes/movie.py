from lib.classes.review import Review
from statistics import mean
class Movie:
    all = []
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
# title property goes here!
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title,str) and  len(title)> 0:
            self._title = title
        else: 
            raise Exception("title must be str more than 0 char")
    
    def reviews(self):
        return [review for review in Review.all if review.movie is self] 
    
    def reviewers(self):
        return [review.viewer for review in self.reviews()]    
        
    def average_rating(self):
        return mean([review.rating for review in self.reviews()]) if len(self.reviews()) > 0 else None

    @classmethod
    def highest_rated(cls):
        return sorted(cls.all, key = lambda n: n.average_rating(), reverse=True).pop(0) 
      