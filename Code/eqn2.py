import unit_convert_input as uci
import unit_convert_output as uco
import math

def eqn2s():
    global s
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.time()
    print("\n===============================================================\n")
    s = (uci.u * uci.t) + (0.5 * uci.a * uci.t * uci.t)
    uco.eqn2_distance()

def eqn2u():
    global u
    uci.distance()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.time()
    print("\n===============================================================\n")
    u = uci.s - (0.5 * uci.a * uci.t)
    uco.eqn2_initial_velocity()

def eqn2t():
    global t
    uci.distance()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.initial_velocity()
    print("\n===============================================================\n")
    v = math.sqrt((2 * uci.a * uci.s) + uci.u * uci.u)
    t = (v - uci.u)/uci.a
    uco.eqn2_time()

def eqn2a():
    global a
    uci.distance()
    print("\n===============================================================\n")
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.time()
    print("\n===============================================================\n")
    a = 2 * (uci.s - (uci.u * uci.t))/(uci.t * uci.t)
    uco.eqn2_acceleration()
