import string
import secrets
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        speak(f"Your generated password is: {password}")
    except ValueError:
        speak("Please enter a valid number.")


