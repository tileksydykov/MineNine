import time
import random as rd
import tkinter as tk
import threading as thread

class Timer(thread.Thread):
    """
    This is a Timer
    Timer takes a label from Ui and will
    update the value of timer in Ui

    Timer will show how many time you have left

    Timer is Good Boy!
    """
    def __init__(self, label):
        """
        This method takes object Label
        and initialise it for our Timer

        :param label: Object Label from TKINTER!!!
        """
        self.th = thread.Thread.__init__()
        self.sec = 10
        self.label = label

    def start(self):
        """
        This method will continue while your time is not end
        :return: Timeout if your time is out
        """
        self.sec = 10
        while True:
            self.sec -= 1
            time.sleep(1)
            if self.sec == 0:
                return "Timeout"

    def add(self):
        """
        if user picked a right button This method
        will add a 5 seconds to the user time
        :return:
        """
        self.sec += 5


class Generator:
    """
    This class is generate functions and answers for a game

    """
    def __init__(self):
        """
        initialise our operators for our generator
        """
        self.operator = ['+', '-', '*', '/']

    def gen(self, lvl):
        """
        generates math function for other methods in the class

        :param lvl: it's a main level for generating
        :return: math function
        """
        if lvl > 20:
            first = rd.randint(111, 999)
            second = rd.randint(111, 999)
            operator = self.operator[rd.randint(0, 3)]
            if operator == '+':
                return [str(first)+' + '+str(second)+" = ", first+second]
            elif operator == '-':
                return [str(first)+' - '+str(second)+" = ", first-second]
            elif operator == '*':
                return [str(first)+' * '+str(second)+" = ", first*second]
            elif operator == '/':
                return [str(first)+' / '+str(second)+" = ", first/second]
        elif lvl > 10:
            first = rd.randint(11, 99)
            second = rd.randint(11, 99)
            operator = self.operator[rd.randint(0, 3)]
            if operator == '+':
                return [str(first) + ' + ' + str(second) + " = ", first + second]
            elif operator == '-':
                return [str(first) + ' - ' + str(second) + " = ", first - second]
            elif operator == '*':
                return [str(first) + ' * ' + str(second) + " = ", first * second]
            elif operator == '/':
                return [str(first) + ' / ' + str(second) + " = ", first / second]

        else:
            first = rd.randint(1, 9)
            second = rd.randint(1, 9)
            operator = self.operator[rd.randint(0, 3)]
            if operator == '+':
                return [str(first) + ' + ' + str(second) + " = ", first + second]
            elif operator == '-':
                return [str(first) + ' - ' + str(second) + " = ", first - second]
            elif operator == '*':
                return [str(first) + ' * ' + str(second) + " = ", first * second]
            elif operator == '/':
                return [str(first) + ' / ' + str(second) + " = ", first / second]

    def genButton(self, lvl):
        """
        Method creates a row of buttons with answers

        :return: label for renew and answers for renew
        """
        fun = self.gen(lvl)
        answer = fun[1]
        fun = fun[0]
        answer_array = self.gen_answer_array(answer)
        return {'label': fun, 'answers': answer_array}

    def gen_answer_array(self, num):
        """
        This method takes a right answer for a
        math problem then returns array which consist
        a three additional number similar to right answer

        :param num: right answer
        :return: array in array with random numbers
        similar to right answer , second argument in
        array is index of right answer

        """
        num_type = type(num)
        result = []
        if num_type == float:
            if num < 10:
                start = 1
                end = 5
            else:
                start = 5
                end = 12
            for i in range(4):
                gen_num = rd.uniform(start, end)
                result.append(self.gen_answer(num, gen_num))
            random_index = rd.randint(0, 3)
            result[random_index] = num
            return [result, random_index]
        elif num_type == int:
            if num < 10:
                start = 1
                end = 5
            else:
                start = 5
                end = 12
            for i in range(4):
                gen_num = rd.randint(start, end)
                result.append(self.gen_answer(num, gen_num))
            random_index = rd.randint(0, 3)
            result[random_index] = num
            return [result, random_index]

    @staticmethod
    def gen_answer(a, b):
        """
        This staic method is generate a one answer
        which is similar to a var A value

        @:returns a + b or a - b
        """
        arr = ['+', '-']
        f = arr[rd.randint(0, 1)]
        if f == "-":
            return a - b
        else:
            return a + b


