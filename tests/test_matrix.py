from niat import PixelMatrix
import time

matrix = PixelMatrix()

matrix.demo()


while True:
    matrix.show("heart","red")
    time.sleep(1)

    matrix.show("diamond","green")
    time.sleep(1)

    matrix.show("arrow_up","blue")
    time.sleep(1)