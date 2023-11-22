

class Review:
    all = []
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        type(self).all.append(self)
        
# rating property goes here!
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and rating in range(1,6):
            self._rating = rating
        else: 
            raise Exception('rating must be int from 1-5')
           

# viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    @viewer.setter
    def viewer(self, viewer):
        from lib.classes.viewer import Viewer
        if isinstance(viewer,Viewer):
            self._viewer = viewer
        else: 
            raise Exception('not a viewer')
           
# movie property goes here!
    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, movie):
        from lib.classes.movie import Movie
        if isinstance(movie,Movie):
            self._movie = movie
        else: 
            raise Exception('not a movie')
           
           
