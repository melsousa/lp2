from tokenize import String
from typing import List, Set
from Question import Question
from AnswerText import AnswerText
from AnswerChoice import AnswerChoice

class QuestionFactory:
    
    
    def createAnswerText(text:String, tags:Set, level:Question.Level):
        return Question(text, tags, level, AnswerText())

    
    def createAnswerChoice( text:String, tags:Set, level:Question.Level, options:Set):
        return Question(text, tags, level, AnswerChoice(options))