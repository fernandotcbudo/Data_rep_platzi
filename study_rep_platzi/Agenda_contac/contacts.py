import csv

class Contact:

    def __init__(self,name,phone,email):
        self._name= name
        self._phone= phone
        self._email= email


class Contact_book:
    def __init__(self):
        self._contacts=[]

    def add(self,name,phone,email):
        contact=Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()


    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break

        else:
            self._not_found()

    def update(self,name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():

                name = str(input('Escribe el nombre: '))
                phone = str(input('Escribe el telefono: '))
                email = str(input('Escribe el mail: '))

                contact._name=name
                contact._phone =phone
                contact._email=email
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv','w') as f:
            writer= csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact._name, contact._phone, contact._email))



    def _print_contact(self,contact):
        print('___*______*______*______*___')
        print(f'Nombre: {contact._name}')
        print(f'Celular: {contact._phone}')
        print(f'Email: {contact._email}')
        print('___*______*______*______*___')

    def _not_found(self):
        print('¡NO ENCONTRADO!')





def run():

    contact_book=Contact_book()

    with open('contacts.csv','r') as f:
        reader= csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            elif row == []:
                continue
            else:
                contact_book.add(row[0],row[1],row[2])





    while True:
        command=str(input('''
        ¿Que deseas hacer?
        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre: '))
            phone = str(input('Escribe el telefono: '))
            email = str(input('Escribe el mail: '))

            contact_book.add(name,phone,email)

        elif command == 'ac':
            nombre_a_encontrar=str(input('Nombre de contacto a actualizar: '))
            contact_book.update(nombre_a_encontrar)
        elif command == 'b':
            name = str(input('Escribe el nombre: '))
            contact_book.search(name)
        elif command == 'e':
            name = str(input('Escribe el nombre: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando NO encontrado: ')



if __name__=='__main__':
    print(' *** BIENVENIDO/A A TU AGENDA ***')
    run()