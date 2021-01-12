class Page:
    def __init__(self,page_number):
        self.page_number=page_number
        self.waiting_time=0
        self.frequency=0

    def return_page_number(self):
        return self.page_number

    def add_frequency(self):
        self.frequency=self.frequency+1

    def return_frequency(self):
        return self.frequency

    def add_wait_time(self):
        self.waiting_time=self.waiting_time+1

    def delete_wait_time(self):
        self.waiting_time=0

    def return_wait_time(self):
        return self.waiting_time