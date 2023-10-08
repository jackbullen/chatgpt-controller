import tkinter as tk
from tkinter import scrolledtext, filedialog, ttk
import backend as backend

def send_query():
    query = user_input.get()
    builder_type = prompt_builder_var.get()
    num_continuations = int(continuations_spinbox.get())  # Get the number of desired continuations
    
    is_complete = backend.interact_with_chatgpt(query, builder_type)
    # chat_history.insert(tk.END, f"You: {query}\n")
    user_input.delete(0, tk.END)
    
    if is_complete:
        # Automatically trigger the continuation based on user input
        for _ in range(num_continuations):
            continue_chat()


def continue_chat():
    backend.interact_with_chatgpt("Please continue elaborating and working on the next step.")

def get_latex():
    query = user_input.get()
    latex = backend.interact_with_chatgpt(query, builder_type="LaTeX")
    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("ChatGPT")
user_input = tk.Entry(root, width=60)
user_input.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_query)
send_button.pack(pady=10)

prompt_builder_var = tk.StringVar()
prompt_builder_var.set("Standard")  # default value
prompt_builder_label = tk.Label(root, text="Select a Prompt Builder:")
prompt_builder_label.pack(pady=5)
prompt_builder_dropdown = ttk.Combobox(root, textvariable=prompt_builder_var, 
                                       values=["Standard", "Build", "Research", "Deep Dive", "Notebook", "Expert Panel"])#, 
                                               #"Historical Context", "Pro-Con Analysis", "Future Implications"])
prompt_builder_dropdown.pack(pady=5)

send_button = tk.Button(root, text="LaTeX", command=get_latex)
send_button.pack(pady=10)

continuations_label = tk.Label(root, text="Number of continuations:")
continuations_label.pack(pady=5)
continuations_spinbox = tk.Spinbox(root, from_=0, to=10, width=5)  # Let's allow between 1 to 10 continuations
continuations_spinbox.pack(pady=5)

def on_closing():
    backend.close_browser()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
