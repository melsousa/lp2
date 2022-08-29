from enum import Enum
from Answer import Answer

class Question(Enum):
    tags = set()

    def __init__(self, text, tags, level):
        self.text = text
        self.tags = tags
        self.level = level
        
    def text(self):
        return self.text
    
    def tags(self):
        return tuple(self.tags)
    
    def level(self):
        return self.level
    
    def Answer(self):
        return Answer

     # erro
    def level(self):
        easy = 25
        medium = 50
        hard = 75
        very_hard = 100
        
        def score(self, easy, medium, hard, very_hard):
            return score()
        # def level(self, score): #####
        #     self.score = score
        
        # def score(self):
        #     return score
