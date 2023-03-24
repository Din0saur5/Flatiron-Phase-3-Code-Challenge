class Movie:
    all = []
    
    def __init__(self, title):
        self.title = title
        self.reviews = []
        self.reviewers = []
        Movie.all.append(self)

    def get_title(self):
        return self._title
    def set_title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title must be a non-empty string")
    title = property(get_title, set_title)

    def average_rating(self):
        if len(self.reviews) > 0:
            return sum([review.rating for review in self.reviews]) / len(self.reviews)
        else:
            return 0

    @classmethod
    def highest_rated(cls):
        # highest_rated = None
        # highest_rating = 0
        # for movie in cls.all:
        #     if movie.average_rating() > highest_rating:
        #         highest_rated = movie
        #         highest_rating = movie.average_rating()
        # return highest_rated

        # highest_rated = {}
        # for movie in cls.all:
        #     highest_rated[movie] = movie.average_rating()
        # return max(highest_rated, key=highest_rated.get)

        return max(cls.all, key=lambda movie: movie.average_rating())