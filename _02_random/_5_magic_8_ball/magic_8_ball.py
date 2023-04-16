import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    # Make a variable and initialize it to a random number between 0 and 3
    ball = random.randint(0, 3)
    simpledialog.askstring(title="ASK 8BALL", prompt="INPUT YOUR QUESTION")
    # If the random number is 0
    if ball == 0:
        messagebox.showinfo(title=None, message="Yes")
    if ball == 1:
        messagebox.showinfo(title=None, message="No")
    if ball == 2:
        messagebox.showinfo(title=None, message="Maybe you should ask Google?")
    if ball == 3:
        messagebox.showinfo(title=None, message="TRY AGAIN")
