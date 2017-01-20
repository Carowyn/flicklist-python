import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        movies = [
            "Home, The Movie",
            "Thirteen Ghosts",
            "Hidden Figures",
            "The Bee Movie",
            "Moana"
        ]
        # TODO: make a list with at least 5 movie titles

        # TODO: randomly choose one of the movies, and return it
        list_length = len(movies)
        index = random.randint(0, list_length - 1)
        return movies[index]

    def get(self):
        # choose a movie by invoking our new function
        movie_today = self.getRandomMovie()
        movie_tomorrow = self.getRandomMovie()

        while movie_today == movie_tomorrow:
            movie_tomorrow= self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie_today + "</p>"

        new_content = "<h2>Tomorrow's Movie</h2>"
        new_content += "<p>" + movie_tomorrow + "</p>"
        
        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        self.response.write(content + new_content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
