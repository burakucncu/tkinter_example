import tkinter as tk
from tkinter import Tk, Label
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import pygame  
from tkinter import filedialog

def plus():
    num1 = entry_int_plus1.get()
    num2 = entry_int_plus2.get()
    num1 = float(num1)
    num2 = float(num2)
    result = num1 + num2
    formatted_result_plus = "{:.2f}".format(result)
    result_label.config(text=f"{num1} + {num2} = {formatted_result_plus} kıps ;)")

def minus():
    num1 = entry_int_minus1.get()
    num2 = entry_int_minus2.get()
    num1 = float(num1)
    num2 = float(num2)
    result = num1 - num2
    formatted_result_minus = "{:.2f}".format(result)
    result_label.config(text=f"{num1} - {num2} = {formatted_result_minus} kıps ;)")

def multiply():
    num1 = entry_int_multiply1.get()
    num2 = entry_int_multiply2.get()
    num1 = float(num1)
    num2 = float(num2)
    result = num1 * num2
    formatted_result_multiply = "{:.2f}".format(result)
    result_label.config(text=f"{num1} * {num2} = {formatted_result_multiply} kıps ;)")

def divide():
    num1 = entry_int_divide1.get()
    num2 = entry_int_divide2.get()
    num1 = float(num1)
    num2 = float(num2)
    result = num1 / num2
    formatted_result_divide = "{:.2f}".format(result)
    result_label.config(text=f"{num1} / {num2} = {formatted_result_divide} kıps ;)")

def power():
    num1 = entry_int_power1.get()
    num2 = entry_int_power2.get()
    num1 = float(num1)
    num2 = float(num2)
    result = num1 ** num2
    formatted_result_power = "{:.2f}".format(result)
    result_label.config(text=f"{num1} ^ {num2} = {formatted_result_power} kıps ;)")

def root():
    number = entry_int_number.get()
    root_degree = entry_int_root_degree.get()
    number = float(number)
    root_degree = float(root_degree)
    result = number ** (1/root_degree)
    formatted_result_root = "{:.2f}".format(result)
    result_label.config(text=f"Root = {formatted_result_root} kıps ;)")

def velocity():
    first_velocity = entry_int_first_velocity.get()
    acceleration = entry_int_acceleration.get()
    time_velocity = entry_int_time_velocity.get()
    first_velocity = float(first_velocity)
    acceleration = float(acceleration)
    time_velocity = float(time_velocity)
    result = first_velocity + acceleration * time_velocity 
    formatted_result_velocity = "{:.2f}".format(result)
    result_label.config(text=f"Velocity = {formatted_result_velocity} m/s kıps ;)")

def interest():
    starting_money = entry_int_starting_money.get()
    interest_rate = entry_int_interest_rate.get()
    time = entry_int_time.get()
    starting_money = float(starting_money)
    interest_rate = float(interest_rate)
    time = float(time)
    result = starting_money + ((starting_money / 100) * (interest_rate / 365) * time)
    formatted_result_interest = "{:.2f}".format(result)
    formatted_result_interest = float(formatted_result_interest)
    haram_money = formatted_result_interest - starting_money
    formatted_haram_money = "{:.2f}".format(haram_money)
    result_label.config(text=f"Money = {formatted_result_interest}, haram money ={formatted_haram_money} kıps ;)")

def installment():
    cost = entry_int_cost.get()
    month = entry_int_month.get()
    cost = float(cost)
    month = float(month)
    result = cost / month
    formatted_result_installment = "{:.2f}".format(result)
    result_label.config(text=f"Installment = {formatted_result_installment} 'per month kıps ;)")

# I used the 2024 income tax rates in Turkey.
# I know that the rates are high, but I wanted to show you how to calculate the income tax.
# If you want to change the rates, you can change them in the function.

def income_tax():           
    earning = entry_int_earning.get()
    earning = float(earning)
    if earning <= 115000:
        tax_rate = 15
        result = (earning * tax_rate / 100)
        formatted_result_income_tax = "{:.2f}".format(result)
        result_label.config(text=f"Income Tax = {formatted_result_income_tax} teype araba parası kıps ;)")
    elif earning <= 230000 and earning > 115000:
        tax_rate = 20 
        result = 16500 + ((earning - 110000) * tax_rate / 100)
        formatted_result_income_tax = "{:.2f}".format(result)
        result_label.config(text=f"Income Tax = {formatted_result_income_tax} teype araba parası kıps ;)")
    elif earning <= 580000 and earning > 230000:
        tax_rate = 27
        result = 40500 + ((earning - 230000) * tax_rate / 100)
        formatted_result_income_tax = "{:.2f}".format(result)
        result_label.config(text=f"Income Tax = {formatted_result_income_tax} teype araba parası kıps ;)")
    elif earning <= 3000000 and earning > 580000:
        tax_rate = 35
        result = 135000 + ((earning - 580000) * tax_rate / 100)
        formatted_result_income_tax = "{:.2f}".format(result)
        result_label.config(text=f"Income Tax = {formatted_result_income_tax} teype araba parası kıps ;)")
    elif earning > 3000000:
        tax_rate = 40
        result = 982000 + ((earning - 3000000) * tax_rate / 100)
        formatted_result_income_tax = "{:.2f}".format(result)
        result_label.config(text=f"Income Tax = {formatted_result_income_tax} teype araba parası kıps ;)")

