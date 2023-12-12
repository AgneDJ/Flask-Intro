"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html> 
      <head>
        <title>Start Here</title>
      </head>
      <body>
        <a href= http://localhost:5000/hello>HelloPage</a> 
        <a href= http://localhost:5000/diss>MeanPage</a> 
        <h1>Hi! This is the home page.</h1> 
      </body>
    </html>
       """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          <p>Choose a compliment: </p> 
          <input type="radio" id="compliment" name="compliment" value="beautiful">
          <label for="compliment">Beautiful</label><br>
          <input type="radio" id="compliment" name="compliment" value="nice">
          <label for="compliment">Nice</label><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


@app.route('/diss')
def say_diss():
    """Say diss and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There...</title>
      </head>
      <body>
        <h1>Hi There...</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          <p>Choose word :( : </p> 
          <input type="radio" id="diss" name="diss" value="mean person">
          <label for="diss">Mean</label><br>
          <input type="radio" id="diss" name="diss" value="anoying person">
          <label for="diss">Anoying</label><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
