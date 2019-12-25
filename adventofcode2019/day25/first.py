from collections import defaultdict

with open("input.txt") as inp:
    text = dict((ind, elem) for ind, elem in enumerate(inp.read().split(",")))
    opcodes_initial = defaultdict(lambda: '0', text)


def next_move(inp_tape):
    position = 0
    inp_position = 0
    base = 0
    opcodes = opcodes_initial.copy()

    while position < len(opcodes):
        op = opcodes[position]

        if len(op) > 2:
            C = int(op[-3])
        else:
            C = 0

        if len(op) > 3:
            B = int(op[-4])
        else:
            B = 0

        if len(op) > 4:
            A = int(op[-5])
        else:
            A = 0

        op = int(op[-2:])

        if op == 99:
            break

        first = int(opcodes[position + 1])

        if op == 3:
            # n = input('waiting for input:\n')
            if inp_position >= len(inp_tape):
                yield '-1'
            n = inp_tape[inp_position]
            inp_position += 1
            if C == 0:
                opcodes[first] = n
            elif C == 2:
                opcodes[first + base] = n
            else:
                raise Exception('cannot assign value to int')
            position += 2
        elif op == 4:
            if C == 0:
                yield opcodes[first]
            elif C == 2:
                yield opcodes[base + first]
            else:
                yield str(first)
            position += 2
        elif op == 9:
            if C == 0:
                base += int(opcodes[first])
            elif C == 2:
                base += int(opcodes[first + base])
            else:
                base += first
            position += 2
        else:
            if C == 0:
                first = int(opcodes[first])

            if C == 2:
                first = int(opcodes[first + base])

            second = int(opcodes[position + 2])
            if B == 0:
                second = int(opcodes[second])

            if B == 2:
                second = int(opcodes[second + base])

            result = int(opcodes[position + 3])
            if A == 2:
                result += base

            if op == 1:
                opcodes[result] = str(first + second)

            if op == 2:
                opcodes[result] = str(first * second)

            if op == 7:
                opcodes[result] = '1' if first < second else '0'
            if op == 8:
                opcodes[result] = '1' if first == second else '0'

            position += 4

            if op == 5:
                if first:
                    position = second
                else:
                    position -= 1
            if op == 6:
                if not first:
                    position = second
                else:
                    position -= 1


def explore():
    while True:
        try:
            res = int(next(gen))
            if 0 <= res <= 256:
                print(chr(res), end='')
            else:
                instruction = input()
                [inp_tape.append(str(ord(x))) for x in instruction + '\n']
        except StopIteration:
            break


if __name__ == '__main__':
    inp_tape = []
    gen = next_move(inp_tape)
    explore()


'''
 N
W E
 S
                                                                       Warp Drive Maintenance
                                                                                |
    Corridor*  - Holodeck  - Hallway*-------------------------------------Observatory *  
                     |       |                                                  |
        Gift Wrapping Center*|               Pressure-Sensitive Floor           |
                     |       |                         |                        |
                   Arcade*   |              Security Checkpoint--Science Lab*   |
                             |                                          |       |  
              Engineering-Sick Bay        Hot Chocolate Fountain*--Passages*--Stables*
                             |        
               Hull Breach-Storage-Navigation-Kitchen*
                                     |
                                  Crew Quarters*
                             
                             
                             * -- item
                             
'''