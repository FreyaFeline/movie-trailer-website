#import webbrowser from Python Standard Library
import webbrowser
#define the aspects of class movie
class Movie():
    def __init__(self, movie_title, release_date, movie_storyline, movie_actors, poster_image, trailer_youtube):
        self.title = movie_title
        self.date = release_date
        self.storyline = movie_storyline
        self.actors = movie_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#define command show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
