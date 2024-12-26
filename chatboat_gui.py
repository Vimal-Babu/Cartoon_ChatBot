import tkinter as tk
from cartoon_chatbot import CartoonChatbot

class CartoonChatbotGUI:
    def __init__(self, root):
        self.chatbot = CartoonChatbot()  # Use the previously defined chatbot logic
        self.root = root
        self.root.title("Cartoon Chatbot")
        
        # Create the chat window
        self.chat_window = tk.Text(self.root, height=15, width=50, state="disabled")
        self.chat_window.pack(pady=10)
        
        # Create an input box for the user to type their question
        self.user_input = tk.Entry(self.root, width=40)
        self.user_input.pack(pady=10)
        self.user_input.bind("<Return>", self.on_enter)

        # Create a button to submit the question
        self.submit_button = tk.Button(self.root, text="Ask", command=self.on_enter)
        self.submit_button.pack()

    def on_enter(self, event=None):
        user_question = self.user_input.get()
        response = self.chatbot.respond(user_question)
        
        # Display the user's question and the chatbot's response
        self.chat_window.config(state="normal")
        self.chat_window.insert(tk.END, f"You: {user_question}\nBot: {response}\n\n")
        self.chat_window.config(state="disabled")
        
        # Clear the input box for the next question
        self.user_input.delete(0, tk.END)

# Create the main window
root = tk.Tk()
chatbot_gui = CartoonChatbotGUI(root)
root.mainloop()
