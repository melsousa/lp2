from enum import Enum
from Answer import Answer

class AnswerText(Answer):
    
    def Option(self):
        return Answer.Options.TEXT
        
