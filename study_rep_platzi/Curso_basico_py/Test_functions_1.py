# Function that receives three numbers, and returns its average.  

def operation(list_transformed):
    op=0
    list_without_str=[]
    for number in list_transformed:
        if number == ",":
            continue
        op= op+int(number)
        list_without_str.append(number)
        
    
    print(f'The result of the operation is {round(op/len(list_without_str),2)}')
    
           
def run():
    list_transformed=[]
    num_list1=(int(input('Write a number: ')))
    num_list2=(int(input('Write a second number: ')))
    num_list3=(int(input('Write a third number: ')))

    list_transformed=[num_list1,num_list2,num_list3]
    operation(list_transformed)



if __name__ == "__main__":
    print('*Function that receives three numbers, and returns its average*')
    run()