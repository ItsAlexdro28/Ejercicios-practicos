from pynput.keyboard import Key, Controller
keyboard = Controller()
import time

user_input = input("Enter a number: ")

# Split the input string into individual digits
digits = [int(char) for char in user_input if char.isdigit()]

time.sleep(4)

for i in range(5):
    keyboard.press('1')
    keyboard.release('1')  
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(str(i+1))
    keyboard.release(str(i+1))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(str(i+1))
    keyboard.release(str(i+1))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(str(digits[0]))
    keyboard.release(str(digits[0]))
    keyboard.press(str(digits[1]))
    keyboard.release(str(digits[1]))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
