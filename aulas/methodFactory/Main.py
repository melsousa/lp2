from typing import Final, final

from QuestionFactory import QuestionFactory
from Question import Question
from Answer import Answer

# So ta chamando de forma de objeto

question = QuestionFactory.createAnswerText(
        "Qual linguagem estudar?",
        ['#programação', '#estudo'],
        Question.Level.HARD)

question1 = QuestionFactory.createAnswerChoice(
        "teste?",
        ('#1', '#2'),
        Question.Level.EASY,
        ('ndj', 'vjks')
        
)
print(question.text)
print(question.tags)
print(question1.level)