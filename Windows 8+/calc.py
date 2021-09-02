import eqn1
import eqn2
import eqn3
import unit_convert_input as uci
import unit_convert_output as uco
import ctypes
import os

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("Motion Calculator")


print("\033[1;32;40m")
print("  __  __       _   _                _____      _            _       _             ")
print(" |  \/  |     | | (_)              / ____|    | |          | |     | |            ")
print(" | \  / | ___ | |_ _  ___  _ __   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ")
print(" | |\/| |/ _ \| __| |/ _ \| '_ \  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
print(" | |  | | (_) | |_| | (_) | | | | | |____ (_| | | (__| |_| | | (_| | |_ (_) | |   ")
print(" |_|  |_|\___/ \__|_|\___/|_| |_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
print("                                              By Pranay Chopra, a.k.a PraDevHunter")
print("\033[1;37;40m")
print()

def main():
    print("P.S. The answers might differ by a few decimals from the manual method of calculation because of the fraction to decimalconversion, so please round off your answers.\n")
    print("Which equation of motion do you want to use?")
    print("1. v = u + at")
    print("2. s = ut + 1/2at\u00b2")
    print("3. v\u00b2 - u\u00b2 = 2as")
    q = input("Enter your choice (1, 2, 3): ")
    print("\n===============================================================\n")
    if q == "1":
        def func():
            print("What do you want to calculate?")
            print("1. Final velocity (v)")
            print("2. Initial velocity (u)")
            print("3. Acceleration (a)")
            print("4. Time (t)")
            qq = input("Enter your choice (v, u, a, t): ")
            print("\n===============================================================\n")
            qq == qq.lower()
            if qq == "v":
                eqn1.eqn1v()
            elif qq == "u":
                eqn1.eqn1u()
            elif qq == "a":
                eqn1.eqn1a()
            elif qq == "t":
                eqn1.eqn1t()
            else:
                print("Please choose the correct option.")
                print("\n===============================================================\n")
                func()
        func()
    elif q == "2":
        def func():
            print("What do you want to calculate?")
            print("1. Distance (s)")
            print("2. Initial velocity (u)")
            print("3. Time (t)")
            print("4. Acceleration (a)")
            qq = input("Enter your choice (s, u, t, a): ")
            print("\n===============================================================\n")
            qq == qq.lower()
            if qq == "s":
                eqn2.eqn2s()
            elif qq == "u":
                eqn2.eqn2u()            
            elif qq == "t":
                eqn2.eqn2t()
            elif qq == "a":
                eqn2.eqn2a()
            else:
                print("Please choose the correct option.")
                print("\n===============================================================\n")
                func()
        func()
    elif q == "3":
        def func():
            print("What do you want to calculate?")
            print("1. Final velocity (v)")
            print("2. Initial velocity (u)")
            print("3. Acceleration (a)")
            print("4. Distance (s)")
            qq = input("Enter your choice (v, u, a, s): ")
            print("\n===============================================================\n")
            qq == qq.lower()
            if qq == "v":
                eqn3.eqn3v()
            elif qq == "u":
                eqn3.eqn3u()
            elif qq == "a":
                eqn3.eqn3a()
            elif qq == "s":
                eqn3.eqn2s()
            else:
                print("Please choose the correct option.")
                print("\n===============================================================\n")
                func()
        func()
    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        main()

main()
                    
