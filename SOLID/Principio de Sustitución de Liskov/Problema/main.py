from pinguino import Pinguino 
# Uso 
if __name__ == "__main__": 
    pinguino = Pinguino() 
    try: 
        print(pinguino.volar()) 
    except NotImplementedError as e: 
        print(e)