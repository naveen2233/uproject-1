class Movie():
    """ This class is to create movie details by storing movie details
    and call it by using attributes """
    def __init__(self, movie_title, movie_image_url, movie_trailer_url,
                 movie_shot_note, movie_wiki_url):
        self.title = movie_title
        self.poster_image_url = movie_image_url
        self.trailer_youtube_url = movie_trailer_url
        self.movie_shot_info = movie_shot_note
        self.movie_wiki_url = movie_wiki_url
