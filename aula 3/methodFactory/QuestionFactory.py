from abc import ABC,abstractmethod
from Question import Question
from AnswerText import AnswerText
from AnswerChoice import AnswerChoice

class QuestionFactory(ABC):
    
    @staticmethod
    def create(self, text, tags, level):
        return Question(text,tags,level,AnswerText() )

    @staticmethod
    def create(self, text, tags, level, options):
        return Question(text, tags, level, AnswerChoice(options))