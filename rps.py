import tkinter
import random


def main():
    rps = ["Rock", "Paper", "Scissors"]
    value = random.choice(rps)
    window = tkinter.Tk()
    window.title("Rock,Paper,Scissors")
    window.configure(background="#ffc0cb")
    lab6 = tkinter.Label(window, text="Choose!", font=("Courier", 40), bg="#ffc0cb", fg="#800000").pack()
    lab7 = tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                         fg='black').pack()

    def click():
        lab8 = tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                             fg='black').pack()
        lab = tkinter.Label(window, text="You choosed Rock!", font=("Georgia", 20), bg="#add8e6", fg='black').pack()
        lab1 = tkinter.Label(window, text="Computer choosed " + value + "!", font=("Georgia", 20), fg='black',
                             bg="#e6eafa").pack()
        if value == "Rock":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb").pack()
            tkinter.Label(window, text="It's a draw!", font=("Comic Sans MS", 25), bg="#d8bfd8", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def again():
                main()

            tkinter.Button(window, text="Play again", command=again, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()
        if value == "Paper":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="Computer wins!", font=("Comic Sans MS", 25), bg="red", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def myagain():
                main()

            tkinter.Button(window, text="Play again", command=myagain, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()
        if value == "Scissors":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="You win!", font=("Comic Sans MS", 25), bg="#00ff00", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def playagain():
                main()

            tkinter.Button(window, text="Play again", command=playagain, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()

    bt = tkinter.Button(window, text="Rock", bg="#ff4500", fg="black", padx=50, command=click).pack()

    def myclick():
        lab10 = tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                              fg='black').pack()
        lab2 = tkinter.Label(window, text="You choosed Paper!", font=("Georgia", 20), bg="#add8e6", fg='black').pack()
        lab3 = tkinter.Label(window, text="Computer choosed " + value + "!", font=("Georgia", 20), bg="#e6eafa",
                             fg='black').pack()
        if value == "Rock":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="You win!", font=("Comic Sans MS", 25), bg="#00ff00", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def again():
                main()

            tkinter.Button(window, text="Play again", command=again, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()
        if value == "Paper":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="It's a draw!", font=("Comic Sans MS", 25), bg="#d8bfd8", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def myagain():
                main()

            tkinter.Button(window, text="Play again", command=myagain, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()
        if value == "Scissors":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="Computer wins!", font=("Comic Sans MS", 25), bg="red", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def playagain():
                main()

            tkinter.Button(window, text="Play again", command=playagain, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()

    bt = tkinter.Button(window, text="Paper", bg="yellow", fg="black", padx=50, command=myclick, ).pack()

    def clicked():
        lab12 = tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                              fg='black').pack()
        lab4 = tkinter.Label(window, text="You choosed Scissors!", font=("Georgia", 20), bg="#add8e6",
                             fg='black').pack()
        lab5 = tkinter.Label(window, text="Computer choosed " + value + "!", font=("Georgia", 20), bg="#e6eafa",
                             fg='black').pack()
        if value == "Rock":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="Computer wins!", font=("Comic Sans MS", 25), bg="red", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def again():
                main()

            tkinter.Button(window, text="Play again", command=again, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()
        if value == "Paper":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="You win!", font=("Comic Sans MS", 25), bg="#00ff00", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def myagain():
                main()

            tkinter.Button(window, text="Play again", command=myagain, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()
        if value == "Scissors":
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()
            tkinter.Label(window, text="It's a draw!", font=("Comic Sans MS", 25), bg="#d8bfd8", fg='black').pack()
            tkinter.Label(window, text="Thanks for playing!", font=("Bookman", 10), bg="#ffd700", fg='black').pack()
            tkinter.Label(window, text="__________________________________________________", bg="#ffc0cb",
                          fg='black').pack()

            def playagain():
                main()

            tkinter.Button(window, text="Play again", command=playagain, bg="#40e0d0", fg='black').pack()

            def close():
                quit()

            tkinter.Button(window, text="Close", command=close, bg="#40e0d0", fg='black').pack()

    bt = tkinter.Button(window, text="Scissors", bg="#32cd32", fg="black", padx=50, command=clicked).pack()
    window.geometry('390x430')
    window.mainloop()


main()
