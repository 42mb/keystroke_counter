import PySimpleGUI as sg
singlestroke = ['\n',' ',
                '1','2','3','4','5','6','7','8','9','0','ß',
                'q','w','e','r','t','z','u','i','o','p','ü','+',
                'a','s','d','f','g','h','j','k','l','ö','ä','#',
                '<','y','x','c','v','b','n','m',',','.','-']


sg.theme('Tan')   
# All the stuff inside your window.
layout = [  [sg.Text('')],
            [sg.Multiline(size=(200, 40), key='textbox')],
            [sg.Button('Count'), sg.Button('Delete all'), sg.Button('Close Window'), sg.Text('Keystrokes: '), sg.Text('',key = 'result')]]  # identify the multiline via key option


window = sg.Window('Keystrokecounter_GER', layout).Finalize()


def count_keystrokes(textinput):
    int_result = 0
    #print(textinput)
    for c in textinput:
        if(c in singlestroke):
            int_result+=1
        else:
            int_result+=2

    window['result'].update(int_result)


# Event Loop 
while True:
    event, values = window.read()
    if event in (None, 'Close Window'): 
        break
    if event in (None, 'Delete all'):
        window['textbox'].Update('')
        window['result'].Update('')
    if event in (None, 'Count'):
        count_keystrokes(values['textbox'])


    #print(values['textbox']) 

window.close()