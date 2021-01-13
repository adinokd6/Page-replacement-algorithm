import numpy
import random
from page import Page


class Generator:
    def __init__(self, state=0):  # state can be read or generate (default is set to generate) e.g read=1 generate=0
        self.list_of_pages = []
        if state == 0:
            self.set_conditions()
        else:
            f = input("File path: ")
            self.file_path = f
            self.read()

    def set_conditions(self):
        number_of_pages = int(input("Stron: "))
        mean_duration = int(input("Srednia wartosc: "))
        standard_deviation = int(input("Odchylenie standardowe: "))
        self.number_of_pages= number_of_pages
        self.mean_duration = mean_duration
        #5/CyLQNAve0YQhMuexWN5EarH6XWI/aFwJ7MPX17tz0=
        self.standard_deviation = standard_deviation
        self.random_duration()


    def read(self):
        f = open(self.file_path, 'r').read()
        lines = f.split('\n')  #
        lines.pop(len(lines) - 1)

        tmp_pages = []

        for line in lines:
            tmp = line.split(" ")
            tmp_page_number = int(tmp[0])
            tmp_pages.append(self.new_Page(tmp_page_number))

        self.list_of_pages = tmp_pages

    def return_list(self):
        return self.list_of_pages

    def write(self):
        counter = 0
        with open("Generated pages", 'w') as f:
            while counter < len(self.list_of_pages):
                f.write(str(self.list_of_pages[counter].return_page_number()))
                f.write("\n")
                counter = counter + 1

    def new_Page(self, page_number):
        tmp = Page(page_number)
        return tmp

    def random_duration(self):  # TODO generator losuje liczby i duration niekiedy wynosi 0. Trzeba to jakos naprawic
        arr = numpy.random.normal(loc=self.mean_duration, scale=self.standard_deviation,size=(self.number_of_pages + 100)).round(0).astype(numpy.int)  # array of random duration time
        tmp_arr = arr.tolist()
        var = 0
        tmp=[]
        for i in range(self.number_of_pages):
            while var <= 0:
                var = random.choice(tmp_arr)
            tmp.append(var)
            var = 0

        for i in range(self.number_of_pages):
            self.list_of_pages.append(Page(tmp[i]))
        self.write()




