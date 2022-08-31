from enum import Enum
from typing import Set
from Answer import Answer

class Question:

     
    class Level(Enum):
        EASY = 25
        MEDIUM = 50
        HARD = 75
        VERY_HARD = 100
        
        def __init__(self, score):
            self.score
        
        def score(self):
            return self.score
    
    tags = set([])

    def __init__(self, text, tags:Set, level: Level, answer: Answer):
        self.text = text
        self.tags = tags
        self.level = level
        self.answer = answer
        
    def text(self):
        return self.text
    
    def tags(self):
        return self.tags
    
    def level(self):
        return self.level
    
    def answer(self):
        return self.answer
    