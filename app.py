from flask import Flask, request, render_template
from stories import Story,create_js
import json

app = Flask(__name__)

@app.route("/")
def landing_page():
    """landing page
    """
    
    return render_template("madlib.html")

@app.route("/story")
def story_page():
    """Page that displays completed Madlib Story!
    """
    story_dictionary = create_js()
    
    
    
    
    answer1 = request.args["input-1"]
    answer2 = request.args["input-2"]
    answer3 = request.args["input-3"]
    answer4 = request.args["input-4"]
    answer5 = request.args["input-5"]
    theme = request.args["story-theme"]
    
    s_obj = {
        "1":answer1,
        "2":answer2,
        "3":answer3,
        "4":answer4,
        "5":answer5
    }
    
    
    story = Story(
        ["1", "2", "3", "4", "5"],
        story_dictionary.get(theme)
    )
    
    
    response = story.generate(s_obj)
    
    return render_template("story.html", madlib=response)
    