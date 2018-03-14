import webbrowser

class Movie(object):

# The self variable represents the instance of the object itself in this case
# the title of the movie, storyline, image and trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# This is to make the youtube trailer open when click by user
    def pop_trailer(self):
        webbrowser.open(self.trailer)
