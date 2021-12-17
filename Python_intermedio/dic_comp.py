import math

def run():
    #dict={}

    #for i in range(1,101):
        #if i%3 != 0:
            #dict[i]= i**3
    #print(dict)
    #return dict

    #dict={i:i**3 for i in range(1,101) if i%3 !=0}

    dict={i:math.sqrt(i) for i in range(1,1001)}
    print(dict)



if __name__ == '__main__':
    run()       