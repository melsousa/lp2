from hashSet import HashSet
from collections import defaultdict
from Answer import Answer

class AnswerChoice(Answer):
    options = HashSet()

    def __init__(self, options):
        self.options = options

    def type_answer(self):
        return Answer.type_answer.CHOICE
    
    # get
    def options(self):
        return defaultdict.update

    
