import re
from operator import and_, or_, xor


def read_input(filename="input.txt"):
    with open(filename) as f:
        content = f.read()
        wires = {w: int(v) for w, v in re.findall(r"(\w+): (\d)", content)}
        gates = {
            w3: (w1, {"AND": and_, "OR": or_, "XOR": xor}[gate], w2)
            for (w1, gate, w2, w3) in re.findall(
                r"(\w+) ([A-Z]+) (\w+) -> (\w+)", content
            )
        }
        return wires, gates


def eval_wire(wire, wires, gates):
    if wire in wires:
        print(wire, "=", wires[wire])
        return wires[wire]
    if wire in gates:
        w1, gate, w2 = gates[wire]
        print(wire, "=", w1, gate.__name__, w2)
        value = gate(eval_wire(w1, wires, gates), eval_wire(w2, wires, gates))
        wires[wire] = value
        return value
    return None


def puzzle1():
    wires, gates = read_input()
    z_wires = sorted([w for w in gates if w.startswith("z")], reverse=True)
    return int("".join(str(eval_wire(w, wires, gates)) for w in z_wires), 2)

def verify_binary_adder(wire, wire_type, gates, faults=[]):
    wire_left, gate, wire_right = gates[wire]
    gate_type = {
        "output": xor,
        "carry": or_,
        "sum": xor,
    }
    wire_type_left, wire_type_right = {
        "output": ("carry", "sum"),
    }[wire_type] 

def puzzle2():
    wires, gates = read_input()
    for i in range(3, 46):



if __name__ == "__main__":
    print(puzzle2())
