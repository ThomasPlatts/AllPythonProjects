import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time


# Functions
def convert_weight():
    combo_value_1 = weight_unit_1.get()
    combo_value_2 = weight_unit_2.get()
    if combo_value_1 == "Kg" and combo_value_2 == "Lbs":
        weight_convert_kg = weight_input.get()
        weight_convert_kg = float(weight_convert_kg)
        kg_lbs_conversion = weight_convert_kg * 2.20462
        kg_lbs_conversion = round(kg_lbs_conversion, 2)
        kg_to_lbs = Label(window, text=f"{kg_lbs_conversion}lbs", font="Helvetica 20 bold")
        kg_to_lbs.place(x=570, y=200)
        window.update()
        time.sleep(3)
        kg_to_lbs.destroy()
    if combo_value_1 == "Kg" and combo_value_2 == "St":
        weight_convert_kg_2 = weight_input.get()
        weight_convert_kg_2 = float(weight_convert_kg_2)
        kg_st_conversion = weight_convert_kg_2 / 6.35
        kg_st_conversion = round(kg_st_conversion, 2)
        kg_to_st = Label(window, text=f"{kg_st_conversion}st", font="Helvetica 20 bold")
        kg_to_st.place(x=570, y=200)
        window.update()
        time.sleep(3)
        kg_to_st.destroy()
    if combo_value_1 == "Lbs" and combo_value_2 == "Kg":
        weight_convert_lbs = weight_input.get()
        weight_convert_lbs = float(weight_convert_lbs)
        lbs_kg_conversion = weight_convert_lbs / 2.20462
        lbs_kg_conversion = round(lbs_kg_conversion, 2)
        lbs_to_kg = Label(window, text=f"{lbs_kg_conversion}kg", font="Helvetica 20 bold")
        lbs_to_kg.place(x=570, y=200)
        window.update()
        time.sleep(3)
        lbs_to_kg.destroy()
    if combo_value_1 == "Lbs" and combo_value_2 == "St":
        weight_convert_lbs_2 = weight_input.get()
        weight_convert_lbs_2 = float(weight_convert_lbs_2)
        lbs_st_conversion = weight_convert_lbs_2 / 14
        lbs_st_conversion = round(lbs_st_conversion, 2)
        lbs_to_st = Label(window, text=f"{lbs_st_conversion}st", font="Helvetica 20 bold")
        lbs_to_st.place(x=570, y=200)
        window.update()
        time.sleep(3)
        lbs_to_st.destroy()
    if combo_value_1 == "St" and combo_value_2 == "Kg":
        weight_convert_st = weight_input.get()
        weight_convert_st = float(weight_convert_st)
        st_kg_conversion = weight_convert_st * 6.35
        st_kg_conversion = round(st_kg_conversion, 2)
        st_to_kg = Label(window, text=f"{st_kg_conversion}kg", font="Helvetica 20 bold")
        st_to_kg.place(x=570, y=200)
        window.update()
        time.sleep(3)
        st_to_kg.destroy()
    if combo_value_1 == "St" and combo_value_2 == "Lbs":
        weight_convert_st_2 = weight_input.get()
        weight_convert_st_2 = float(weight_convert_st_2)
        st_lbs_conversion = weight_convert_st_2 * 14
        st_lbs_conversion = round(st_lbs_conversion, 2)
        st_to_lbs = Label(window, text=f"{st_lbs_conversion}lbs", font="Helvetica 20 bold")
        st_to_lbs.place(x=570, y=200)
        window.update()
        time.sleep(3)
        st_to_lbs.destroy()
    if combo_value_1 == "Kg" and combo_value_2 == "Kg":
        kg_same = weight_input.get()
        kg_same = float(kg_same)
        kg_s_value = Label(window, text=f"{kg_same}kg", font="Helvetica 20 bold")
        kg_s_value.place(x=570, y=200)
        window.update()
        time.sleep(3)
        kg_s_value.destroy()
    if combo_value_1 == "Lbs" and combo_value_2 == "Lbs":
        lbs_same = weight_input.get()
        lbs_same = float(lbs_same)
        lbs_s_value = Label(window, text=f"{lbs_same}lbs", font="Helvetica 20 bold")
        lbs_s_value.place(x=570, y=200)
        window.update()
        time.sleep(3)
        lbs_s_value.destroy()
    if combo_value_1 == "St" and combo_value_2 == "St":
        st_same = weight_input.get()
        st_same = float(st_same)
        st_s_value = Label(window, text=f"{st_same}st", font="Helvetica 20 bold")
        st_s_value.place(x=570, y=200)
        window.update()
        time.sleep(3)
        st_s_value.destroy()


# Main Window
window = tk.Tk()
window.title("Weight Converter")
window.resizable(width=False, height=False)
window.geometry("1280x720")

# Buttons, Labels, Dropdown and Entry
values = "Kg", "Lbs", "St"
weight_unit_1 = ttk.Combobox(window, state="readonly", values=values, width=5)
weight_unit_1.place(x=485, y=50)
weight_unit_2 = ttk.Combobox(window, state="readonly", values=values, width=5)
weight_unit_2.place(x=585, y=100)

title = Label(window, text="Weight Converter", fg="Green", font="Helvetica 20 bold")
title.place(x=550, y=0)
instructions_start = Label(window, text="Select your weight unit that\nyou measure yourself in, "
                                        "then enter your weight", justify=LEFT, font="Helvetica 10 bold")
instructions_start.place(x=675, y=45)
instructions_middle = Label(window, text="Select the unit of measurement\nthat you would like to convert to",
                            justify=LEFT, font="Helvetica 10 bold")
instructions_middle.place(x=650, y=95)

weight_input = Entry(window)
weight_input.place(x=550, y=50)

convert = Button(window, text="Convert", font="Helvetica 12 bold", fg="black", command=convert_weight)
convert.place(x=475, y=95)


mainloop()
