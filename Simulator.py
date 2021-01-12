from generator import Generator

class Simulator:
    def __init__(self,state=0): #could be 0 or 1
        self.g = Generator(state)
        self.list_of_pages=[]
        self.page_frames = []
        self.set_conditions()

    def load_list(self):
        self.list_of_pages=self.g.return_list()

    def set_conditions(self):
        self.number_of_frames=int(input("Podaj ilosc ramek: "))
        self.alg=int(input("Jaki algorytm? 1-FIFO 2-LFU: 3-LRU "))

    def work(self):
        self.load_list()
        if self.alg==1:
            self.fifo()
        elif self.alg==2:
            self.lfu()
        else:
            self.lru()

    def fifo(self):
        miss=0
        hit=0
        counter=1
        xd=set()

        while counter<=len(self.list_of_pages):
            if len(self.page_frames)<self.number_of_frames:
                if(self.list_of_pages[counter-1].return_page_number() in xd):
                    hit=hit+1
                else:
                    self.page_frames.append(self.list_of_pages[counter-1])
                    xd.add(self.list_of_pages[counter-1].return_page_number())
                    miss=miss+1
            else:
                    tmp=self.list_of_pages[counter-1].return_page_number()
                    if(tmp in xd ):
                        print("Secik: ",xd)
                        print("Strona z hitem: " + str(self.list_of_pages[counter-1].return_page_number()))
                        print("Licznik: "+str(counter))
                        print("\n")
                        hit=hit+1
                    else:
                        tmp=sorted(self.page_frames,key=lambda t: t.return_wait_time(),reverse=True)
                        for i in range(self.number_of_frames):
                            if self.page_frames[i].return_wait_time()==tmp[0].return_wait_time():
                                print("Zastepowana strona: "+str(self.page_frames[i].return_page_number()))
                                xd.remove(tmp[0].return_page_number())
                                self.page_frames[i] = self.list_of_pages[counter-1]
                                print("Nowa strona: " + str(self.page_frames[i].return_page_number()))
                                xd.add(self.page_frames[i].return_page_number())
                        miss = miss + 1
            counter = counter + 1


            for i in range(len(self.page_frames)):
                self.page_frames[i].add_wait_time()

            for i in range(len(self.page_frames)):
                print("+-----+")
                print("|  "+str(self.page_frames[i].return_page_number())+"  |")
                print("+-----+")


        print("Miss: "+str(miss)+" Hits: "+str(hit))

    def lfu(self):


        def takeSecond(elem):
            return elem[1]

        fault=0
        counter=1
        xd=set()


        while counter<=len(self.list_of_pages):
            if len(self.page_frames)<self.number_of_frames:
                if(self.list_of_pages[counter-1].return_page_number() in xd):
                    for i in range(len(self.page_frames)):
                        if self.list_of_pages[counter-1].return_page_number()==self.page_frames[i].return_page_number():
                            self.page_frames[i].add_frequency()
                else:
                    self.list_of_pages[counter - 1].add_frequency()
                    self.page_frames.append(self.list_of_pages[counter-1])
                    xd.add(self.list_of_pages[counter-1].return_page_number())
                    fault=fault+1
            else:
                tmp=self.list_of_pages[counter - 1].return_page_number()
                if (tmp in xd):
                    for i in range(len(self.page_frames)):
                        if self.list_of_pages[counter-1].return_page_number()==self.page_frames[i].return_page_number():
                            self.page_frames[i].add_frequency()
                else:
                    tmp_frequencies=[]
                    for i in range(len(self.page_frames)):
                        tmp_frequencies.append(self.page_frames[i].return_frequency())

                    tmp_frequencies.sort()

                    for i in range(1,len(self.page_frames)-1):
                        if tmp_frequencies[0]==tmp_frequencies[i]:
                            continue
                        else:
                            print("Pokaz: " + str(tmp_frequencies[i]))
                            tmp_frequencies.pop(i)

                    tmp_list_of_index=[]
                    print("EEEEEE: "+str(tmp_frequencies[0]))

                    for i in range(len(self.page_frames)):
                        if self.page_frames[i].return_frequency()==tmp_frequencies[0]:
                            print("Strona: "+str(self.page_frames[i].return_page_number())+" Frequency: "+str(self.page_frames[i].return_frequency()))
                            tmp_list_of_index.append(i)

                    tmp_list_of_pages=[]
                    for i in range(len(tmp_list_of_index)):
                        tmp_list_of_pages.append(self.page_frames[tmp_list_of_index[i]])


                    tmp_list_of_pages.sort(key=lambda p: p.return_wait_time(),reverse=True)

                    for i in range(len(self.page_frames)):
                        if self.page_frames[i].return_page_number()==tmp_list_of_pages[0].return_page_number():
                            xd.remove(self.page_frames[i].return_page_number())
                            self.page_frames[i]=self.list_of_pages[counter-1]
                            xd.add(self.list_of_pages[counter-1].return_page_number())
                            self.page_frames[i].add_frequency()
                            fault = fault + 1




            counter = counter + 1


            for i in range(len(self.page_frames)):
                self.page_frames[i].add_wait_time()

            for i in range(len(self.page_frames)):
                print("+-----+")
                print("|  "+str(self.page_frames[i].return_page_number())+"  |")
                print("+-----+")


            print(" ")
            print("Faults: "+str(fault))
            print(" ")

    def lru(self):
        miss = 0
        hit = 0
        counter = 1
        xd = set()

        while counter <= len(self.list_of_pages):
            if len(self.page_frames) < self.number_of_frames:
                if (self.list_of_pages[counter - 1].return_page_number() in xd):
                    hit = hit + 1
                else:
                    self.page_frames.append(self.list_of_pages[counter - 1])
                    xd.add(self.list_of_pages[counter - 1].return_page_number())
                    miss = miss + 1
            else:
                tmp = self.list_of_pages[counter - 1].return_page_number()
                if (tmp in xd):
                    for i in range(len(self.page_frames)):
                        if self.list_of_pages[counter - 1].return_page_number()==self.page_frames[i].return_page_number():
                            self.page_frames[i].delete_wait_time()
                        hit = hit + 1
                else:
                    tmp = sorted(self.page_frames, key=lambda t: t.return_wait_time(), reverse=True)
                    for i in range(self.number_of_frames):
                        if self.page_frames[i].return_wait_time() == tmp[0].return_wait_time():
                            print("Zastepowana strona: " + str(self.page_frames[i].return_page_number()))
                            xd.remove(tmp[0].return_page_number())
                            self.page_frames[i] = self.list_of_pages[counter - 1]
                            print("Nowa strona: " + str(self.page_frames[i].return_page_number()))
                            xd.add(self.page_frames[i].return_page_number())
                    miss = miss + 1
            counter = counter + 1

            for i in range(len(self.page_frames)):
                self.page_frames[i].add_wait_time()

            for i in range(len(self.page_frames)):
                print("+-----+")
                print("|  " + str(self.page_frames[i].return_page_number()) + "  |")
                print("+-----+")

            print(" ")

        print("Miss: " + str(miss) + " Hits: " + str(hit))




