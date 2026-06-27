import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! I'm your AI chatbot. How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! How about you?"
    elif "name" in user_input:
        return "I'm a rule-based chatbot created by Hansika!"
    elif "help" in user_input:
        return "Sure! You can ask me about AI, Python, or your projects."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"
    elif "project" in user_input:
        return "You’re working on AI projects — that’s awesome!"
    elif "thank" in user_input:
        return "You're welcome!"
    elif "time" in user_input:
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    elif "date" in user_input:
        import datetime
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}."
    else:
        return "I'm not sure about that. Try asking something else!"

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)
    chat_window.see(tk.END)
    if user_input.lower() in ["bye", "exit", "quit"]:
        root.after(1000, root.destroy)

root = tk.Tk()
root.title("Rule-Based AI Chatbot 🤖")
root.geometry("500x500")
root.configure(bg="#E8F0FE")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 11))
chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "Bot: Hello! Type something to start chatting.\n\n")

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
send_button.pack(pady=5)

root.mainloop()
