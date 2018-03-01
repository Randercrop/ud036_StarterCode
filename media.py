class Movie:
    """ When a Movie instance is created, assign parameters to variables. """

    def __init__(self, movieName, posterLink, trailerLink, year):
        self.title = movieName
        self.poster_image_url = posterLink
        self.trailer_youtube_url = trailerLink
        self.year = year
