import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.
        cross_off_form = """
        <form action="/cross" method="post">
            <label>
                I want to cross off
                <select name="cross-movie">
                    <option>Magic Mike</option>
                    <option>The Big Lebowski</option>
                    <option>Coyote Ugly</option>
                    <option>House on Haunted Hill</option>
                    <option>Resident Evil</option>
                    <option>The Bee Movie</option>
                    <option>Home, The Movie</option>
                    <option>A Christmas Carol</option>
                    <option>Magic Mike XXL</option>
                    <option>Grease</option>
                </select>
                from my Watchlist.

            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
        """

        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)
        # <input type="text" name="cross-movie"/>


        content = page_header + edit_header + add_form + "<br>" + cross_off_form + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)


# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
    def post(self):
        cross_movie = self.request.get("cross-movie")

        crossed_movie_element= "<strike>" + cross_movie + "</strike>"
        sentence = crossed_movie_element + " has been crossed off your Watchlist."

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)



# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross', CrossOffMovie)
], debug=True)
