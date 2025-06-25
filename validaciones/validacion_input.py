from typing import Union
def validar_a_numero(e: str) :
    if not e.isdigit() or int(e) <= 0:
        return False
    else: 
        return True

def validar_texto(e: str) -> bool:
    if not e.isalnum() or len(e) < 3:
        return False
    else:
        return True
        


