
origin=0
def go(step):
    global origin
    new_pos=origin+step
    origin=new_pos
    return origin
print(go(2))
print(go(2))
print(go(2))