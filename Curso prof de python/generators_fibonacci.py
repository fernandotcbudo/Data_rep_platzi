import time 

def fiboGen(max):   
    n1=0
    n2=1
    count=0
    
    while True:
        
        if count == 0:
            count += 1
            yield n1
        elif count == 1:
            count += 1
            yield n2
        else:
            if count <= max:
                aux= n1 + n2
                n1,n2 = n2, aux
                count += 1
                yield aux
            else:
                print('Finished')
                break

if __name__ == '__main__':
    fibonacci= fiboGen(50)
    for element in fibonacci:
        print(element)  
        time.sleep(0.5)
    