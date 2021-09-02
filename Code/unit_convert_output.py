import eqn1
import eqn2
import eqn3

def eqn1_initial_velocity():
    print("The default unit for initial velocity is m/s")
    print("Type \"kmh\" if you want the initial velocity in km/h")
    print("Type \"cms\" if you want the initial velocity in cm/s")
    print("Type \"ms\" if you want the initial velocity in m/s")
    initial_velocity_unit = input("Enter your choice: ")
    print()
    initial_velocity_unit = initial_velocity_unit.lower()

    if initial_velocity_unit == "kmh":
        eqn1.u = eqn1.u/0.277777778
        print("The answer is " + str(eqn1.u) + " km/h")
        input("Press ENTER to continue...")

    elif initial_velocity_unit == "cms":
        eqn1.u = eqn1.u*100
        print("The answer is " + str(eqn1.u) + " cm/s")
        input("Press ENTER to continue...")

    elif initial_velocity_unit == "ms":
        print("The answer is " + str(eqn1.u) + " m/s")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn1_initial_velocity()


def eqn1_final_velocity():
    print("The default unit for final velocity is m/s")
    print("Type \"kmh\" if you want the final velocity in km/h")
    print("Type \"cms\" if you want the final velocity in cm/s")
    print("Type \"ms\" if you want the final velocity in m/s")
    final_velocity_unit = input("Enter your choice: ")
    print()
    final_velocity_unit = final_velocity_unit.lower()

    if final_velocity_unit == "kmh":
        eqn1.v = eqn1.v/0.277777778
        print("The answer is " + str(eqn1.v) + " km/h")
        input("Press ENTER to continue...")

    elif final_velocity_unit == "cms":
        eqn1.v = eqn1.v*100
        print("The answer is " + str(eqn1.v) + " cm/s")
        input("Press ENTER to continue...")

    elif final_velocity_unit == "ms":
        print("The answer is " + str(eqn1.v) + " m/s")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn1_final_velocity()


def eqn1_acceleration():
    print("The default unit for acceleration is m/s\u00b2")
    print("Type \"kmh2\" if you want the acceleration in km/h\u00b2")
    print("Type \"cms2\" if you want the acceleration in cm/s\u00b2")
    print("Type \"ms2\" if you want the acceleration in m/s\u00b2")
    acceleration_unit = input("Enter your choice: ")
    print()
    acceleration_unit = acceleration_unit.lower()

    if acceleration_unit == "kmh2":
        eqn1.a = eqn1.a*(0.00007716049382716049)
        print("The answer is " + str(eqn1.a) + " km/h\u00b2")
        input("Press ENTER to continue...")

    elif acceleration_unit == "cms2":
        eqn1.a = eqn1.a*0.01
        print("The answer is " + str(eqn1.a) + " cm/s\u00b2")
        input("Press ENTER to continue...")

    elif acceleration_unit == "ms2":
        print("The answer is " + str(eqn1.a) + " m/s\u00b2")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn1_acceleration()



def eqn1_time():
    print("The default unit for time is seconds")
    print("Type \"hr\" if you want the time in hours")
    print("Type \"mins\" if you want the time in minutes")
    print("Type \"secs\" if you want the time in seconds")
    time_unit = input("Enter your choice: ")
    print()
    time_unit = time_unit.lower()

    if time_unit == "hr":
        eqn1.t = eqn1.t/3600
        print("The answer is " + str(eqn1.t) + " hours")
        input("Press ENTER to continue...")

    elif time_unit == "mins":
        eqn1.t = eqn1.t/60
        print("The answer is " + str(eqn1.t) + " minutes")
        input("Press ENTER to continue...")

    elif time_unit == "secs":
        print("The answer is " + str(eqn1.t) + " seconds")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn1_time()













def eqn2_initial_velocity():
    print("The default unit for initial velocity is m/s")
    print("Type \"kmh\" if you want the initial velocity in km/h")
    print("Type \"cms\" if you want the initial velocity in cm/s")
    print("Type \"ms\" if you want the initial velocity in m/s")
    initial_velocity_unit = input("Enter your choice: ")
    print()
    initial_velocity_unit = initial_velocity_unit.lower()

    if initial_velocity_unit == "kmh":
        eqn2.u = eqn2.u/0.277777778
        print("The answer is " + str(eqn2.u) + " km/h")
        input("Press ENTER to continue...")

    elif initial_velocity_unit == "cms":
        eqn2.u = eqn2.u*100
        print("The answer is " + str(eqn2.u) + " cm/s")
        input("Press ENTER to continue...")

    elif initial_velocity_unit == "ms":
        print("The answer is " + str(eqn2.u) + " m/s")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn2_initial_velocity()


def eqn2_distance():
    print("The default unit for distance is metre")
    print("Type \"km\" if you want the distance in kilometre")
    print("Type \"cm\" if you want the distance in centimetre")
    print("Type \"m\" if you want the distance in metre")
    distance_unit = input("Enter your choice: ")
    print()
    distance_unit = distance_unit.lower()

    if distance_unit == "km":
        eqn2.s = eqn2.s/1000
        print("The answer is " + str(eqn2.s) + " kilometre")
        input("Press ENTER to continue...")

    elif distance_unit == "cm":
        eqn2.s = eqn2.s*100
        print("The answer is " + str(eqn2.s) + " centimetre")
        input("Press ENTER to continue...")

    elif distance_unit == "m":
        print("The answer is " + str(eqn2.s) + " metre")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn2_distance()


