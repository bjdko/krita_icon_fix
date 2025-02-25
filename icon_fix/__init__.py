from krita import Extension, Krita
from .icon_fix import yoink

class IconFix(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        yoink()

    def createActions(self, window):
        #suppress
        pass
        
Krita.instance().addExtension(IconFix(Krita.instance()))
