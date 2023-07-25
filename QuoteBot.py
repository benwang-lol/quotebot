class QuoteBot:
    def __init__(self):
        self.quotes = {}

    def handle_message(self, user, message) -> str: 
        if message == "$quoteShowAll":
            return self.show_all_quotes()
        elif message.startswith("$quote"): 
            return self.add_quote(user, message)
        print(self.quotes)
        return 

    def add_quote(self, user, message):
        quote = message[len("quote") + 1:].strip()
        if user not in self.quotes: 
            self.quotes[user] = []
        self.quotes[user].append(quote)
        return "Quote added!"

    def show_all_quotes(self):
        if not self.quotes: 
            return "No quotes yet"
        all_quotes = ""
        for user, quotes in self.quotes.items():
            for quote in quotes: 
                all_quotes += f"{quote} - {user}\n"
        return all_quotes.strip()

# bot = QuoteBot()

# def process_message(user, message):
#     if message.startswith("$quote"):
#         if message == "$quoteShowAll":
#             return bot.show_all_quotes()
#         else:
#             return bot.add_quote(user, message)

# # Example usage:
# user1 = "Alice"
# user2 = "Bob"

# print(process_message(user1, "$quote This is a great quote!")) # Output: Quote added successfully!
# print(process_message(user2, "$quote Another awesome quote!")) # Output: Quote added successfully!
# print(process_message(user1, "$quoteShowAll")) # Output: This is a great quote! - Alice\nAnother awesome quote! - Bob
