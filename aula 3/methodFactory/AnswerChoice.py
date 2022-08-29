from Answer import Answer

class AnswerChoice(Answer):
    options = set()

    def __init__(self, options):
        self.options = options

    def type_answer(self):
        return Answer.type_answer.CHOICE
    
    # get
    def options(self):
        return tuple(self.options)

    
