class CartoonChatbot:
    def __init__(self):
        # Define the knowledge base as a dictionary
        self.rules = {
            "Doraemon": "Doraemon is a Japanese Anime character from the series 'Doraemon'.",
            "Shizuka": "Shizuka is a character in the anime 'Doraemon'. She is Nobita's best friend.",
            "Nobita": "Nobita is the main character in the anime 'Doraemon'. He is a clumsy and often lazy boy.",
            "Suneo": "Suneo is a character in 'Doraemon'. He is a schoolmate of Nobita, often teasing him.",
            "Gian": "Gian is another character in 'Doraemon'. He is known for his love for singing, despite being tone-deaf.",
        }

    def respond(self, user_input):
        # Normalize input to remove unnecessary characters and whitespace
        normalized_input = user_input.strip("?").strip().capitalize()
        # Look for the character name in the dictionary
        response = self.rules.get(normalized_input, "Sorry, I don't have information on that character.")
        return response

# Example usage
if __name__ == "__main__":
    chatbot = CartoonChatbot()
    while True:
        user_input = input("Ask me about a cartoon character: ")
        print(chatbot.respond(user_input))