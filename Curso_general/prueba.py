#Real numbers
a=0,1e-3
print(type(a))
print(a)

#Complex numbers
b= 2,1 + 7,8j
print(type(b))
print(b) 

#Arrays 
new_list=[22,True,'Hello',"0,2",[5,8]]
select=new_list[4][1]
change=new_list[0]=99
select_2=new_list[0]
select_3=new_list[-1:]
print(f'Your first selection is {select} and second is {select_2} ok last selection is \n {select_3}')

#Tuples
new_tuple=(20,22,'Python')
new_select=new_tuple[0]
print(f'The value is {new_select}')

#Dictionaries
new_dic={
    'Neck':'Guillotine',
    'Arms':'Armbar',
    'Knees':'Kneebar'
}
new_select_1=new_dic['Neck']
print(f'Submission is {new_select_1}')

#FLOW CONTROL
keyword_1='texas12345'
key_input=str(input('Write the keyword:'))
if key_input == 'texas12345':
    print('OK')
else:
    print('Sorry, try it again')

#LOOPS 
AGE= 18
while True:
    age_new= int(input('Write your age: '))
    if age_new < AGE:
        continue
         
    else:
        print(f'Woooooo your age is {age_new}')
        break  
        

