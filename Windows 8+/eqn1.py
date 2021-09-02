import unit_convert_input as uci
import unit_convert_output as uco

def eqn1v():
    global v
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.time()
    print("\n===============================================================\n")
    v = uci.u + (uci.a * uci.t)
    uco.eqn1_final_velocity()

def eqn1u():
    global u
    uci.final_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    uci.time()
    print("\n===============================================================\n")
    u = (uci.a * uci.t) - uci.v
    uco.eqn1_initial_velocity()

def eqn1a():
    global a
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.final_velocity()
    print("\n===============================================================\n")
    uci.time()
    print("\n===============================================================\n")
    a = (uci.v - uci.u)/uci.t
    uco.eqn1_acceleration()

def eqn1t():
    global t
    uci.initial_velocity()
    print("\n===============================================================\n")
    uci.final_velocity()
    print("\n===============================================================\n")
    uci.acceleration()
    print("\n===============================================================\n")
    t = (uci.v - uci.u)/uci.a
    uco.eqn1_time()