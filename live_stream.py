import IPython.display
import PIL.image
import time
import numpy 
from IPython.display import clear_output

class ImageShow():

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('create instance')
            cls.instance = super(ImageShow, cls).__new__(cls)
            cls.instance.
        return cls.instance

    def imshow(self, frame, display):
        display.update(frame)
        s = f"""{int(1/(t2-t1))} FPS"""
        d2.update( IPython.display.HTML(s) )

if __name__ == "__main__":
    for i in range(10): 
        modi = ImageShow()
        modi.imshow()
