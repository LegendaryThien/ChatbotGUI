import tkinter as tk
import openai

# Initialize the Tkinter root window
root = tk.Tk()
root.geometry("500x500")
root.title("Chat with GPT")


# Function to handle the display of input and fetching ChatGPT response
def handle_chat():
    user_input = entry.get()  # Get the text from the entry widget

    # Check if the input is not empty
    if user_input.strip() != "":
        label.config(text="You: " + user_input)
        response = chat_with_gpt(user_input)
        reply.config(text="GPT: " + response)

    # Clear the entry widget for the next input
    entry.delete(0, tk.END)


# ChatGPT Code
openai.api_key = "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"  # Ensure you use a valid API key here


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


# Tkinter Code
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=20, pady=10)

button = tk.Button(root, text="Send to ChatGPT", command=handle_chat, font=("Arial", 12))
button.pack(padx=20, pady=10)

label = tk.Label(root, text=" ", font=("Arial", 12))
label.pack(padx=20, pady=10)

reply = tk.Label(root, text="GPT response will appear here", font=("Arial", 12))
reply.pack(padx=20, pady=10)

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
