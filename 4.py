def happy(name,style_char='-'):
    nam="Happy Birthday\n"
    print(style_char*25)
    print(nam*5+name)
    print(style_char*25)
    print("Happy Birthday "+"{}".format(name))


happy("ajay")
happy("anil")

