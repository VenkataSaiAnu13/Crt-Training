from abc import ABC,abstractmethod

class area(ABC):
    @abstractmethod
    def calculate_area(self):
        print("in calculate area")
class square(area):
    def calculate_area(self):
        print("in square method")
class rectangle(area):
    pass
ob=square()
ob.calculate_area()