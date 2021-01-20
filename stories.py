"""Madlibs Stories."""
import json
import os.path

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

def create_dictionary():
    """Stores all the different madlib stories in a dictionary for future use.

    Returns:
        a dictionary object with a key:value of id:story.
        Inside each story are {keys} that will be used to reach the values of a dictionary
        of an object that will be used for the story class
    """
    stories = {
        "1":"Once upon a time, long ago in {1}, there lived a" + 
            " large {2} {3}. It loved to {4} {5}.",
        "2":"As a(n) {1} astronaut, I completely understand the laws of" +
            " {2}, therefore, I am able to {3} very well! This makes me a(n) {4}"
            + " candidate to work on {5}.",
        "3":"While {1} in the ocean, I came across a(n) {2}"
            + " looking sea-{3}. Instead of {4}, I decided to approach it."
            + " Afterwards, I never {5} again!",
        "4":"The Amazon Rain-Forest is so {1}! I mean, someone can easily get"
            + " {2}. In the Amazon, there are so many deadily {3} as well. If you"
            + " {4} fast enough, you will be able to {5} fend them off"
    }
    #with open('story_dictionary.js', 'w') as out_file:
        #out_file.write('var stories = %s;' % json.dumps(stories))
    return stories


# Here's a story to get you started
