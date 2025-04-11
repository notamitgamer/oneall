import tkinter as tk
import random

#def functions 

def sum_of_digit() :

    #functions

    def calculation_sod() :
        error_sod.config(text = "")
        result_sod.config(text='')
        try:
            inp = int(input_sod.get())
            sum = 0
            temp1 = inp
            while temp1 != 0:
                temp2 = temp1 % 10
                sum += temp2
                temp1 = temp1 // 10
            result_sod.config(text=f'Sum of digit {inp} is {sum}.')
        except ValueError:
            error_sod.config(text = "Please enter valid integer numbers.")
            return None

    #window setting

    win_sod = tk.Toplevel(window)
    win_sod.title('Sum Of Digit')
    win_sod.configure(bg='#242432')
    win_sod.attributes("-fullscreen", True)
    win_sod.columnconfigure(0, weight= 1)
    win_sod.columnconfigure(1, weight= 1)

    #label

    header_label_sod = tk.Label(win_sod,text='\n\n\n\nSum Of Digit', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label_sod.grid(row=0, column=0, columnspan=2, padx=1, pady=20)

    inp_label_sod = tk.Label(win_sod,text='Enter input : ', font=('Arial', 15, 'bold'), fg='white', bg='#242432')
    inp_label_sod.grid(row=1,column=0,padx=1,pady=20,sticky='ew')

    #input

    input_sod = tk.Entry(win_sod,font=('Arial', 15, 'bold'),width=20, fg='white', bg='#242432') # Changed input background to white for better visibility
    input_sod.grid(row=1,column=1,padx=1,pady=5)

    #buttons

    calculation_button_sod = tk.Button(win_sod,text = 'Submit',font=('Arial', 13, 'bold'), fg='white', bg='#37374D',command=calculation_sod,relief='flat')
    calculation_button_sod.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

    close_button_sod = tk.Button(win_sod,text='close window',command=win_sod.destroy,font=('Arial', 13, 'bold'), fg='white', bg='#37374D',relief='flat')
    close_button_sod.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

    #output

    result_sod = tk.Label(win_sod, text='', font=('Arial', 15, 'bold'), fg='Green', bg='#242432')
    result_sod.grid(row=3, column=0, columnspan=2, padx=5, pady=0, sticky='ew')

    error_sod = tk.Label(win_sod, text='', font=('Arial', 15, 'bold'), fg='Red', bg='#242432')
    error_sod.grid(row=4, column=0, columnspan=2, padx=5, pady=0, sticky='ew')


def simple() :
    
    #functions

    def input_entry():
        error_label.config(text="")
        result_label.config(text='')
        try:
            input1 = int(input_entry_1.get())
            input2 = int(input_entry_2.get())
            return input1, input2
        except ValueError:
            error_label.config(text="Enter a valid integer number.")
            return None, None

    def addition():
        error_label.config(text="")
        result_label.config(text='')
        inp1, inp2 = input_entry()
        if inp1 is not None and inp2 is not None:
            result = inp1 + inp2
            result_label.config(text=f'Addition of {inp1} and {inp2} is {result}')

    def subtraction():
        error_label.config(text="")
        result_label.config(text='')
        inp1, inp2 = input_entry()
        if inp1 is not None and inp2 is not None:
            result = inp1 - inp2
            result_label.config(text=f'Subtraction of {inp1} and {inp2} is {result}')

    def multiplication():
        error_label.config(text="")
        result_label.config(text='')
        inp1, inp2 = input_entry()
        if inp1 is not None and inp2 is not None:
            result = inp1 * inp2
            result_label.config(text=f'Multiplication of {inp1} and {inp2} is {result}')

    def division():
        error_label.config(text="")
        result_label.config(text='')
        inp1, inp2 = input_entry()
        if inp1 is not None and inp2 is not None:
            if inp2 == 0:
                error_label.config(text='Cannot be divided by Zero')
                return
            result = inp1 / inp2
            result_label.config(text=f'Division of {inp1} and {inp2} is {result}')

    def average():
        error_label.config(text="")
        result_label.config(text='')
        inp1, inp2 = input_entry()
        if inp1 is not None and inp2 is not None:
            result = (inp1 + inp2) / 2
            result_label.config(text=f'Average of {inp1} and {inp2} is {result}')

    def reset():
        input_entry_1.delete(0, tk.END)
        input_entry_2.delete(0, tk.END)
        result_label.config(text='')
        error_label.config(text='')

    #window settings

    win_simple = tk.Toplevel(window)
    win_simple.title('Simple Calculator')
    win_simple.configure(bg='#242432')
    win_simple.attributes("-fullscreen", True)
    win_simple.columnconfigure(0, weight=1)
    win_simple.columnconfigure(1, weight=1)

    # Header

    header = tk.Label(win_simple, text='\n\n\nSimple Calculator', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    # Input labels

    inp_label_1 = tk.Label(win_simple, text='Enter 1st number : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    inp_label_1.grid(row=1, column=0, padx=15, pady=15, sticky='ew')

    inp_label_2 = tk.Label(win_simple, text='Enter 2nd number : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    inp_label_2.grid(row=2, column=0, padx=15, pady=15, sticky='ew')

    # Entry fields

    input_entry_1 = tk.Entry(win_simple, font=('Arial', 15), width=20, bg='#242432', fg='white', insertbackground='white')
    input_entry_1.grid(row=1, column=1, padx=3, pady=15)

    input_entry_2 = tk.Entry(win_simple, font=('Arial', 15), width=20, bg='#242432', fg='white', insertbackground='white')
    input_entry_2.grid(row=2, column=1, padx=3, pady=15)

    # Buttons

    button_addition = tk.Button(win_simple, text='Addition', font=('Arial', 10,'bold'), command=addition, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    button_addition.grid(row=3, column=0, padx=15, pady=15, sticky='ew')

    button_subtraction = tk.Button(win_simple, text='Subtraction', font=('Arial', 10,'bold'), command=subtraction, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    button_subtraction.grid(row=3, column=1, padx=15, pady=15, sticky='ew')

    button_multiplication = tk.Button(win_simple, text='Multiplication', font=('Arial', 10,'bold'), command=multiplication, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    button_multiplication.grid(row=4, column=0, padx=15, pady=15, sticky='ew')

    button_division = tk.Button(win_simple, text='Division', font=('Arial', 10,'bold'), command=division, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    button_division.grid(row=4, column=1, padx=15, pady=15, sticky='ew')

    button_average = tk.Button(win_simple, text='Average', font=('Arial', 10,'bold'), command=average, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    button_average.grid(row=5, column=0, padx=15, pady=15, sticky='ew')

    button_reset = tk.Button(win_simple, text='Clear All', font=('Arial', 10,'bold'), command=reset, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    button_reset.grid(row=5, column=1, padx=15, pady=15, sticky='ew')

    close_button = tk.Button(win_simple, text='close window', command=win_simple.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=8, column=0, columnspan=2, padx=5, pady=20)

    # Result and Error labels

    result_label = tk.Label(win_simple, text='', font=('Arial', 15, 'bold'), fg='Green', bg='#242432')
    result_label.grid(row=6, column=0, columnspan=2, padx=15, pady=0, sticky='ew')

    error_label = tk.Label(win_simple, text='', font=('Arial', 15, 'bold'), fg='Red', bg='#242432')
    error_label.grid(row=7, column=0, columnspan=2, padx=15, pady=0, sticky='ew')


def odd_even() :

    #functions

    def check_odd_even():
        result_oe.config(text='')
        error_oe.config(text="")
        try:
            inp = int(input_oe.get())
            if inp % 2 == 0:
                result_oe.config(text=f'Input {inp} is an EVEN number.')
            else:
                result_oe.config(text=f'Input {inp} is an ODD number.')
        except ValueError:
            error_oe.config(text="Enter a valid integer number.")

    #window settings        

    win_oe = tk.Toplevel(window)
    win_oe.title("Odd or Even")
    win_oe.configure(bg="#242432")
    win_oe.attributes("-fullscreen", True)
    win_oe.columnconfigure(0, weight=1)
    win_oe.columnconfigure(1, weight=1)

    #labels and buttons

    header_oe = tk.Label(win_oe, text="\n\n\n\n\nOdd or Even Checker", font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_oe.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    input_label_oe = tk.Label(win_oe, text="Enter Number : ", font=("Arial", 12,'bold'), bg="#242432", fg='white')
    input_label_oe.grid(row=1, column=0, padx=0, pady=5)

    input_oe = tk.Entry(win_oe,font=('Arial', 13, 'bold'),width=20, fg='white', bg='#242432', insertbackground='white')
    input_oe.grid(row=1, column=1, padx=0, pady=5)

    check_button_oe = tk.Button(win_oe, text="Check", command=check_odd_even, font=("Arial", 12,'bold'), bg="#37374D", fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    check_button_oe.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    result_oe = tk.Label(win_oe, text="", font=('Arial', 15, 'bold'), fg='Green', bg='#242432')
    result_oe.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_oe = tk.Label(win_oe, text="", font=('Arial', 15, 'bold'), fg='Red', bg='#242432')
    error_oe.grid(row=4, column=0, columnspan=2, padx=5, pady=0)

    close_button_oe = tk.Button(win_oe, text='close window', command=win_oe.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button_oe.grid(row=5,column=0,columnspan=2,padx=5,pady=5)


def reverse_string() :

    #functions

    def reverse_input_string():
        result_label.config(text='')
        error_label.config(text='')
        try:
            input_text = input_string.get()
            reversed_str = ""
            for char in input_text:
                reversed_str = char + reversed_str
            result_label.config(text=f'Reverse of "{input_text}" is "{reversed_str}".')

        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_reverse = tk.Toplevel(window)
    win_reverse.title('Reverse String')
    win_reverse.configure(bg='#242432')
    win_reverse.attributes("-fullscreen", True)
    win_reverse.columnconfigure(0, weight=1)
    win_reverse.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_reverse, text='\n\n\n\nReverse String', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_string_label = tk.Label(win_reverse, text='Enter a string: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_string_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_string = tk.Entry(win_reverse, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_string.grid(row=1, column=1, padx=5, pady=5)

    #buttons

    reverse_button = tk.Button(win_reverse, text='Reverse', font=('Arial', 13, 'bold'), command=reverse_input_string, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    reverse_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_reverse, text='close window', command=win_reverse.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #output

    result_label = tk.Label(win_reverse, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_reverse, text='', font=('Arial', 15, 'bold'), fg='Red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def largest_element() :

    #functions

    def find_largest():
        error_label.config(text="")
        result_label.config(text='')
        try:
            total = int(input_total.get())
            element_string = input_element.get()
            element_list = element_string.split(',') # Split the comma separated string
            input_list = [int(element.strip()) for element in element_list] # Convert each element to int, remove white space.

            if len(input_list) != total:
                error_label.config(text = f"Please enter {total} elements")
                return
            
            if len(input_list) < 2:
                error_label.config(text='Please enter at least two elements.')
                return

            if not input_list:
                error_label.config(text="Please enter some elements.")
                return

            first_element = input_list[0]
            all_same = True
            for item in input_list:
                if item != first_element:
                    all_same = False
                    break

            if all_same:
                error_label.config(text='There is no Largest element ( All elements are the same ).')
            else:
                max_val = input_list[0]
                for item in input_list:
                    if max_val < item:
                        max_val = item
                result_label.config(text=f'Largest element is {max_val}.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter integers.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_largest = tk.Toplevel(window)
    win_largest.title('Largest Element')
    win_largest.configure(bg='#242432')
    win_largest.attributes("-fullscreen", True)
    win_largest.columnconfigure(0, weight=1)
    win_largest.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_largest, text='\n\n\n\nLargest Element', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_total_label = tk.Label(win_largest, text='How many elements? : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_total_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_total = tk.Entry(win_largest, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_total.grid(row=1, column=1, padx=5, pady=5)

    input_element_label = tk.Label(win_largest, text='Enter elements (comma separated): ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_element_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

    input_element = tk.Entry(win_largest, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_element.grid(row=2, column=1, padx=5, pady=5)

    #buttons

    calculate_button = tk.Button(win_largest, text='Calculate', font=('Arial', 13, 'bold'), command=find_largest, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_largest, text='close window', command=win_largest.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    #output
    
    result_label = tk.Label(win_largest, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_largest, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=6, column=0, columnspan=2, padx=5, pady=0)


def second_largest() :

    #functions

    def find_second_largest():
        error_label.config(text="")
        result_label.config(text="")
        try:
            total = int(input_total.get())
            element_string = input_element.get() # Get the string from the entry
            element_list = element_string.split(',') # Split the string
            input_list = [int(element.strip()) for element in element_list] # Convert to int

            if len(input_list) != total:
                error_label.config(text=f'Please enter {total} elements.')
                return

            if len(input_list) < 2:
                error_label.config(text='Please enter at least two elements.')
                return

            unique_elements = sorted(list(set(input_list)), reverse=True)

            if len(unique_elements) < 2:
                error_label.config(text=f'No second largest element ( all elements are the same ).')
            else:
                second_largest_val = unique_elements[1]
                result_label.config(text=f'Second largest element is {second_largest_val}.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter integers.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_second = tk.Toplevel(window)
    win_second.title('Second Largest')
    win_second.configure(bg='#242432')
    win_second.attributes("-fullscreen", True)
    win_second.columnconfigure(0, weight=1)
    win_second.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_second, text='\n\n\n\nSecond Largest', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_total_label = tk.Label(win_second, text='How many elements? : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_total_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_total = tk.Entry(win_second, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_total.grid(row=1, column=1, padx=5, pady=5)

    input_element_label = tk.Label(win_second, text='Enter elements (comma separated): ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_element_label.grid(row=2, column=0,  padx=5, pady=5, sticky='ew')

    input_element = tk.Entry(win_second, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_element.grid(row=2, column=1, padx=5, pady=5)

    #buttons

    calculate_button = tk.Button(win_second, text='Calculate', font=('Arial', 13, 'bold'), command=find_second_largest, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_second, text='close window', command=win_second.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_second, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_second, text='', font=('Arial', 15, 'bold'), fg='Red', bg='#242432')
    error_label.grid(row=6, column=0, columnspan=2, padx=5, pady=0)


def fibonacci_series() :

    #functions

    def generate_fibonacci():
        error_label.config(text="")
        result_label.config(text='')
        try:
            inp = int(input_entry.get())
            temp1 = 0
            temp2 = 1
            fib_series = f'Fibonacci series upto {inp} is \n{temp1}   {temp2}'

            if inp > 2 :
                for _ in range(0, inp - 2):
                    next_num = temp1 + temp2
                    temp1, temp2 = temp2, next_num
                    fib_series += f'   {next_num}'
            elif inp < 1:
                error_label.config(text = "Please enter a positive integer.")
                return

            result_label.config(text=fib_series)

        except ValueError:
            error_label.config(text="Invalid input. Please enter an integer.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_fibonacci = tk.Toplevel(window)
    win_fibonacci.title('Fibonacci Series')
    win_fibonacci.configure(bg='#242432')
    win_fibonacci.attributes("-fullscreen", True)
    win_fibonacci.columnconfigure(0, weight=1)
    win_fibonacci.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_fibonacci, text='\n\n\n\nFibonacci Series', font=('Georgia', 30, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_fibonacci, text='Enter a number : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=0, sticky='ew')

    input_entry = tk.Entry(win_fibonacci, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=0)

    safe_input_label = tk.Label(win_fibonacci, text='( safe range : 25 )', font=('Arial', 13, 'bold'), bg='#242432', fg='red')
    safe_input_label.grid(row=2, column=0, padx=5, pady=0, sticky='ew')

    #buttons

    generate_button = tk.Button(win_fibonacci, text='Generate', font=('Arial', 13, 'bold'), command=generate_fibonacci, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_fibonacci, text='close window', command=win_fibonacci.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_fibonacci, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_fibonacci, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=5, column=0, columnspan=2, padx=5, pady=0)


def palindrome_check() :

    #functions

    def check_palindrome():
        result_label.config(text='')
        error_label.config(text='')
        try:
            inp = int(input_entry.get())
            temp1 = inp
            temp2 = 0
            while temp1 != 0:
                a = temp1 % 10
                temp2 = (temp2 * 10) + a
                temp1 = temp1 // 10
            if temp2 == inp:
                result_label.config(text=f'Input {inp} is a Palindrome number.')
            else:
                result_label.config(text=f'Input {inp} is not a Palindrome number.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter an integer.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_palindrome = tk.Toplevel(window)
    win_palindrome.title('Palindrome Check')
    win_palindrome.configure(bg='#242432')
    win_palindrome.attributes("-fullscreen", True)
    win_palindrome.columnconfigure(0, weight=1)
    win_palindrome.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_palindrome, text='\n\n\n\nPalindrome Check', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_palindrome, text='Enter a number: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_palindrome, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=5)

    #buttons

    check_button = tk.Button(win_palindrome, text='Check', font=('Arial', 13, 'bold'), command=check_palindrome, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    check_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_palindrome, text='close window', command=win_palindrome.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_palindrome, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_palindrome, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def unique_elements() :

    #functions

    def find_unique():
        result_label.config(text='')
        error_label.config(text='')
        try:
            limit = int(input_limit.get())
            element_string = input_element.get()
            element_list = element_string.split(',')
            inp = [int(element.strip()) for element in element_list]

            if len(inp) != limit:
                error_label.config(text=f'Please enter {limit} elements.')
                return

            unique_list = []
            for item in inp:
                if item not in unique_list:
                    unique_list.append(item)
            result_label.config(text=f'Unique elements: {unique_list}')

        except ValueError:
            error_label.config(text="Invalid input. Please enter integers.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_unique = tk.Toplevel(window)
    win_unique.title('Unique Elements')
    win_unique.configure(bg='#242432')
    win_unique.attributes("-fullscreen", True)
    win_unique.columnconfigure(0, weight=1)
    win_unique.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_unique, text='\n\n\n\nUnique Elements', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_limit_label = tk.Label(win_unique, text='How many elements? : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_limit_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_limit = tk.Entry(win_unique, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_limit.grid(row=1, column=1, padx=5, pady=5)

    input_element_label = tk.Label(win_unique, text='Enter elements (comma separated): ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_element_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

    input_element = tk.Entry(win_unique, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_element.grid(row=2, column=1, padx=5, pady=5)

    #buttons

    find_button = tk.Button(win_unique, text='Find Unique', font=('Arial', 13, 'bold'), command=find_unique, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    find_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_unique, text='close window', command=win_unique.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_unique, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_unique, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=6, column=0, columnspan=2, padx=5, pady=0)


def prime_check() :

    #functions

    def check_prime_number():
        result_label.config(text='')
        error_label.config(text='')
        try:
            inp = int(input_entry.get())
            is_prime = True  # Assume prime initially
            if inp < 2:
                is_prime = False
            else:
                for item in range(2, int(inp**0.5) + 1):  # Optimized range
                    if inp % item == 0:
                        is_prime = False
                        break  # No need to continue checking

            if is_prime:
                result_label.config(text=f'Input {inp} is a prime number.')
            else:
                result_label.config(text=f'Input {inp} is not a prime number.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter an integer.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_prime = tk.Toplevel(window)
    win_prime.title('Prime Check')
    win_prime.configure(bg='#242432')
    win_prime.attributes("-fullscreen", True)
    win_prime.columnconfigure(0, weight=1)
    win_prime.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_prime, text='\n\n\n\nPrime Check', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_prime, text='Enter a number: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_prime, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=5)

    #buttons

    check_button = tk.Button(win_prime, text='Check', font=('Arial', 13, 'bold'), command=check_prime_number, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    check_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_prime, text='close window', command=win_prime.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_prime, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_prime, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def factorial_calculation() :

    #functions

    def calculate_factorial():
        result_label.config(text = '')
        error_label.config(text = '')
        try:
            inp = int(input_entry.get())

            def check_factorial(n):
                if n < 0:
                    error_label.config(text="Factorial is not defined for negative numbers.")
                    return None
                elif n == 0:
                    return 1
                else:
                    return n * check_factorial(n - 1)

            factorial_result = check_factorial(inp)
            if factorial_result is not None:
                result_label.config(text=f'Factorial of {inp} is {factorial_result}.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter an integer.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_factorial = tk.Toplevel(window)
    win_factorial.title('Factorial Calculation')
    win_factorial.configure(bg='#242432')
    win_factorial.attributes("-fullscreen", True)
    win_factorial.columnconfigure(0, weight=1)
    win_factorial.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_factorial, text='\n\n\n\nFactorial Calculation', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_factorial, text='Enter a number: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_factorial, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=5)

    #buttons

    calculate_button = tk.Button(win_factorial, text='Calculate', font=('Arial', 13, 'bold'), command=calculate_factorial, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_factorial, text='close window', command=win_factorial.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #result label

    result_label = tk.Label(win_factorial, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_factorial, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def multiplication_table() :

    #functions

    def generate_table():
        result_label.config(text='')
        error_label.config(text='')
        try:
            inp = int(input_number.get())
            rnge = int(input_range.get())

            table_text = f'\nBelow is the multiplication table of {inp} upto {rnge} : \n'
            for item in range(1, rnge + 1):
                table_text += f'{inp} x {item} = {item * inp}\n'

            result_label.config(text=table_text)

        except ValueError:
            error_label.config(text="Invalid input. Please enter integers.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_multiplication = tk.Toplevel(window)
    win_multiplication.title('Multiplication Table')
    win_multiplication.configure(bg='#242432')
    win_multiplication.attributes("-fullscreen", True)
    win_multiplication.columnconfigure(0, weight=1)
    win_multiplication.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_multiplication, text='Multiplication Table', font=('Georgia', 30, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_number_label = tk.Label(win_multiplication, text='Enter a number: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_number_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_number = tk.Entry(win_multiplication, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_number.grid(row=1, column=1, padx=5, pady=5)

    input_range_label = tk.Label(win_multiplication, text='Enter range : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_range_label.grid(row=2, column=0, padx=5, pady=0, sticky='ew')

    input_range = tk.Entry(win_multiplication, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_range.grid(row=2, column=1, padx=0, pady=5)

    safe_range_label = tk.Label(win_multiplication, text='( safe range : 15 )', font=('Arial', 13, 'bold'), bg='#242432', fg='red')
    safe_range_label.grid(row=3, column=0, padx=5, pady=0, sticky='ew')

    #buttons

    generate_button = tk.Button(win_multiplication, text='Generate Table', font=('Arial', 13, 'bold'), command=generate_table, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    close_button = tk.Button(win_multiplication, text='close window', command=win_multiplication.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=7, column=0, columnspan=2, padx=5, pady=0)

    #output

    result_label = tk.Label(win_multiplication, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_multiplication, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=6, column=0, columnspan=2, padx=5, pady=0)


def armstrong_check() :

    #functions

    def check_armstrong():
        result_label.config(text='')
        error_label.config(text='')
        try:
            inp = int(input_entry.get())
            s_inp = str(inp)
            length = len(s_inp)
            sum_digits = 0
            for digit in s_inp:
                sum_digits += int(digit) ** length

            if sum_digits == inp:
                result_label.config(text=f'Input {inp} is an Armstrong Number.')
            else:
                result_label.config(text=f'Input {inp} is not an Armstrong Number.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter an integer.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_armstrong = tk.Toplevel(window)
    win_armstrong.title('Armstrong Check')
    win_armstrong.configure(bg='#242432')
    win_armstrong.attributes("-fullscreen", True)
    win_armstrong.columnconfigure(0, weight=1)
    win_armstrong.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_armstrong, text='\n\n\n\nArmstrong Check', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_armstrong, text='Enter a number: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_armstrong, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=5)

    #buttons

    check_button = tk.Button(win_armstrong, text='Check', font=('Arial', 13, 'bold'), command=check_armstrong, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    check_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_armstrong, text='close window', command=win_armstrong.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_armstrong, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_armstrong, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def guessing_game() :

    #functions

    def check_guess():
        result_label.config(text='')
        error_label.config(text='')
        try:
            guess = int(input_entry.get())

            if guess > 100 or guess < 1:
                error_label.config(text='Enter a valid choice between 1 to 100.')
                return

            if guess > actual_guess[0]:
                result_label.config(text='Too High!!! Try Again.')
                guess_count[0] += 1
            elif guess < actual_guess[0]:
                result_label.config(text='Too Low!!! Try Again.')
                guess_count[0] += 1
            else:
                result_label.config(text=f'Congratulations!! 🎉🎉 You made it in just {guess_count[0]} try.')
                guess_count[0] = 1 # Reset for new game
                actual_guess[0] = random.randint(1, 100) # New random number

        except ValueError:
            error_label.config(text="Invalid input. Please enter an integer.")
        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_guessing = tk.Toplevel(window)
    win_guessing.title('Guessing Game')
    win_guessing.configure(bg='#242432')
    win_guessing.attributes('-fullscreen', True)
    win_guessing.columnconfigure(0, weight=1)
    win_guessing.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_guessing, text='\n\n\n\nGuessing Game', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_guessing, text='Enter your choice (1-100): ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_guessing, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=5)

    #variables
    guess_count = [1]
    actual_guess = [random.randint(1, 100)]

    #buttons

    guess_button = tk.Button(win_guessing, text='Guess', font=('Arial', 13, 'bold'), command=check_guess, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    guess_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_guessing, text='close window', command=win_guessing.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #output
    result_label = tk.Label(win_guessing, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_guessing, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def vowel_consonant_count() :

    #functions

    def count_vowels_consonants():
        result_label.config(text='')
        error_label.config(text='')
        try:
            string = input_entry.get()
            inp = string.lower()
            vowel_count = 0
            consonant_count = 0
            for char in inp:
                if 'a' <= char <= 'z':  # Check if it's an alphabet
                    if char in 'aeiou':
                        vowel_count += 1
                    else:
                        consonant_count += 1
            result_label.config(text=f'Your string "{string}" has {vowel_count} Vowels and {consonant_count} Consonants.')

        except Exception as e:
            error_label.config(text=f"An error occurred: {e}")

    #window setting

    win_vowel_consonant = tk.Toplevel(window)
    win_vowel_consonant.title('Vowel Consonant Count')
    win_vowel_consonant.configure(bg='#242432')
    win_vowel_consonant.attributes('-fullscreen',True)
    win_vowel_consonant.columnconfigure(0, weight=1)
    win_vowel_consonant.columnconfigure(1, weight=1)

    #label

    header_label = tk.Label(win_vowel_consonant, text='\n\n\n\nVowel Consonant Count', font=('Georgia', 25, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    input_label = tk.Label(win_vowel_consonant, text='Enter the string: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_vowel_consonant, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=1, column=1, padx=5, pady=5)

    #buttons

    count_button = tk.Button(win_vowel_consonant, text='Count', font=('Arial', 13, 'bold'), command=count_vowels_consonants, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    count_button.grid(row=2, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_vowel_consonant, text='close window', command=win_vowel_consonant.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    #output

    result_label = tk.Label(win_vowel_consonant, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_vowel_consonant, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=0)


def even_list() :

    # Functions

    def check_even_list():
        result_label.config(text='')
        error_label.config(text='')
        try:
            start = int(starting_from_entry.get())
            end = int(ending_entry.get())

            if end <= start:
                error_label.config(text="Ending value should be greater than the starting value.")
                return

            if (end - start) > 70:
                error_label.config(text="Please maintain a SAFE difference of 70 between starting and ending values.")
                return

            even_numbers = []
            for item in range(start + 1, end):
                if item % 2 == 0:
                    even_numbers.append(item)

            if even_numbers:
                result_label.config(text=f'Even numbers in the range of {start} and {end} are:\n{even_numbers}')
            else:
                result_label.config(text=f'Even numbers in the range of {start} and {end} not found.')

        except ValueError:
            error_label.config(text="Invalid input. Please enter integers for the start and end values.")
        except Exception as e:
            error_label.config(text=f'An error occurred: {e}')

    # Window setting for the even list window

    win_even = tk.Toplevel(window)
    win_even.title('Even list')
    win_even.configure(bg='#242432')
    win_even.attributes('-fullscreen', True)
    win_even.columnconfigure(0, weight=1)
    win_even.columnconfigure(1, weight=1)

    # Labels

    header_label = tk.Label(win_even, text='\n\n\nEven List', font=('Georgia', 30, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

    safe_header_label = tk.Label(win_even, text='\n\nPlease maintain a SAFE difference between starting and ending\n', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    safe_header_label.grid(row=1, column=0, columnspan=2, padx=20, pady=0)

    starting_from_label = tk.Label(win_even, text='Starting from : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    starting_from_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

    starting_from_entry = tk.Entry(win_even, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    starting_from_entry.grid(row=2, column=1, padx=5, pady=5)

    ending_label = tk.Label(win_even, text='Ending at : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    ending_label.grid(row=4, column=0, padx=5, pady=5, sticky='ew')

    ending_entry = tk.Entry(win_even, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    ending_entry.grid(row=4, column=1, padx=5, pady=5)
    
    safe_header_label_2 = tk.Label(win_even, text='(SAFE difference : 70)', font=('Arial', 13, 'bold'), fg='red', bg='#242432')
    safe_header_label_2.grid(row=5, column=0, padx=20, pady=0)

    # Buttons

    get_button = tk.Button(win_even, text='Get', font=('Arial', 13, 'bold'), command=check_even_list, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    get_button.grid(row=6, column=0, columnspan=2, padx=5, pady=20)

    close_button = tk.Button(win_even, text='close window', command=win_even.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    # Output labels

    result_label = tk.Label(win_even, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_even, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=8, column=0, columnspan=2, padx=5, pady=0)


def string_operation() :
    
    # functions

    def check_uppercase() :
        result_label.config(text = '')
        error_label.config(text = '')
        try : 
            inp = input_entry.get()
            temp = inp 
            if inp == temp.upper() :
                result_label.config(text = f'All character in String "{inp}" are in UPPERCASE.')
            else :
                result_label.config(text = f'NOT all character in String "{inp}" are in UPPERCASE.')
        
        except Exception :
            error_label.config(text = f'An error occurred') 


    def vowel_start() :
        result_label.config(text = '')
        error_label.config(text = '')
        try : 
            inp = input_entry.get()
            temp = inp[0]
            result = 0
            for char in 'aeiou' :
                if char == temp.lower() :
                    result_label.config(text = f'Input String "{inp}" is starting with a vowel.')
                    result = 1
                    break

            if result == 0 :
                result_label.config(text = f'Input String "{inp}" is not starting with a vowel.')
        
        except Exception :
            error_label.config(text = f'An error occurred') 

        
    def reverse_input() :
        result_label.config(text = '')
        error_label.config(text = '')
        try : 
            reverse = ''
            inp = input_entry.get()
            for char in inp :
                reverse = char + reverse
            result_label.config(text = f'Reverse of "{inp}" is "{reverse}".')

        except Exception as e :
            error_label.config(text = f'An error occurred {e}') 

    # Window setting
    
    win_string = tk.Toplevel(window)
    win_string.title('Even list')
    win_string.configure(bg='#242432')
    win_string.attributes('-fullscreen', True)
    win_string.columnconfigure(0, weight=1)
    win_string.columnconfigure(1, weight=1)

    # Labels

    header_label = tk.Label(win_string, text='\n\n\nString Operation', font=('Georgia', 30, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

    safe_header_label = tk.Label(win_string, text='\n\nThis was a test given by Gemini AI\n', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    safe_header_label.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    input_label = tk.Label(win_string, text='Enter the string : ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_string, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=2, column=1, padx=5, pady=5)


    # Buttons

    get1_button = tk.Button(win_string, text='Check Uppercase', font=('Arial', 13, 'bold'), command=check_uppercase, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    get1_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    get2_button = tk.Button(win_string, text='Check vowel', font=('Arial', 13, 'bold'), command=vowel_start, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    get2_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    get3_button = tk.Button(win_string, text='Reverse string', font=('Arial', 13, 'bold'), command=reverse_input, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    get3_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    close_button = tk.Button(win_string, text='Close window', command=win_string.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    # Output labels

    result_label = tk.Label(win_string, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_string, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=7, column=0, columnspan=2, padx=5, pady=0)


def text_file_handling() :

    #functions

    def find_highest_scorer():

        result_label.config(text='')
        error_label.config(text='')
        try:
            filename = input_entry.get()
            highest_score = -1
            toppers = []  # Initialize a list to store toppers
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        try:
                            if len(parts) == 2:
                                name, number = parts
                                score = int(number)
                                if score > highest_score:
                                    highest_score = score
                                    toppers = [(name, score)]  # Reset toppers list with the new highest scorer
                                elif score == highest_score:
                                    toppers.append((name, score))  # Add to the toppers list if score is equal
                            else:
                                error_label.config(text=f"Warning: Skipping invalid data....")
                        except ValueError:
                            error_label.config(text=f"Warning: Skipping invalid data....")

            if toppers:

                if len(toppers) == 1:
                    name, score = toppers[0]
                    result_label.config(text=f"The student with the highest score is: {name} ({score})")

                else:
                    toppers_info = "\n".join([f"{name} ({score})" for name, score in toppers])
                    result_label.config(text=f"The students with the highest score are:\n{toppers_info}")

            else:
                error_label.config(text="No valid student scores found in the file.")

        except FileNotFoundError:
            error_label.config(text=f"Error: File '{filename}' not found.")

        except Exception as e:
            error_label.config(text=f"An unexpected error occurred: {e}")


    # Window setting

    win_text_file = tk.Toplevel(window)
    win_text_file.title('Text File Handling')
    win_text_file.configure(bg='#242432')
    win_text_file.attributes('-fullscreen', True)
    win_text_file.columnconfigure(0, weight=1)
    win_text_file.columnconfigure(1, weight=1)

    # Labels

    header_label = tk.Label(win_text_file, text='\n\n\n\nFind the Highest Scorer', font=('Georgia', 30, 'bold'), fg='white', bg='#242432')
    header_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

    safe_header_label = tk.Label(win_text_file, text='This was a test given by Gemini AI\n', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    safe_header_label.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    input_label = tk.Label(win_text_file, text='Enter the filename: ', font=('Arial', 15, 'bold'), bg='#242432', fg='white')
    input_label.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

    input_entry = tk.Entry(win_text_file, font=('Arial', 15), bg='#242432', fg='white', insertbackground='white')
    input_entry.grid(row=2, column=1, padx=5, pady=5)


    # Buttons

    do_button = tk.Button(win_text_file, text='Check Topper', font=('Arial', 13, 'bold'), command=find_highest_scorer, bg='#37374D', fg='white', relief='flat', activebackground='#4D4D64', activeforeground='white')
    do_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    close_button = tk.Button(win_text_file, text='Close window', command=win_text_file.destroy, font=('Arial', 13, 'bold'), fg='white', bg='#37374D', relief='flat', activebackground='#4D4D64', activeforeground='white')
    close_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    # Output labels

    result_label = tk.Label(win_text_file, text='', font=('Arial', 15, 'bold'), fg='green', bg='#242432')
    result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=0)

    error_label = tk.Label(win_text_file, text='', font=('Arial', 15, 'bold'), fg='red', bg='#242432')
    error_label.grid(row=7, column=0, columnspan=2, padx=5, pady=0)


#creating the main window

window = tk.Tk()
window.title('All in one')
window.configure(bg='#242432')
window.attributes("-fullscreen", True)

# Column configure to expand if needed

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Content window here...

# Header label

header_label = tk.Label(window, text='\nContents', font=('Garamond', 50, 'bold'), fg='white', bg='#242432')
header_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky='ew') 

# Style constants

button_bg = '#37374D'
button_fg = 'white'
button_font = ('Arial', 12, 'bold')
button_padx = 0
button_pady = 0
button_sticky = 'nsew'
button_relief = tk.FLAT
button_width = 13
button_height = 2

# Button creation

button_simple = tk.Button(window, text='simple', command=simple)
button_sod = tk.Button(window, text='Sum of Digit', command=sum_of_digit)
button_oe = tk.Button(window, text='Odd Even Check', command=odd_even)
button_reverse = tk.Button(window, text='Reverse String', command=reverse_string)
button_largest = tk.Button(window, text='Largest Element', command=largest_element)
button_second_largest = tk.Button(window, text='Second Largest', command=second_largest)
button_fibonacci = tk.Button(window, text='Fibonacci Series', command=fibonacci_series)
button_palindrome = tk.Button(window, text='Palindrome Check', command=palindrome_check)
button_unique = tk.Button(window, text='Unique Elements', command=unique_elements)
button_prime = tk.Button(window, text='Prime Check', command=prime_check)
button_factorial = tk.Button(window, text='Factorial', command=factorial_calculation)
button_multiplication = tk.Button(window, text='Multiplication Table', command=multiplication_table)
button_armstrong = tk.Button(window, text='Armstrong Check', command=armstrong_check)
button_guessing = tk.Button(window, text='Guessing Game', command=guessing_game)
button_vowel_consonant = tk.Button(window, text='Vowel Consonant Count', command=vowel_consonant_count)
button_even_list = tk.Button(window, text='Get Even List', command=even_list)
button_string_opr = tk.Button(window, text='String Operation', command=string_operation)
button_file_handling = tk.Button(window, text='Text File Handeling', command=text_file_handling)
close_button = tk.Button(window, text='close window', command=window.destroy)

# Apply styles to buttons

buttons = [
    button_sod, button_simple, button_oe, button_reverse,
    button_largest, button_second_largest, button_fibonacci,
    button_palindrome, button_unique, button_prime, button_factorial,
    button_multiplication, button_armstrong, button_guessing,
    button_vowel_consonant, button_even_list, button_string_opr, button_file_handling, close_button
]

for button in buttons:
    button.config(font=button_font, fg=button_fg, bg=button_bg, padx=button_padx, pady=button_pady,relief=button_relief, width=button_width, height=button_height)

# Grid layout

button_simple.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
button_sod.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
button_oe.grid(row=1, column=2, padx=5, pady=5, sticky='ew')
button_reverse.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
button_largest.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
button_second_largest.grid(row=2, column=2, padx=5, pady=5, sticky='ew')
button_fibonacci.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
button_palindrome.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
button_unique.grid(row=3, column=2, padx=5, pady=5, sticky='ew')
button_prime.grid(row=4, column=0, padx=5, pady=5, sticky='ew')
button_factorial.grid(row=4, column=1, padx=5, pady=5, sticky='ew')
button_multiplication.grid(row=4, column=2, padx=5, pady=5, sticky='ew')
button_armstrong.grid(row=5, column=0, padx=5, pady=5, sticky='ew')
button_guessing.grid(row=5, column=1, padx=5, pady=5, sticky='ew')
button_vowel_consonant.grid(row=5, column=2, padx=5, pady=5, sticky='ew')
button_even_list.grid(row=6, column=0, padx=5, pady=5, sticky='ew')
button_string_opr.grid(row=6, column=1, padx=5, pady=5, sticky='ew')
button_file_handling.grid(row=6, column=2, padx=5, pady=5, sticky='ew')
close_button.grid(row=7, column=0, columnspan=3, padx=5, pady=20)

# Looping window

window.mainloop()