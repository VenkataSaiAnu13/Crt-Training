from abc import ABC,abstractmethod

class area(ABC):
    @abstractmethod
    def calculate_area(self):
       pass
    @abstractmethod
    def calculate_circle_are(self):
        pass
class square(area):
    def calculate_area(self):
        print("in square")
    def calculate_circle_are(self):
        pass

ob=square()
ob.calculate_area()