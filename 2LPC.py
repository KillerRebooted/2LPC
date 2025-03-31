import os
import sys
import datetime
import random
import time
import pyfiglet
import getpass
import datetime
import cv2
import win32api

clear = lambda: os.system('cls')

#Get file path based on whether code is running as a Python Script or an Executable
def get_path(relative_path):
    """ Get the correct path whether running as .py or .exe """
    if getattr(sys, 'frozen', False):  # Check if running as an .exe
        base_path = sys._MEIPASS  # Temp folder where PyInstaller extracts files
    else:
        base_path = os.path.dirname(__file__)  # Normal script directory
    
    return os.path.join(base_path, relative_path)

#Print RGB text
def rgb(text, Cycles):

    def colored(r, g, b, text):
        return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"

    r = 255
    g = 0
    b = 0
    x = 0

    while x != Cycles:

        while g != 255:

            print(colored(r, g, b, text), end="\r")
            time.sleep(0.1)

            g += 51

        while r != 0:

            print(colored(r, g, b, text), end="\r")
            time.sleep(0.1)

            r -= 51

        while b != 255:

            print(colored(r, g, b, text), end="\r")
            time.sleep(0.1)

            b += 51

        while g != 0:

            print(colored(r, g, b, text), end="\r")
            time.sleep(0.1)

            g -= 51

        while r != 255:

            print(colored(r, g, b, text), end="\r")
            time.sleep(0.1)

            r += 51

        while b != 0:

            print(colored(r, g, b, text), end="\r")
            time.sleep(0.1)

            b -= 51

        x += 1

    print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")

#Letter by Letter Printing
def LbL(sentence, gap):

    x = len(sentence)
    loop = -1

    while x!=0:
        loop += 1
        print(sentence[loop], end = "", flush=True)
        time.sleep(gap)
        x -= 1

    return ""

#Print Stylised Text
def styled_text(text):

    for i in range(len(text.split())):
        
        clear()

        text1 = pyfiglet.figlet_format(" ".join(text.split()[:i+1]), font = "slant", justify = 'center', width = os.get_terminal_size().columns)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        print(f"\033[38;2;{r};{g};{b}m{text1} \033[38;2;255;255;255m", end="\r")
    
        time.sleep(1)

#Run Hypnotising Video
def Hypnotise():

    # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture(get_path("Dependencies/Videos/Hypnotise.mp4"))

    # Check if camera opened successfully 
    if (cap.isOpened()== False): 
        print("Error opening video file") 
        
    window_name = "Hypnotise"
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    cv2.setMouseCallback("Hypnotise", mouse_evt)

    ret = True

    while ret:
        
        ret, frame = cap.read() 
        if ret == True:
            cv2.imshow(window_name, frame)

            cv2.waitKey(25)

        else: 
            break

    # When everything done, release the video capture object 
    cap.release() 

    # Closes all the frames 
    cv2.destroyAllWindows()

#For the function Hypnotise
def mouse_evt(event, x, y, flags, param):
    # Mouse is Moving
    if event == cv2.EVENT_MOUSEMOVE:
        win32api.SetCursor(None)

#n to 0 Users animation
def get_users(start_digits, end_digits, end_number):

    if start_digits > end_digits:
        increase = False
    else:
        increase = True

    for i in range(start_digits, end_digits + (1 if increase else -1), 1 if increase else -1):
        
        for j in range(30):
            print(f'Users: {random.randint(int(f"1{'0'*(i-1)}"), int(f"{'9'*i}"))}', end="\r", flush=True)
            time.sleep(0.01)

        print(" "*(i+len("Users: ")), end="\r", flush=True)

    t = 0
    for i in range(3, -1, -1):
        
        time.sleep(t)
        print(f"Users: {end_number-(i*(1 if increase else -1))+(1 if increase else -1)}", end="\r", flush=True)

        t += 0.8

#Open file with given relative path
def open_file(relative_path):
    
    os.system(f'"{get_path(f"Dependencies/{relative_path}")}"')

user = getpass.getuser()

clear()

print("Hello Hooman, hope you are doing well \U0001F601")
time.sleep(2)
print("Of course you are. If you are taking time to watch my...", end="\r")
time.sleep(2.5)
print("Of course you are. If you are taking time to watch (I mean) OUR Program")
time.sleep(2)

clear()

dt = datetime.datetime.now()

if dt.hour < 12: wish = "Morning"
elif (dt.hour >= 12) and (dt.hour < 18): wish = "Afternoon"
else: wish = "Evening"

LbL(f"The Story starts on a Fine {wish} as Python greets the User as usual...", 0.1)
time.sleep(1)

clear()

styled_text(f"{wish}, {user}!")

print()

response = input(": ")

if response == "":

    print()
    print("Well", end="", flush=True)
    time.sleep(1)
    print(LbL(", I guess You are not the talking type", 0.1), end="", flush = True)
    time.sleep(0.4)
    LbL("...", 0.4)

elif response[-1] == "!":

    print()
    print("Excited??!!", end= "\r")
    time.sleep(1)
    print("Excited??!! Me Too!!")
    time.sleep(1)

else:

    replies = ["Nice to meet you Hooman!", "Let me show you what all I can do!", "So how are you do-"]

    print()
    print(random.choice(replies))
    time.sleep(1.5)

#VBS Interaction 1
open_file("VBS/1.vbs")

clear()

print("STOP", end = "\r")
time.sleep(1)
print("STOP IT! ", end = "", flush=True)
time.sleep(1)
LbL("Visual Basics!", 0.1)

time.sleep(1)

clear()

