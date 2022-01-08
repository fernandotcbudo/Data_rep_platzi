def set_op(set1,set2):
    union=set1|set2
    print(f'The result of Union is {union}')
    intersection=set1&set2
    print(f'The result of Intersection is {intersection}')
    diference_1=set1-set2
    diference_2=set2-set1
    print(f'The first result of Diference is {diference_1} and the second is {diference_2}')
    simetric=set2^set1
    print(f'The result of Simetric Diference is {simetric}')
    
    return 'Finished'

if __name__ == '__main__':
    print('........ Sets example ........')
    print('')
    set_final=set_op({"Goku","Superman","Naruto","Chapulin"},{"Batman","Naruto","Flash","Goku"})
    print(set_final)