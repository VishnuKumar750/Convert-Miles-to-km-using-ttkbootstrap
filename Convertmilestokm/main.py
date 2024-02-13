# ttkbootstrap
import ttkbootstrap as ttk

# convert function to convert miles into km
def convert():
    milesInput = entry_int.get()
    # 1mile - 1.6km
    result = milesInput * 1.6
    output_string.set(result)

# window 
window = ttk.Window(themename="journal")
window.title('ConvertMilestoKm')
window.geometry('550x250')

# title
title_label = ttk.Label(master = window, text="Miles to kilometers", font="Calibri 24 bold")
title_label.pack()

# input_frame
input_frame = ttk.Frame(master=window)
entry_int = ttk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left")
button.pack(side="right", padx=10)
input_frame.pack(pady=10)

# output_label
output_text_label = ttk.Label(master=window, text="Output")
output_text_label.pack(pady=5)

# result
output_string = ttk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_string, font="Calibri 24")
output_label.pack(pady=15)

# showing window
window.mainloop()