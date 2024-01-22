"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    nueva_lista = []
    for char in result:
        if char == "o":
            nueva_lista.append("0")
        elif char == "i":
            nueva_lista.append("1")
        elif char == "a":
            nueva_lista.append("@")
        else:
            nueva_lista.append(char.upper())
    
    #...
    return nueva_lista  

print(fn_hack_10())