def eqn2_acceleration():
    print("The default unit for acceleration is m/s\u00b2")
    print("Type \"kmh2\" if you want the acceleration in km/h\u00b2")
    print("Type \"cms2\" if you want the acceleration in cm/s\u00b2")
    print("Type \"ms2\" if you want the acceleration in m/s\u00b2")
    acceleration_unit = input("Enter your choice: ")
    print()
    acceleration_unit = acceleration_unit.lower()

    if acceleration_unit == "kmh2":
        eqn2.a = eqn2.a*(0.00007716049382716049)
        print("The answer is " + str(eqn2.a) + " km/h\u00b2")
        input("Press ENTER to continue...")

    elif acceleration_unit == "cms2":
        eqn2.a = eqn2.a*0.01
        print("The answer is " + str(eqn2.a) + " cm/s\u00b2")
        input("Press ENTER to continue...")

    elif acceleration_unit == "ms2":
        print("The answer is " + str(eqn2.a) + " m/s\u00b2")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn2_acceleration()



def eqn2_time():
    print("The default unit for time is seconds")
    print("Type \"hr\" if you want the time in hours")
    print("Type \"mins\" if you want the time in minutes")
    print("Type \"secs\" if you want the time in seconds")
    time_unit = input("Enter your choice: ")
    print()
    time_unit = time_unit.lower()

    if time_unit == "hr":
        eqn2.t = eqn2.t/3600
        print("The answer is " + str(eqn2.t) + " hours")
        input("Press ENTER to continue...")

    elif time_unit == "mins":
        eqn2.t = eqn2.t/60
        print("The answer is " + str(eqn2.t) + " minutes")
        input("Press ENTER to continue...")

    elif time_unit == "secs":
        print("The answer is " + str(eqn2.t) + " seconds")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn2_time()













def eqn3_initial_velocity():
    print("The default unit for initial velocity is m/s")
    print("Type \"kmh\" if you want the initial velocity in km/h")
    print("Type \"cms\" if you want the initial velocity in cm/s")
    print("Type \"ms\" if you want the initial velocity in m/s")
    initial_velocity_unit = input("Enter your choice: ")
    print()
    initial_velocity_unit = initial_velocity_unit.lower()

    if initial_velocity_unit == "kmh":
        eqn3.u = eqn3.u/0.277777778
        print("The answer is " + str(eqn3.u) + " km/h")
        input("Press ENTER to continue...")

    elif initial_velocity_unit == "cms":
        eqn3.u = eqn3.u*100
        print("The answer is " + str(eqn3.u) + " cm/s")
        input("Press ENTER to continue...")

    elif initial_velocity_unit == "ms":
        print("The answer is " + str(eqn3.u) + " m/s")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn3_initial_velocity()


def eqn3_final_velocity():
    print("The default unit for final velocity is m/s")
    print("Type \"kmh\" if you want the final velocity in km/h")
    print("Type \"cms\" if you want the final velocity in cm/s")
    print("Type \"ms\" if you want the final velocity in m/s")
    final_velocity_unit = input("Enter your choice: ")
    print()
    final_velocity_unit = final_velocity_unit.lower()

    if final_velocity_unit == "kmh":
        eqn3.v = eqn3.v/0.277777778
        print("The answer is " + str(eqn3.v) + " km/h")
        input("Press ENTER to continue...")

    elif final_velocity_unit == "cms":
        eqn3.v = eqn3.v*100
        print("The answer is " + str(eqn3.v) + " cm/s")
        input("Press ENTER to continue...")

    elif final_velocity_unit == "ms":
        print("The answer is " + str(eqn3.v) + " m/s")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn3_final_velocity()


def eqn3_acceleration():
    print("The default unit for acceleration is m/s\u00b2")
    print("Type \"kmh2\" if you want the acceleration in km/h\u00b2")
    print("Type \"cms2\" if you want the acceleration in cm/s\u00b2")
    print("Type \"ms2\" if you want the acceleration in m/s\u00b2")
    acceleration_unit = input("Enter your choice: ")
    print()
    acceleration_unit = acceleration_unit.lower()

    if acceleration_unit == "kmh2":
        eqn3.a = eqn3.a*(0.00007716049382716049)
        print("The answer is " + str(eqn3.a) + " km/h\u00b2")
        input("Press ENTER to continue...")

    elif acceleration_unit == "cms2":
        eqn3.a = eqn3.a*0.01
        print("The answer is " + str(eqn3.a) + " cm/s\u00b2")
        input("Press ENTER to continue...")

    elif acceleration_unit == "ms2":
        print("The answer is " + str(eqn3.a) + " m/s\u00b2")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn3_acceleration()



def eqn3_distance():
    print("The default unit for distance is metre")
    print("Type \"km\" if you want the distance in kilometre")
    print("Type \"cm\" if you want the distance in centimetre")
    print("Type \"m\" if you want the distance in metre")
    distance_unit = input("Enter your choice: ")
    print()
    distance_unit = distance_unit.lower()

    if distance_unit == "km":
        eqn3.s = eqn3.s/1000
        print("The answer is " + str(eqn3.s) + " kilometre")
        input("Press ENTER to continue...")

    elif distance_unit == "cm":
        eqn3.s = eqn3.s*100
        print("The answer is " + str(eqn3.s) + " centimetre")
        input("Press ENTER to continue...")

    elif distance_unit == "m":
        print("The answer is " + str(eqn3.s) + " metre")
        input("Press ENTER to continue...")

    else:
        print("Please choose the correct option.")
        print("\n===============================================================\n")
        eqn3_distance()












