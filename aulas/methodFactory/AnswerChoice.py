from enum import Enum
from typing import Set
from Answer import Answer

class AnswerChoice(Answer):
   
    options = set()
   
    def __init__(self, options:Set):
        self.options = options

    def Option(self):
        return Answer.Options.CHOICE
    
    # get
    def options(self):
        return self.options

    
