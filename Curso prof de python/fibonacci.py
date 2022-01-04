#Fibonacci sequence with iterators
import time

class FiboIter():
    # Constructor with the atribute max_num 
    def __init__(self,max_num:None):
        self.max_num = max_num
    # Method iter
    def __iter__(self):
        self.n1=0
        self.n2=1
        self.count=0
        return self
    # Method next
    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.n1
        elif self.count == 1:
            self.count += 1
            return self.n2
        else:
            if self.count <= self.max_num:
                self.aux= self.n1 + self.n2
                self.n1,self.n2 = self.n2,self.aux
                self.count += 1
                return self.aux
            else:
                print('Finished')
                raise StopIteration
                
        
if __name__ == '__main__':
    fibonacci= FiboIter(50)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)