from typing import Dict,List
from typing import Tuple

# Listas con tipado estatico 
positives: List[int] = [1,2,3,4,5]
# Diccionarios con tipado estatico 
users: Dict [str,int] = {
    'argentina':1,
    'colombia':2,
}
# Listas con diccionarios embebidos tipado estatico
countries:List[Dict[str,str]] = [
    {
        'name':'Argentina',
        'people':'656886',
    },
    
    {
        'name':'Colombia',
        'people':'786586',
    },  
]
# Tuplas con tipado estatico
numbers: Tuple[int,float,int] = [1,0.5,5]
