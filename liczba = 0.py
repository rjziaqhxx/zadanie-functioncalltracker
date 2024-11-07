
class FunctionCallTracker:
    def __init__(self, funkcja):
        self.funkcja = funkcja
        self.liczba = 0

    def __call__(self):
        return self.funkcja(self)
    
@FunctionCallTracker
def count_calls(self):
    self.liczba += 1
    return self.liczba

for i in range(10):
    print(count_calls())

