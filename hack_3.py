"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(str):
    result = str
    #...
    cambiar = {"a":"@", "e":"3", "i":"¡", "o":"0", "u":"v"}
    lista = len(result)
    
    if len(result) >= 3:
        for antes, despues in cambiar.items():
            lista = len(result) - 1
            upper_letra = result[-1].upper()
            result = result[0].upper() + result[1:lista].replace(antes,despues) + upper_letra
    
    elif len(result) < 3:
        primera_letra = result[0].upper()
        for antes, despues in cambiar.items():
            for letra in result:
                if letra in cambiar.values() or letra == "u":
                    result = primera_letra + letra.lower().replace(antes,despues)
   
                else:
                    result = primera_letra + letra.upper().replace(antes,despues)

    return result

print(fn_hack_3("3q"))