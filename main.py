import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    print(f"Command received: {command}")
    
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing TanOS")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print(f"You said: {word}")
                
                if "hello" in word.lower():

                    speak("Yes, how can I help you?")
                    print("TanOS Active...")

                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
                if "exit" in command.lower():
                    speak("Goodbye! Exiting TanOS.")
                    break

                
                

        except sr.WaitTimeoutError:
            pass  # just keep listening
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except Exception as e:
            print(f"Error: {e}")
