from Data import Data
from HexViewer import HexViewer
from OctalViewer import OctalViewer
from DecimalViewer import DecimalViewer

d1 = Data("Data 1")
d2 = Data("Data 2")

v1 = HexViewer()
v2 = OctalViewer()
v3 = DecimalViewer()

d1.attach(v1)
d1.attach(v2)
d1.attach(v3)

d2.attach(v1)
d2.attach(v2)
d2.attach(v3)

d1.data = 10
d2.data = 15

d1.detach(v1)
