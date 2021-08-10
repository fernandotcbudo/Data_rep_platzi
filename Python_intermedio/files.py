def read():
    num=[]
    with open("/media/fernandot/FernandoTC/study_rep_platzi/Python_intermedio/files/files.txt","r",encoding="utf-8") as f:
        for line in f:
            num.append(int(line)) 
        print(num)
        f.close()

def write():
    names=['Facundo','Paula','Fernando','Emma','Ana','Rocío']
    with open('/media/fernandot/FernandoTC/study_rep_platzi/Python_intermedio/files/names.txt','w',encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
        f.close()


def run():
    write()

if __name__ == '__main__':
    run()