# If you didn't paly the sound file, you will delete include 134-143 and replace this text='AMMINAKEE!!' to text='' on line 134.

def clear():
    result_label.config(text='AMMINAKEE!!')
    
def play_sound():
    file_path = "ammınake_vada.mp3"
    if file_path:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def clear_and_play_sound():
    clear()
    play_sound()

window = ttk.Style().master   #You can use darkly or journal theme if you want.

window.title('Math')
window.geometry('1920x1080')

title_label = ttk.Label(window, 
                        text='Some Calculations', 
                        font=('Times 24 bold italic'))
title_label.pack(pady=20)

plus_label = ttk.Label(window,
                          text='+, colmn 1: number, colmn 2: number',
                          font=('Arial', 14))
plus_label_name = ttk.Label(window,
                            text='Subsitution →',
                            font=('Times 14 bold italic'))

minus_label = ttk.Label(window,
                          text='-, colmn 1: number, colmn 2: number',
                          font=('Arial', 14))
minus_label_name = ttk.Label(window,
                            text='Extraction →',
                            font=('Times 14 bold italic'))

multiply_label = ttk.Label(window,
                           text='*, colmn 1: number, colmn 2: number',
                          font=('Arial', 14))
multiply_label_name = ttk.Label(window,
                            text='Multiplication →',
                            font=('Times 14 bold italic'))

divide_label = ttk.Label(window,
                         text='/, colmn 1: numerator, colmn 2: denominator',
                         font=('Arial', 14))
divide_label_name = ttk.Label(window,
                            text='Division →',
                            font=('Times 14 bold italic'))

power_label = ttk.Label(window,
                        text='^, colmn 1: number, colmn 2: power',
                        font=('Arial', 14))
power_label_name = ttk.Label(window,
                            text='Exponential →',
                            font=('Times 14 bold italic'))

root_label = ttk.Label(window,
                       text='√, colmn 1: number, colmn 2: root degree',
                       font=('Arial', 14))
root_label_name = ttk.Label(window,
                            text='Root →',
                            font=('Times 14 bold italic'))

velocity_label = ttk.Label(window,
                            text='hint: colmn 1: first velocity, colmn 2: acceleration,\ncolmn 3: time',
                            font=('Arial', 14))
velocity_label_name = ttk.Label(window,
                            text='Velocity →',
                            font=('Times 14 bold italic'))

interest_label = ttk.Label(window,
                           text='hint: colmn 1: starting money, colmn 2: interest rate,\ncolmn 3: time',
                          font=('Arial', 14))
interest_label_name = ttk.Label(window,
                            text='Interest →',
                            font=('Times 14 bold italic'))

installment_label = ttk.Label(window,
                              text='hint: colmn 1: cost, colmn 2: month',
                              font=('Arial', 14))
installment_label_name = ttk.Label(window,
                            text='Installment →',
                            font=('Times 14 bold italic'))

income_tax_label = ttk.Label(window,
                             text='hint: colmn 1: earning per a year',
                             font=('Arial', 14))
income_tax_label_name = ttk.Label(window,
                            text='Income Tax →',
                            font=('Times 14 bold italic'))

# Plus

input_frame_plus = ttk.Frame(window)
entry_int_plus1 = tk.IntVar()
entry_int_plus1 = ttk.Entry(input_frame_plus, textvariable=entry_int_plus1)
entry_int_plus2 = tk.IntVar()
entry_int_plus2 = ttk.Entry(input_frame_plus, textvariable=entry_int_plus2)

button_plus1 = ttk.Button(input_frame_plus,  
                         text='Add', 
                         command=plus)
# So that the screen looks nice, I added the same button again
button_plus2 = ttk.Button(input_frame_plus, 
                         text='Add', 
                         command=plus)

