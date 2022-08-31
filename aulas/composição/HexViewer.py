class HexViewer:

    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(
            subject.name, subject.data))
