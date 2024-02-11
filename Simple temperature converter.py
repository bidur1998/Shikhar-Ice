import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

#Temperatureconveter : A utility class with a static method to convert Fahrenheit to Celsius.
class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

#ConverterFrame :  A frame responsible for creating widgets (labels, entry, button) and handling events.
class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}

        # Temperature label and entry
        self.temperature_label = ttk.Label(self, text='Fahrenheit')
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()

        # Convert button
        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        # Result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # Add padding to the frame
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self):
        try:
            f = float(self.temperature.get())
            c = TemperatureConverter.fahrenheit_to_celsius(f)
            result = f'{f} Fahrenheit = {c:.2f} Celsius'
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)


#App :  The main application class that initializes the GUI.
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Temperature Converter')
        self.geometry('300x70')
        self.resizable(False, False)


#The if __name__ == "__main__": block starts the application.
if __name__ == "__main__":
    app = App()
    ConverterFrame(app)
    app.mainloop()
