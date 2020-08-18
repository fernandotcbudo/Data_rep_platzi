# Function that receives a list of numbers, and returns its average.  

def operation(num_list):
    op=0
    list_without_str=[]
    for number in num_list:
        if number == ",":
            continue
        op= op+int(number)
        list_without_str.append(number)
        
    
    print(op/len(list_without_str))
    
           
def run():
    num_list=(list(input('Write a list of 5 numbers (just one digit and separated by ,): ')))
    operation(num_list)



if __name__ == "__main__":
    run()