"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(str):
    result = str
    #...
    remover_letra = {"a":"", "o":"", "i":"", "u":""}

    for letra_vieja, nueva_letra in remover_letra.items():
        result = result.replace(letra_vieja, nueva_letra)
           
    return result