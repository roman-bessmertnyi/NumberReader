import OPi.GPIO as GPIO

GPIO.setboard(GPIO.ZEROPLUS)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(0, GPIO.OUT)

def get_bit(input, position):
    return (input >> position) & 1

fileName = input("Enter name of a file you wish to see:\n")
f = open(fileName, "r")
input = int(f.read())

print("Number found in file: \n%2d\n" %(input))
print("In byte from: ")

print("%1d" %(get_bit(input, 3)))
print("%1d" %(get_bit(input, 2)))
print("%1d" %(get_bit(input, 1)))
print("%1d" %(get_bit(input, 0)))

print("\nWriting to pins 8, 9, 7, 0")

GPIO.output(8, get_bit(input, 0))
GPIO.output(9, get_bit(input, 1))
GPIO.output(7, get_bit(input, 2))
GPIO.output(0, get_bit(input, 3))