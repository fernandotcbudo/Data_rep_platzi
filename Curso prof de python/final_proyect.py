from datetime import datetime
import pytz
import random


def set_change(any_list):
    
    final_set= set(any_list)
    list_change= list(final_set)
    selector= random.randint(0,4)
    name_chosen= list_change[selector]
    bogota_timezone= pytz.timezone("America/Bogota")
    bogota_datetime=datetime.now(bogota_timezone)
    
    return 'Hola ' + name_chosen + ' la fecha de hoy en Bogotá es: ' +bogota_datetime.strftime("%d/%m/%Y")

def run():
    run_func= set_change(["Diego","Paula","Fernando","Emma","Fernando","Paula","Carlos","Emma"])
    print(run_func)

if __name__ == '__main__':
    run()
