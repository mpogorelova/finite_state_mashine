def to_decimal(n):
    res = int(n, 2)
    return res


def shift_register_4(input_regs):
    initial_state = '000'
    register = [0, 0, 0]
    output_regs = []
    dec = to_decimal(initial_state)
    for input_reg in input_regs:
        if dec % 2 != 0:
            output_regs.append(0)
        else:
            output_regs.append(1)
        if register[0] == register[2]:
            register[2] = register[1]
            register[1] = 0
            register[0] = input_reg
        else:
            register[2] = register[1]
            register[1] = 1
            register[0] = input_reg
        reg = [str(r) for r in register]
        reg_state = ''.join(reg)
        dec = to_decimal(reg_state)
    return output_regs
