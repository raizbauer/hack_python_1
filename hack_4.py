"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    #...
    return result[0:-1] + result[-1].upper()

print(fn_hack_4())