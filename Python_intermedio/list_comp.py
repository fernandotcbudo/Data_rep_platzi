list= range(0,51)
#count=[]

def run():
    #for i in list:
        #if i%3 != 0:
            #count.append(i**2)
        #else:
            #pass
    #print(count
    #return count
    #count=[i**2 for i in range(1,51) if i%3 != 0]
    #print(count)

    count=[ i for i in range (1,9999) if i%4 == 0 and i%6 ==0 and i%9 == 0 ]
    print(count)
    

if __name__ == '__main__':
    run()