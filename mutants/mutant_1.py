def to_decimal(n):
    res = int(n, 2)
    return res


def shift_register_1(input_regs):
    initial_state = '000'
    register = [0, 0, 0]
    output_regs = []
    dec = to_decimal(initial_state)
    for input_reg in input_regs:
        if dec * 2 == 0:
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


def test_register_1():
    input_lists, output_lists = read_test_sequences()
    reg_out_lists = []
    for i in input_lists:
        reg_output = shift_register_1(i)
        reg_out_lists.append(reg_output)
    assert reg_out_lists == output_lists


def test_register_2():
    input_lists, output_lists = read_test_sequences()
    reg_out_lists = []
    for i in input_lists:
        reg_output = shift_register_2(i)
        reg_out_lists.append(reg_output)
    assert reg_out_lists == output_lists


def test_register_3():
    input_lists, output_lists = read_test_sequences()
    reg_out_lists = []
    for i in input_lists:
        reg_output = shift_register_3(i)
        reg_out_lists.append(reg_output)
    assert reg_out_lists == output_lists


def test_register_4():
    input_lists, output_lists = read_test_sequences()
    reg_out_lists = []
    for i in input_lists:
        reg_output = shift_register_4(i)
        reg_out_lists.append(reg_output)
    assert reg_out_lists == output_lists


def test_register_5():
    input_lists, output_lists = read_test_sequences()
    reg_out_lists = []
    for i in input_lists:
        reg_output = shift_register_5(i)
        reg_out_lists.append(reg_output)
    assert reg_out_lists == output_lists
