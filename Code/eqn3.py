import unit_convert_input as uci
import unit_convert_output as uco
import math

def eqn3v():
    global v
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.distance()
    print("\n===============================================================\n")
    v = math.sqrt((2 * uci.a * uci.s) + uci.u * uci.u)
    uco.eqn3_final_velocity()

def eqn3u():
    global u
    uci.final_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.distance()
    print("\n===============================================================\n")
    u = math.sqrt((uci.v * uci.v) - (2 * uci.a * uci.s))
    uco.eqn3_initial_velocity()

def eqn3a():
    global a
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.final_velocity()
    print("\n===============================================================\n")
    uci.distance()
    print("\n===============================================================\n")
    a = ((uci.u * uci.u) - (uci.v * uci.v))/(2 * uci.s)
    uco.eqn3_acceleration()

def eqn3s():
    global s
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.final_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    s = ((uci.u * uci.u) - (uci.v * uci.v))/(2 * uci.a)
    uco.eqn3_distance()