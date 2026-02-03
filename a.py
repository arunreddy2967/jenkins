
# main.py

def greet(name):
    return f"Hello, {name}! Welcome to Jenkins CI."

if __name__ == "__main__":
    user = "Arun"
    message = greet(user)
    print(message)
