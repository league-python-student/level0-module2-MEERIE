import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times
    for i in range(5):
        rand_num = random.randint(1, 2)

        if rand_num == 1:
            messagebox.showinfo(title=None, message="Your Cool!")
        elif rand_num == 2:
            messagebox.showinfo(title=None, message="Your UGLY!")
    # TODO 3) Find someone to test out your program. They will like it :)