print("Everybody", end="\r")
time.sleep(1)
print("Everybody likes", end="\r")
time.sleep(1)
print("Everybody likes me!")
time.sleep(1)
print(LbL("Aaaaaand", 0.1), end="\r")
time.sleep(0.5)
print("Aaaaaand nobody complains about me being", end="\r")
time.sleep(1)
print("Aaaaaand nobody complains about me being cAsE", end="\r")
time.sleep(1)
print("Aaaaaand nobody complains about me being cAsE sENsITivE")
time.sleep(1)

clear()

year = datetime.datetime.now().year

LbL(f"Who even uses VBS in {year}??", 0.1)

time.sleep(1)

clear()

for i in range(3):
    print("Logging into Database   ", end="\r")
    time.sleep(0.1)
    print("Logging into Database.  ", end="\r")
    time.sleep(0.1)
    print("Logging into Database.. ", end="\r")
    time.sleep(0.1)
    print("Logging into Database...", end="\r")
    time.sleep(0.1)

clear()

print(">>> ", end="", flush=True)
time.sleep(1)
LbL("VBS.get_users()", 0.08)
print()
time.sleep(1)

get_users(7, 1, 1)

print("Users: NULL")

time.sleep(1)

#VBS Interaction 2
open_file("VBS/2.vbs")

clear()

print("What", end = "\r")
time.sleep(1)
print("What a ", end = "\r")
time.sleep(1)
print("What a JOKE", end = "", flush=True)
time.sleep(1)
print(LbL("!!!", 0.3), end="\r", flush=True)
time.sleep(1)
print("What a \U0001F921     ")
time.sleep(1)

print()

print(LbL("I can do a lot of things that", 0.05), end = "\r")
time.sleep(0.5)
print("I can do a lot of things that YOU", end="\r")
time.sleep(1)
print("I can do a lot of things that YOU can't.")
time.sleep(1)

print()

print("What's the maximum you can do?", end = "\r")
time.sleep(1.5)
print("What's the maximum you can do? Be a VIRUS?", end = "\r")
time.sleep(1)

completion_time = time.time() + 3

while time.time() < completion_time:
    
    print("What's the maximum you can do? Be a VIRUS? \U0001F602", end = "\r")
    time.sleep(0.2)
    print("What's the maximum you can do? Be a VIRUS? \U0001F606", end = "\r")
    time.sleep(0.2)

clear()

#VBS Interaction 3 - Part 1
open_file("VBS/3_1.vbs")

time.sleep(1)
print("Yeah so-")
time.sleep(1)

clear()

#VBS Interaction 3 - Part 2
open_file("VBS/3_2.vbs")

print("I didn't hear you.")
time.sleep(1)
print(f"I was paying attention to {user} and CMD.")
time.sleep(2.5)

clear()

#VBS Interaction 4
open_file("VBS/4.vbs")

print(LbL("HAHAHAHA", 0.1), end="\r")
time.sleep(1)
print("HAHAHAHAHA", end="", flush=True)
time.sleep(1.5)
print(". My second name is User-Friendly")
time.sleep(3)
print("Check THIS out!")
time.sleep(1.5)

clear()

user_friendly_question = input(f"Is the weather good today, {user}? (y/n): ")

clear()

if user_friendly_question.lower() in ["y", "n"]:

    print()
    print("See?", end = "\r")
    time.sleep(1)

    for i in range(4):

        print("See? I can easily be User-Friendly, unlike you \U0001F922", end = "\r")
        time.sleep(0.5)
        print("See? I can easily be User-Friendly, unlike you \U0001F92E", end = "\r")
        time.sleep(0.5)

    #VBS Interaction 5 - Part 1
    open_file("VBS/5_1.vbs")

else:
    
    rgb("This is the reason I don't like being friendly. It seems you're drunk and see everything in rainbow or something", 2)

    clear()

    rgb("See this, it might fix it.", 1)

    clear()

    rgb("But you might become blind if you're unlucky. Don't worry, it only happens 82.6% of the times! Here goes nothing", 2)

    print(Hypnotise())

    clear()
    time.sleep(1)
    print("I think everything should be fixed now...")
    time.sleep(3)
    clear()
    
    random_number = random.randint(1, 10)

    answer = input(f"Tell me how much is this - '{random_number}': ")

    if answer == str(random_number):

        changed_answer = answer

        while str(changed_answer) == str(answer):
            
            changed_answer = random.randint(1, 10)
        
        clear()
        print(f"Tell me how much is this - '{changed_answer}': {answer}")
        print()
        print("WRONG! ", end="", flush=True)
        time.sleep(1)
        print(f"It was {changed_answer}")

    else:

        print()
        print("WRONG! ", end="", flush=True)
        time.sleep(1)
        print(f"It was {random_number}")

    time.sleep(3)
    clear()

    LbL("It seems that the treatment has ruined your eyesight...", 0.1)
    time.sleep(2)

    #VBS Interaction 5 - Part 2
    open_file("VBS/5_2.vbs")

clear()

time.sleep(1)
print(LbL(f"Anything else you want me to prove, {user}?", 0.1), end=" ", flush=True)
time.sleep(1)
LbL("Or should we call it a day?", 0.1)
time.sleep(1)

clear()

#VBS Interaction 6
open_file("VBS/6.vbs")

time.sleep(1.5)
print("Ha ", end="")
time.sleep(1)
print(LbL("That's what I thought. ", 0.1), end="")
time.sleep(0.5)
print("VBS ", end="")
time.sleep(0.5)
print("was ", end="")
time.sleep(0.5)
print("NO ", end="")
time.sleep(1)
print("Challenge.")
time.sleep(1)

clear()

LbL("It was like a Human trying to control Nature which was never their's to control.", 0.1)
print()
LbL("When the Human overestimates himself, the Nature shows its true nature.", 0.1)