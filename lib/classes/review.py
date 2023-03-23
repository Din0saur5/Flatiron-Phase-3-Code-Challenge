from lib.classes.viewer import Viewer
from lib.classes.movie import Movie

class Review:
    
    def __init__(self, viewer, movie, rating):
        self._viewer = viewer
        self._movie = movie
        self.rating = rating
        viewer.reviews.append(self)
        viewer.reviewed_movies.append(movie)
        movie.reviews.append(self)
        movie.reviewers.append(viewer)

    def get_viewer(self):
        return self._viewer
    def set_viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer must be a Viewer object")
    viewer = property(get_viewer, set_viewer)

    def get_movie(self):
        return self._movie
    def set_movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Movie must be a Movie object")
    movie = property(get_movie, set_movie)

    def get_rating(self):
        return self._rating
    def set_rating(self, rating):
        if isinstance(rating, int) and 0 < rating <= 5:
            self._rating = rating
        else:
            raise Exception("Rating must be an integer between 1 and 5")
    rating = property(get_rating, set_rating)

    # rating property goes here!

    # viewer property goes here!

    # movie property goes here!
