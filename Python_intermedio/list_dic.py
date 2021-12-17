def run():
    my_list=[1,"Hello",True,4.5]
    my_dict={"firstname":"Diego","lastname":"Torres"}

    super_list=[
        {"firstname":"Diego","lastname":"Torres"},
        {"firstname":"Facundo","lastname":"Garcia"},
        {"firstname":"Paula","lastname":"Cantor"},
    ]

    super_dict={
        "natural_nums":[1,2,3,4],
        "floating_nums":[0.4,1.1,3.5]
    }

    for key, values in super_dict.items():
        print(f"El valor de la llave es {key} y el valor es {values}")

    for value in super_list:
        print("El nombre es " + value["firstname"], "y el apellido es " + value["lastname"])
            
        

if __name__ == '__main__':  
    run()