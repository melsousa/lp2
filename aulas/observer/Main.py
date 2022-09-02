from Observer import Observer
from Chat import Chat
from Newspaper import Newspaper
from Magazine import Magazine

ob1 = Observer("Paulo")
ob2 = Observer("Raquel")

v1 = Chat()
v2 = Newspaper()
v3 = Magazine()

ob1.register(v1)
ob1.register(v2)
ob2.register(v3)

ob1.data = 10
ob2.data = 15

# ob1.notify()




