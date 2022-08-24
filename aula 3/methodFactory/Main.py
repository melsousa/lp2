class Question:
    def __init__(self, text, level, tag, types,answer):
        self.text = text
        self.level = level
        self.tag = tag
        self.types = types
        self.answer = answer
        
    def createQuestion(text, level, tag, types, answer):
        return Question(text, level, tag, types, answer)
    
class AnswerText:
    
   def tipo(self):
       return "TEXT"
   
   
class AnswerOptions:
    
    # def __init__(self,options):
    #     self.options = options
    
    # def opthions_method(self):
    #     return self.options
        
    def tipo(self):
        return "CHOICE"
    def factory_method(tipo):
       pass

def factory_method(tipo):
    answer = {
        "TEXT": AnswerText,
        "CHOICE": AnswerOptions,
    }
    return answer[tipo]()

if __name__ == "__main__":
    q1 = Question.createQuestion("Quem foi?", 2, "#historia",factory_method('CHOICE'),['MEL','ABC'] )
    
    print(q1.answer)
    print(q1.level)
    print(q1.tag)
    print(q1.types())