# main.py

from chatbot import get_crypto_by_name, give_advice

def start_chat():
    print("🤖Welcome to your Crypto Advisor Sidekick!")
    print("Type a crypto name or symbol (e.g., BTC, Ethereum). Type 'exit' to quit.\n")

    while True:
        user_input = input(" Your input: ").strip()
        if user_input.lower() == "exit":
            print(" 👋Exiting. See you next time!")
            break

        crypto = get_crypto_by_name(user_input)
        if crypto:
            give_advice(crypto)
        else:
            print("❌ Crypto not found in the database.\n")

# Start the chatbot
start_chat()
