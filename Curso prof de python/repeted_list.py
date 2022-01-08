# Remove repeated items for a list

#def remove_duplicates(some_list):
    #with_out_dup= []
    #for element in some_list:
        #if element not in with_out_dup:
            #with_out_dup.append(element)
    #return with_out_dup
        
#def run():
    #random_list= [1,1,2,5,6,4,4,7,8]
    #print(remove_duplicates(random_list))
    
def remove_set(some_list):
    my_set= set(some_list)
    return my_set

    
def run():
    random_list= [1,1,2,5,6,4,4,7,8]
    print(remove_set(random_list))

if __name__ == '__main__':
    run()