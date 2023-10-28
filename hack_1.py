"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(str):
    result = str
    #...

    nuevo_txt = ""

    if len(result) % 2 == 0 and len(result) > 2:
        for n in range(0, len(result)):
            if n == 1:
                nuevo_txt = nuevo_txt + result[n].upper()
            elif n == 2:
                nuevo_txt = nuevo_txt + result[n].lower()
            
            elif result[n] == "i":
                nuevo_txt = nuevo_txt + result[n].upper()
            else:
                nuevo_txt += result[n]
            
    elif len(result) % 2 == 1:
        for n in range(0, len(result)):
            if result[n] == "u":
                nuevo_txt = nuevo_txt + result[n].upper()
            else:
                nuevo_txt += result[n]
    
    elif len(result) % 2 == 0 and len(result) >= 2:
        for n in result:
            nuevo_txt = nuevo_txt + n.lower()
            
    return nuevo_txt