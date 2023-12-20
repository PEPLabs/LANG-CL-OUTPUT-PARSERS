from src.main.lab import invoke_basic_chain

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    response = invoke_basic_chain(topic)
    print(response)


