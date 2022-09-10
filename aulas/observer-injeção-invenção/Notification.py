from Email import Email
from Sms import Sms
from Whatsapp import Whatsapp

class Notification:
    
    def execute(self, User):
        Email.execute(self, User)
        Sms.execute(self, User)
        Whatsapp.execute(self, User)
        
        