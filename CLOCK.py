# print(''.join(['\033[' + str(x) + 'mfoo' for x in range(0,150)]) +'\033[0m')
# print('\033[' +'102' + 'm ' + '\033[0m')
import time
import datetime
import os


templ_ = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ]
f_0 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '], 
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]

f_1 = [
        ['⬛', '⬛', '⬛', '⬛', '  ', '  ', '  '],
        ['  ', '  ', '⬛', '⬛', '  ', '  ', '  '],
        ['  ', '  ', '⬛', '⬛', '  ', '  ', '  '],
       ['  ', '  ', '⬛', '⬛', '  ', '  ', '  '],
       ['  ', '  ', '⬛', '⬛', '  ', '  ', '  '],
       ['  ', '  ', '⬛', '⬛', '  ', '  ', '  '],
        ['  ', '  ', '⬛', '⬛', '  ', '  ', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]


f_2 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '  ', '  ', '  '],
        ['⬛', '⬛', '  ', '  ', '  ', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]


f_3 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
          ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]


f_4 = [
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ]


f_5 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '  ', '  ', '  '],
        ['⬛', '⬛', '  ', '  ', '  ', '  ', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]

f_6 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '  ', '  ', '  '],
         ['⬛', '⬛', '  ', '  ', '  ', '  ', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
]

f_7 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '  ', '  ', '  ', '⬛', '⬛', '  '],
       ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
       ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
       ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ]


f_8 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]


f_9 = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['  ', '  ', '  ', '  ', '⬛', '⬛', '  '],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '  '],
        ]

sep_1 = [
        ['', '', '', '', '', '', '  '],
        ['', '', '', '', '', '', '  '],
        ['', '', '', '⬛', '', '', '  '],
        ['', '', '', '', '', '', '  '],
        ['', '', '', '', '', '', '  '],
        ['', '', '', '⬛', '', '', '  '],
       ['', '', '', '', '', '', '  '],
        ['', '', '', '', '', ''], '  ',
        ]

def get_current_time():
    current_time = datetime.datetime.now()
    my_cur_time = current_time.strftime('%H:%M:%S')
    
    list_ct = []
    for i in my_cur_time:
        if i == '0':
            list_ct.append(f_0)
        elif i == '1':
            list_ct.append(f_1)
        elif i == '2':
            list_ct.append(f_2)
        elif i == '3':
            list_ct.append(f_3)
        elif i == '4':
            list_ct.append(f_4)
        elif i == '5':
            list_ct.append(f_5)
        elif i == '6':
            list_ct.append(f_6)
        elif i == '7':
            list_ct.append(f_7)
        elif i == '8':
            list_ct.append(f_8)
        elif i == '9':
            list_ct.append(f_9)
        elif i == ':':
            list_ct.append(sep_1)    
    for g in range(len(list_ct)):
        for l in range(len(list_ct[g])):
            for n in range(len(list_ct[g][l])):
                print(''.join(map(str,list_ct[g][l][n])), end='')
            print()
        
def sleep():    
    time.sleep(1)
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    
while True:
    get_current_time()
    sleep()
    clear_screen()
    
    