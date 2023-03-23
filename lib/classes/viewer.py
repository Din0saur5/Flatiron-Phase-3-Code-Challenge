class Viewer:
    all = []

    def __init__(self, username):
        # if username not in [viewer.username for viewer in Viewer.all]:
        self.username = username
        self.reviews = []
        self.reviewed_movies = []
        Viewer.all.append(self)

    def get_username(self):
        return self._username
    def set_username(self, username):
        if isinstance(username, str) and 16 > len(username) > 6:
            for viewer in Viewer.all:
                if viewer.username == username:
                    raise Exception("Username already exists")
                
            self._username = username
        else:
            raise Exception("Username must be a non-empty string between 6 and 16 characters")
    username = property(get_username, set_username)
    
    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):
        from lib.classes.review import Review
        if isinstance(rating, int) and 0 < rating <= 5:
            if movie in self.reviewed_movies:
                for review in self.reviews:
                    if review.movie == movie:
                        review.rating = rating
            else:
                Review(self, movie, rating)
        else:
            raise Exception("Rating must be an integer between 1 and 5")