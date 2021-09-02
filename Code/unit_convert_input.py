import time

#initial velocity
def initial_velocity():
    global u
    print("The default unit for initial velocity is m/s")
    print("Type \"kmh\" if you have the initial velocity in km/h")
    print("Type \"cms\" if you have the initial velocity in cm/s")
    print("Type \"ms\" if you have the initial velocity in m/s")
    initial_velocity_unit = input("Enter your choice: ")
    print()
    initial_velocity_unit = initial_velocity_unit.lower()

    if initial_velocity_unit == "kmh":
        try:
            u = float(input("Enter initial velocity: "))
            u = u*0.277777778
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif initial_velocity_unit == "cms":
        try:
            u = float(input("Enter initial velocity: "))
            u = u/100
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif initial_velocity_unit == "ms":
        try:
            u = float(input("Enter initial veocity: "))
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        initial_velocity()


#acceleration
def acceleration():
    global a
    print("The default unit for acceleration is m/s\u00b2")
    print("Type \"kmh2\" if you have the acceleration is km/h\u00b2")
    print("Type \"cms2\" if you have the acceleration is cm/s\u00b2")
    print("Type \"ms2\" if you have the acceleration is m/s\u00b2")
    acceleration_unit = input("Enter your choice: ")
    print()
    acceleration_unit = acceleration_unit.lower()

    if acceleration_unit == "kmh2":
        try:
            a = float(input("Enter acceleration: "))
            a = a*(0.00007716049382716049)
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
    
    elif acceleration_unit == "cms2":
        try:
            a = float(input("Enter acceleration: "))
            a = a*0.01
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
        
    elif acceleration_unit == "ms2":
        try:
            a = float(input("Enter acceleration: "))
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        acceleration()






#final velocity
def final_velocity():
    global v
    print("The default unit for final velocity is m/s")
    print("Type \"kmh\" if you have the final velocity in km/h")
    print("Type \"cms\" if you have the final velocity in cm/s")
    print("Type \"ms\" if you have the final velocity in m/s")
    final_velocity_unit = input("Enter your choice: ")
    print()
    final_velocity_unit = final_velocity_unit.lower()

    if final_velocity_unit == "kmh":
        try:
            v = float(input("Enter final velocity: "))
            v = v*0.277777778
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif final_velocity_unit == "cms":
        try:
            v = float(input("Enter final velocity: "))
            v = v/100
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif final_velocity_unit == "ms":
        try:
            v = float(input("Enter final veocity: "))
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        final_velocity()





#time
def time():
    global t
    print("The default unit for time is seconds")
    print("Type \"hr\" if you have the time in hours")
    print("Type \"mins\" if you have the time in minutes")
    print("Type \"secs\" if you have the time in seconds")
    time_unit = input("Enter your choice: ")
    print()
    time_unit = time_unit.lower()

    if time_unit == "hr":
        try:
            t = float(input("Enter time: "))
            t = t*3600
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif time_unit == "mins":
        try:
            t = float(input("Enter time: "))
            t = t*60
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif time_unit == "secs":
        try:
            t = float(input("Enter time: "))
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        time()



#distance
def distance():
    global s
    print("The default unit for distance is metre")
    print("Type \"km\" if you have the distance in kilometre")
    print("Type \"cm\" if you have the distance in centimetre")
    print("Type \"m\" if you have the distance in metre")
    distance_unit = input("Enter your choice: ")
    print()
    distance_unit = distance_unit.lower()

    if distance_unit == "km":
        try:
            s = float(input("Enter distance: "))
            s = s*1000
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif distance_unit == "cm":
        try:
            s = float(input("Enter distance: "))
            s = s/100
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()

    elif distance_unit == "m":
        try:
            s = float(input("Enterdistance: "))
        except ValueError as e:
            print()
            print("Please see that you input numbers only")
            print("Quitting...")
            time.sleep(5)
            quit()
        except KeyboardInterrupt as k:
            print()
            print("Quitting...")
            time.sleep(5)
            quit()
    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        distance()


