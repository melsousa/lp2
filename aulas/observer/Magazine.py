class Magazine:

    def update(self, subject):
        print('Magazine: Subject' + str(subject.name) +
              'has data '+str(oct(subject.data)))
