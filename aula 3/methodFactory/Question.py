from Answer import Answer

class Question:
    def __init__(self, text, tags, level):
        self.text = text
        self.tags = tags
        self.level = level
        
    def text(self):
        return self.text
    
    def tags(self):
        return self.tags
    
    def level(self):
        return self.level
    
    def Answer(self):
        return Answer
    