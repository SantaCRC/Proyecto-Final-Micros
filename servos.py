import pyfirmata
board = pyfirmata.Arduino('/dev/ttyACM0')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
pin9 = board.get_pin('d:9:s')
pin10 = board.get_pin('d:10:s')

def main(posicion):
    x=posicion[0]
    y=posicion[1]
    pin9.write(x)
    pin10.write(y)

if __name__ == '__main__': 
    main([100,100])