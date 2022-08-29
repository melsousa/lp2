from typing import Final, final

from QuestionFactory import QuestionFactory
from Question import Question

class Main:
    tags = set()
    question: Final = QuestionFactory.create(
        'Qual linguagem estudar?',
        tags.add("#programação")
        tags.add("#estudo"),
        # Question.level.score 
    )