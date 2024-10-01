def chatbot():
    # Welcome message
    print("Hello! Welcome to the chatbot.")
    
    # Collect user's name and age
    name = input("What is your name? ")
    age = input("How old are you? ")
    
    # Display a personalized message
    print(f"Nice to meet you, {name}! I see you're {age} years old.")
    
    # Ask how the bot can help
    print("How can I help you today?")
    print("1. Ask a question")
    print("2. Get some advice")
    print("3. Tell me a joke")
    print("4. Exit")
    
    # Get the user's choice
    choice = input("Please select an option by entering the corresponding number: ")
    
    # Process the user's choice
    if choice == "1":
        question = input("What question would you like to ask? ")
        print(f"That's a great question, {name}! Let me think about that.")
    elif choice == "2":
        print("Advice: Always keep learning and stay curious!")
    elif choice == "3":
        print("Why don't scientists trust atoms? Because they make up everything!")
    elif choice == "4":
        print(f"Goodbye, {name}! Have a great day!")
    else:
        print("Sorry, I didn't understand that. Please choose a valid option.")

# Run the chatbot
chatbot()
