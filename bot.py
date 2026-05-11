print("===== AI CUSTOMER CHATBOT =====")
print("Type 'bye' to exit.\n")

while True:

    
    user = input("You: ").lower()

   
    if user == "bye":
        print("Bot: Thank you for visiting!")
        break

   
    elif "hello" in user or "hi" in user or "namste" in user:
        print("Bot: Hello! How may I help you?")

    
    elif "product" in user:
        print("Bot: We sell laptops, mobiles, headphones, and smart watches.")

   
    elif "price" in user or "cost" in user:
        print("Bot: Our product prices start from Rs. 10,000.")

   
    elif "delivery" in user or "shipping" in user:
        print("Bot: Delivery takes around 3 to 5 business days.")

    
    elif "return" in user or "refund" in user:
        print("Bot: Products can be returned within 7 days.")

    
    elif "warranty" in user:
        print("Bot: All products come with 1-year warranty.")

    
    elif "contact" in user or "support" in user:
        print("Bot: Contact us at support@gmail.com")

    
    elif "payment" in user:
        print("Bot: We accept UPI, debit card, credit card, and net banking.")


    else:
        print("Bot: Sorry, I could not understand your query.")