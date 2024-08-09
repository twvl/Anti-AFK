import random
import keyboard
import time
import ctypes
import webbrowser
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def action(keys: list):
    random.shuffle(keys)
    for key in keys:
        keyboard.press(key)
        keyboard.release(key)

def display_menu():
    print("\x1b[38;5;225m")
    print("""
  █████╗ ███╗   ██╗████████╗██╗     █████╗ ███████╗██╗  ██╗
 ██╔══██╗████╗  ██║╚══██╔══╝██║    ██╔══██╗██╔════╝██║ ██╔╝
 ███████║██╔██╗ ██║   ██║   ██║    ███████║█████╗  █████╔╝ 
 ██╔══██║██║╚██╗██║   ██║   ██║    ██╔══██║██╔══╝  ██╔═██╗ 
 ██║  ██║██║ ╚████║   ██║   ██║    ██║  ██║██║     ██║  ██╗
 ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ 
          Anti AFK by dx9bloob
 Usage: Activate and stay tabbed on roblox.
    """)
    print("\x1b[38;5;225m")

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("ᓚᘏᗢ")
    display_menu()

    mode_choice = input('[1] Jump Key\n[2] Extra\n>>> ')

    if mode_choice == '1':
        keys = ['space']
        print("TYPE 1 THEN TAB IN ON ROBLOX")
    elif mode_choice == '2':
        clear_screen()
        display_menu()
        extra_choice = input('[1] Credits\n>>> ')
        if extra_choice == '1':
            clear_screen()
            display_menu()
            webbrowser.open('discord://users/1048171869339136010')
            exit()
        else:
            print("Type 1 not that hard man..")
            exit()

    return keys

if __name__ == '__main__':
    keys = main()

    while True:
        action(keys)
        time.sleep(1)