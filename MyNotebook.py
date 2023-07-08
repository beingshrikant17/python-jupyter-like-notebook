import tkinter as tk
import io
import sys


root = tk.Tk()
root.title("Jupyter-like GUI")
root.geometry("1480x830")
def run_code():  
    output_label.delete(1.0, tk.END)
    code = code_input.get("1.0", "end-1c")
    output_stream = io.StringIO()
    sys.stdout = output_stream
    try:
        exec(code)
        output_label.insert("1.0", output_stream.getvalue())
    except Exception as e:
        output_label.insert("1.0", str(e))
    sys.stdout = sys.__stdout__

heading = tk.Label(root, text="A Python Notebook", font=("Helvetica", 20),bg="orange", fg="white", height=4, width=100)
heading.pack()

code_input = tk.Text(root, height=10, width=200)
code_input.pack(pady=20)

run_button = tk.Button(root, text="Run", command=run_code)
run_button.pack(pady=10)

output_label = tk.Text(root, bg="white", width=220, height=25)
output_label.pack(pady=10)

root.mainloop()