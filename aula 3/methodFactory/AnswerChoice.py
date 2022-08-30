from enum import Enum
from Answer import Answer

class AnswerChoice(Answer):
   
    def __init__(self, options):
        self.options = options

    def Option(self):
        return Answer.Options.CHOICE
    
    # get
    def options(self):
        return self.options

    
