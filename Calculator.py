import tkinter as tk
from pathlib import Path

root = tk.Tk()
root.geometry("325x610")
root.title("Calculator")
root.configure(bg = "#FFFFFF")

canvas = tk.Canvas( root, bg = "#FFFFFF", height = 610, width = 340, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle( 0.0, 200.0, 335.0, 610.0, fill="#E7D1F6", outline="")

base_dir = Path(__file__).parent / "assets" / "frame0"

nos = ['1','2','3','4','5','6','7','8','9','0']
ops = {'add':'+','subtract':'-','multiply':'*','divide':'/'}
calculation = []
def remove_from_calc():
    global calculation
    calculation.pop()
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    
def add_to_calc(val):
    global calculation
    if not calculation:
        if val in ops.keys():
            text_result.delete(1.0, "end")
        else:
            calculation.append(val)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, "".join(calculation))
    else:
        if val in nos:
            calculation.append(val)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, "".join(calculation))
        elif val in ops.keys():
            if calculation[-1] in ops.values():
                calculation.pop()
                calculation.append(ops[val])
                text_result.delete(1.0, "end")
                text_result.insert(1.0, "".join(calculation))
            else:
                calculation.append(ops[val])
                text_result.delete(1.0, "end")
                text_result.insert(1.0, "".join(calculation))
        else: 
            text_result.delete(1.0, "end")
        
def all_clear():
    global calculation
    text_result.delete(1.0, "end")
    calculation = []

def evaluate():
    global calculation
    if not calculation:
        text_result.delete(1.0, "end")
    else:
        try:
            result = str(eval("".join(calculation)))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)
            calculation = list(result)
        except Exception as e:
            text_result.delete(1.0, "end")
            text_result.insert(1.0, "Error")
            calculation = []

def evaluation(calc):
    def do_calculation():
        operator = operations.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)
    def precedence(opp):
        if opp in ('+','-'):
            return 1
        elif opp in ('*','-'):
            return 2
        return 0
    
    values = []
    operations = []
    i = 0
    while i < len(calc):
        if calc[i].isdigit():
            value = 0
            while i<len(calc) and calc[i].isdigit():
                value = (value*10)+calc[i]
                i+=1
            values.append(value)
            i -=1
        elif calc[i] in ops.values():
            if (operations and precedence(operations[-1]))>=precedence(calc[i]):
                do_calculation(operations, values)
            operations.append(calc[i])
        i+=1
    while operations:
        do_calculation(operations, values)
    return values[0]

def key_press(val):
    print("Button Pressed: ",val)
    if val == 'del': remove_from_calc()
    elif val == 'ac': all_clear()
    elif val == 'equal': evaluate()
    else: add_to_calc(val)

def disable_typing(event):
    return "break"

class Button():
    def __init__(self, pos_x, pos_y, val =None, h = 75.0, w = 75.0):
        image_path = base_dir / f"button_{val}.png"
        self.image = tk.PhotoImage(file=image_path)
        self.button = tk.Button(root, image=self.image, command=lambda: key_press(val), relief="flat")
        self.button.place(x=pos_x, y=pos_y, height=h, width=w)

text_result = tk.Text(root, font = ("Arial",24), bg="#ffffff",fg="black", highlightthickness=0)
text_result.place(x=5, y=90, height=100, width=310)
#text_result.bind("<Key>", disable_typing)

button_1 = Button( 5, 285, val='1')
button_2 = Button( 85, 285, val='2')
button_3 = Button( 165, 285, val='3')
button_4 = Button( 5, 365, val='4')
button_5 = Button( 85, 365, val='5')
button_6 = Button( 165, 365, val='6')
button_7 = Button( 5, 445, val='7')
button_8 = Button( 85, 445, val='8')
button_9 = Button( 165, 445, val='9')
button_0 = Button( 85, 525, val='0')

button_del = Button( 165, 205, val='del')
button_ac = Button( 5, 205, val='ac', w=150.0)
button_equal = Button( 165, 525, val='equal', w=150.0)
button_subtract = Button( 245, 285, val='subtract')
button_multiply = Button( 245, 365, val='multiply')
button_divide = Button( 245, 445, val='divide')
button_add = Button( 245, 205, val='add')

root.resizable(False, False)
root.mainloop()