plus_label_name.place(x=443, y=90)
button_plus2.pack(side='left')
entry_int_plus1.pack(side='left', padx=10)
entry_int_plus2.pack(side='left', padx=10)
button_plus1.pack(side='left')
input_frame_plus.pack(pady=10)
plus_label.place(x=978, y=90)

# Minus

input_frame_minus = ttk.Frame(window)
entry_int_minus1 = tk.IntVar()
entry_int_minus1 = ttk.Entry(input_frame_minus, textvariable=entry_int_minus1)
entry_int_minus2 = tk.IntVar()
entry_int_minus2 = ttk.Entry(input_frame_minus, textvariable=entry_int_minus2)

button_minus1 = ttk.Button(input_frame_minus, 
                         text='Mns', 
                         command=minus)
# So that the screen looks nice, I added the same button again
button_minus2 = ttk.Button(input_frame_minus, 
                         text='Mns', 
                         command=minus)

minus_label_name.place(x=450, y=139)
button_minus2.pack(side='left')
entry_int_minus1.pack(side='left', padx=10)
entry_int_minus2.pack(side='left', padx=10)
button_minus1.pack(side='left')
input_frame_minus.pack(pady=10)
minus_label.place(x=980, y=140)

# Multiplication

input_frame_multiply = ttk.Frame(window)
entry_int_multiply1 = tk.IntVar()
entry_int_multiply1 = ttk.Entry(input_frame_multiply, textvariable=entry_int_multiply1)
entry_int_multiply2 = tk.IntVar()
entry_int_multiply2 = ttk.Entry(input_frame_multiply, textvariable=entry_int_multiply2)

button_multiply1 = ttk.Button(input_frame_multiply, 
                         text='Mul', 
                         command=multiply)
# So that the screen looks nice, I added the same button again
button_multiply2 = ttk.Button(input_frame_multiply, 
                         text='Mul', 
                         command=multiply)

multiply_label_name.place(x=420, y=188)
button_multiply2.pack(side='left')
entry_int_multiply1.pack(side='left', padx=10)
entry_int_multiply2.pack(side='left', padx=10)
button_multiply1.pack(side='left')
input_frame_multiply.pack(pady=10)
multiply_label.place(x=980, y=190)

# Division

input_frame_divide = ttk.Frame(window)
entry_int_divide1 = tk.IntVar()
entry_int_divide1 = ttk.Entry(input_frame_divide, textvariable=entry_int_divide1)
entry_int_divide2 = tk.IntVar()
entry_int_divide2 = ttk.Entry(input_frame_divide, textvariable=entry_int_divide2)

button_divide1 = ttk.Button(input_frame_divide,
                           text='Div',
                           command=divide)
# So that the screen looks nice, I added the same button again
button_divide2 = ttk.Button(input_frame_divide,
                           text='Div',
                           command=divide)

divide_label_name.place(x=474, y=236)
button_divide2.pack(side='left')
entry_int_divide1.pack(side='left',padx=10)
entry_int_divide2.pack(side='left', padx=10)
button_divide1.pack(side='left')
input_frame_divide.pack(pady=10)
divide_label.place(x=980, y=240)

# Power

input_frame_power = ttk.Frame(window)
entry_int_power1 = tk.IntVar()
entry_int_power1 = ttk.Entry(input_frame_power, textvariable=entry_int_power1)
entry_int_power2 = tk.IntVar()
entry_int_power2 = ttk.Entry(input_frame_power, textvariable=entry_int_power2)

button_power1 = ttk.Button(input_frame_power,
                          text='Pow',
                          command=power)
# So that the screen looks nice, I added the same button again
button_power2 = ttk.Button(input_frame_power,
                          text='Pow',
                          command=power)

power_label_name.place(x=436, y=286)
button_power2.pack(side='left')
entry_int_power1.pack(side='left', padx=10)
entry_int_power2.pack(side='left', padx=10)
button_power1.pack(side='left')
input_frame_power.pack(pady=10)
power_label.place(x=980, y=290)

# Root

input_frame_root = ttk.Frame(window)
entry_int_number = tk.IntVar()
entry_int_number = ttk.Entry(input_frame_root, textvariable=entry_int_number)
entry_int_root_degree = tk.IntVar()
entry_int_root_degree = ttk.Entry(input_frame_root, textvariable=entry_int_root_degree)

button_root1 = ttk.Button(input_frame_root,
                    text='Root',
                    command=root)
# So that the screen looks nice, I added the same button again
button_root2 = ttk.Button(input_frame_root,
                    text='Root',
                    command=root)