class Ui:
    """
    This is main class for User Interface

    creates a user interface and consist a
    logic and controllers for game

    """
    def __init__(self):
        """
        We initialise all elements and
        variables which we needs for our next methods

        Initialise
            *   PLayer ()
            *   Generator ()
            *   Timer ()

        """
        self.lvl = 1
        self.player = Player()
        self.gen = Generator()

        self.right_answer = 0

        self.is_over = False

        self.root = tk.Tk()
        self.root.title('Mental Math')
        self.bottom = tk.Frame(self.root,
                               bg="#2B2B2B",
                               width=1000,
                               height=500)

        self.top = tk.Frame(self.root,
                            bg="#3C3F41",
                            width=1000,
                            height=100)

        self.left = tk.Frame(self.root,
                             bg="#595B5D",
                             width=300,
                             height=500)

        self.timer = tk.Label(self.left,
                              bg="#595B5D",
                              text="10",
                              font=("Helvetica", 100),
                              fg="#FFF")

        self.start_button = tk.Button(self.root,
                                      text="start game",
                                      font=("Helvetica", 20),
                                      command=self.start)

        self.name = tk.Label(self.root,
                             text="Math Arithmeic",
                             font=("Helvetica", 32),
                             fg="#BBBBBB",
                             bg="#3C3F41")

        self.timer_label = tk.Label(self.left,
                                    bg="#595B5D",
                                    text="Timer:",
                                    font=("Helvetica", 32),
                                    fg="#FFF")

        self.game_over_label = tk.Label(self.bottom,
                                        text="GAME OVER",
                                        font=("Helvetica", 70),
                                        fg="red",
                                        bg="#2B2B2B",)

        self.time = 10

    def create(self):

        """
        This id main constructor of game

        It places all elements in UI and
        starts the Tkinter

        :return:
        """
        self.root.bind("<Key>", self.f)

        self.root.minsize(width=1000, height=600)

        self.root.maxsize(width=1000, height=600)

        self.root.overrideredirect(False)

        self.top.pack(side="top")

        self.bottom.pack(side="bottom")

        self.left.place(x=0, y=100)

        self.name.place(x=10, y=10)

        self.timer_label.place(x=20, y=20)

        self.timer.place(x=40, y=100)

        self.start_button.place(x=600, y=350)

        self.root.mainloop()

    def start(self):

        """
        This method is activates when
        MAIN START BUTTON clicked

        Creates all needed elements for game

        Bindes all elements with functions

        Starts Timer

        :return:
        """
        self.root.bind("<Key>", self.key)
        self.timer_run = True
        self.renew_timer()
        self.start_button.place_forget()
        array = self.gen.genButton(1)
        self.right_answer = array['answers'][1]
        answers = array['answers'][0]
        if self.is_over:
            self.game_over_label.place_forget()
            self.is_over = False
            self.your_lvl.place_forget()

        self.lvl_label = tk.Label(self.left,
                                  text="Level:",
                                  font=("Helvetica", 40),
                                  fg="#FFF",
                                  bg="#595B5D"
                                  )
        self.lvl_label.place(x=0, y=250)


        self.lvl_label_p = tk.Label(self.left,
                                  text=self.lvl,
                                  font=("Helvetica", 80),
                                  fg="#FFF",
                                  bg="#595B5D"
                                  )
        self.lvl_label_p.place(x=80, y=340)

        self.label = tk.Label(self.bottom,
                              text=array['label'],
                              font=("Helvetica", 55),
                              fg="#FFF",
                              bg="#2B2B2B"
                              )
        self.label.place(x=500, y=50)
        self.btn1 = tk.Button(self.bottom,
                              text="A",
                              font=("Helvetica", 50),
                              command=lambda x=0: self.click(x)
                              )
        self.btn1.place(x=400, y=300)
        self.btn2 = tk.Button(self.bottom,
                              text="B",
                              font=("Helvetica", 50),
                              command=lambda x=1: self.click(x)
                              )
        self.btn2.place(x=550, y=300)
        self.btn3 = tk.Button(self.bottom,
                              text="C",
                              font=("Helvetica", 50),
                              command=lambda x=2: self.click(x)
                              )
        self.btn3.place(x=700, y=300)
        self.btn4 = tk.Button(self.bottom,
                              text="D",
                              font=("Helvetica", 50),
                              command=lambda x=3: self.click(x)
                              )
        self.btn4.place(x=850, y=300)
        self.labels = []
        self.var = ["A: ", "B: ", "C: ", "D: "]

        j = 0
        for i in answers:
            i = round(i, 2)
            f = tk.Label(self.bottom, text=self.var[j]+str(i), font=("Helvetica", 25), bg="#2B2B2B", fg="#FFF")
            f.place(x=400+j*150, y=200)
            self.labels.append(f)
            j+=1

    def renew_timer(self):
        """
        This is main function of timer
        which will update timer every
        second
        :return:
        """
        if not self.timer_run:
            return
        if self.time != 0:
            self.time -= 1
            self.timer.config(text=self.time)
            self.timer.after(1000, self.renew_timer)
        else:
            self.loose()


    def add_timer_time(self):
        """
        this method will add 5 seconds to a timer
        when the user guess a num
        :return:
        """
        self.time += 5
        self.timer.config(text=self.time)

    def click(self, label):
        """
        this method is reacts to click event in
        tkinter and made all needed actions

        :param label: (int) 0-3 index of button
         of key which was clicked
        :return:
        """
        if label == self.right_answer:
            self.add_timer_time()
            self.lvl += 1
            self.lvl_label_p.config(text=self.lvl)

            array = self.gen.genButton(self.lvl)
            self.right_answer = array['answers'][1]
            answers = array['answers'][0]
            self.label.config(text=array['label'])
            self.var = ["A: ", "B: ", "C: ", "D: "]
            j = 0
            for i in answers:
                i = round(i, 2)
                self.labels[j].config(text=self.var[j]+str(i))
                j += 1
        else:
            self.loose()

    def loose(self):
        """
        if player looses ui is delete all elements and
        create a start menu with Label "GAME OVER"
        :return:
        """
        self.your_lvl = tk.Label(self.bottom,
                                 text="Your Level is " + str(self.lvl),
                                 font=("Helvetica", 40),
                                 fg="#FFF",
                                 bg="#2B2B2B"
                                 )
        self.your_lvl.place(x=400, y=400)
        self.time = 10
        self.timer.config(text=self.time)
        self.timer_run = False
        self.is_over = True
        self.game_over_label.place(x=350, y=50)
        self.lvl_label.place_forget()
        self.lvl_label_p.place_forget()
        self.lvl = 1
        for i in self.labels:
            i.place_forget()
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn3.place_forget()
        self.btn4.place_forget()
        self.label.place_forget()
        self.start_button.place(x=600, y=350)

    def key(self, n):
        """
        This is a router for keyboard events

        :param n: event object from tkinter.bind
        :return:
        """
        n = n.char
        if n == '1':
            self.click(0)
        elif n == '2':
            self.click(1)
        elif n == '3':
            self.click(2)
        elif n == '4':
            self.click(3)

    def f(self, event):
        if not self.is_over:
            self.start()



class Player:
    """
    This is our player
    """
    def __init__(self):
        """
        initialising how much the player can mistake
        """
        self.live = 3

    def miss(self):
        """
        if player miss his point
        :return: alive   or dead
        """
        if self.live == 1:
            return "dead"
        else:
            self.live -= 1
            return self.live


game = Ui()
game.create()
