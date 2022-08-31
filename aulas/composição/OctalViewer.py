
class OctalViewer():

    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) +
              'has data '+str(oct(subject.data)))