root_label_name.place(x=496, y=336)
button_root2.pack(side='left')
entry_int_number.pack(side='left', padx=10)
entry_int_root_degree.pack(side='left', padx=10)
button_root1.pack(side='left')
input_frame_root.pack(pady=10)
root_label.place(x=980, y=340)

# Velocity

input_frame_velocity = ttk.Frame(window)
entry_int_first_velocity = tk.IntVar()
entry_int_first_velocity = ttk.Entry(input_frame_velocity, textvariable=entry_int_first_velocity)
entry_int_acceleration = tk.IntVar()
entry_int_acceleration = ttk.Entry(input_frame_velocity, textvariable=entry_int_acceleration)
entry_int_time_velocity = tk.IntVar()
entry_int_time_velocity = ttk.Entry(input_frame_velocity, textvariable=entry_int_time_velocity)

button_velocity1 = ttk.Button(input_frame_velocity,
                          text='Velocity',
                          command=velocity)
# So that the screen looks nice, I added the same button again
button_velocity2 = ttk.Button(input_frame_velocity,
                          text='Velocity',
                          command=velocity)

velocity_label_name.place(x=377, y=384)
button_velocity2.pack(side='left')
entry_int_first_velocity.pack(side='left', padx=10)
entry_int_acceleration.pack(side='left', padx=10)
entry_int_time_velocity.pack(side='left', padx=10)
button_velocity1.pack(side='left')
input_frame_velocity.pack(pady=10)
velocity_label.place(x=1070, y=378)

# Interest

input_frame_interest = ttk.Frame(window)
entry_int_starting_money = tk.IntVar()
entry_int_starting_money = ttk.Entry(input_frame_interest, textvariable=entry_int_starting_money)
entry_int_interest_rate = tk.IntVar()
entry_int_interest_rate = ttk.Entry(input_frame_interest, textvariable=entry_int_interest_rate)
entry_int_time = tk.IntVar()
entry_int_time = ttk.Entry(input_frame_interest, textvariable=entry_int_time)

button_interest1 = ttk.Button(input_frame_interest,
                             text='Interest',
                          command=interest)
# So that the screen looks nice, I added the same button again
button_interest2 = ttk.Button(input_frame_interest,
                             text='Interest',
                          command=interest)

interest_label_name.place(x=382, y=433)
button_interest2.pack(side='left')
entry_int_starting_money.pack(side='left', padx=10)
entry_int_interest_rate.pack(side='left', padx=10)
entry_int_time.pack(side='left', padx=10)
button_interest1.pack(side='left')
input_frame_interest.pack(pady=10)
interest_label.place(x=1070, y=428)

# Installment

input_frame_installment = ttk.Frame(window)
entry_int_cost = tk.IntVar()
entry_int_cost = ttk.Entry(input_frame_installment, textvariable=entry_int_cost)
entry_int_month = tk.IntVar()
entry_int_month = ttk.Entry(input_frame_installment, textvariable=entry_int_month)

button_installment1 = ttk.Button(input_frame_installment,
                             text='Installment',
                          command=installment)
# So that the screen looks nice, I added the same button again
button_installment2 = ttk.Button(input_frame_installment,
                             text='Installment',
                          command=installment)
installment_label_name.place(x=406, y=482)
button_installment2.pack(side='left')
entry_int_cost.pack(side='left', padx=10)
entry_int_month.pack(side='left', padx=10)
button_installment1.pack(side='left')
input_frame_installment.pack(pady=10)
installment_label.place(x=1012, y=487)

# Income Tax

input_frame_income_tax = ttk.Frame(window)
entry_int_earning = tk.IntVar()
entry_int_earning = ttk.Entry(input_frame_income_tax, textvariable=entry_int_earning)

button_income_tax1 = ttk.Button(input_frame_income_tax,
                             text='Income Tax',
                          command=income_tax)
# So that the screen looks nice, I added the same button again
button_income_tax2 = ttk.Button(input_frame_income_tax,
                             text='Income Tax',
                          command=income_tax)

income_tax_label_name.place(x=480, y=531)
button_income_tax2.pack(side='left')
entry_int_earning.pack(side='left', padx=10)
button_income_tax1.pack(side='left')
input_frame_income_tax.pack(pady=10)
income_tax_label.place(x=936, y=535)




# Clear

clear_button = ttk.Button(window, 
                          text='Clear', 
                          command= clear_and_play_sound)
clear_button.pack(pady=10)




# Result

result_label = ttk.Label(window, 
                         text='The result will be shown here kıps ;)', 
                         font=('Arial', 16))
result_label.pack(pady=90)



# Run the main loop

window.mainloop()