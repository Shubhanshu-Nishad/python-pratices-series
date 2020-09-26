from win32com.client import Dispatch

def speak(str):
    speak= Dispatch(("SAPI.SpVoice"))
    speak.speak(str)



if __name__ == "__main__":
    speak('I have subscribe your channel and i will share it with my friends ')
    print('i have speak')