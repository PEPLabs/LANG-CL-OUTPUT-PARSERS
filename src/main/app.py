from src.main.lab import invoke_basic_chain, invoke_complex_chain

if __name__ == "__main__":
    choice = input("Enter 1 for basic, 2 for complex: ")
    try:
        choice = int(choice)
    except Exception:
        print("Invalid choice")
        exit()

    if choice == 1:
        topic = input("Enter a topic: ")
        response = invoke_basic_chain(topic)
        print(response)
        exit()
    elif choice == 2:
        movie = input("Enter a movie: ")
        response = invoke_complex_chain(movie)
        print(response)
        exit()
    else: 
        print("Invalid choice")
        exit()