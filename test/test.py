from pyparsing import nums, Word
from main import shift_register


def parsing(variable):
    input_test = (Word(nums))('input_test')
    output_test = (Word(nums))('output_test')
    full_test = input_test + '/' + output_test
    res = full_test.parseString(variable)
    input_test = int(res.input_test)
    output_test = int(res.output_test)
    return input_test, output_test


def read_test_sequences():
    f = open('../test/test_sequences.txt', 'r')
    list_of_input_lists = []
    list_of_output_lists = []
    for itr in f.read().splitlines():  # разбиваем файл на строки
        input_seq = []
        output_seq = []
        for i in itr.split():
            input_test, output_test = parsing(i)
            input_seq.append(input_test)
            output_seq.append(output_test)
        list_of_input_lists.append(input_seq)
        list_of_output_lists.append(output_seq)
    return list_of_input_lists, list_of_output_lists


def test_register():
    input_lists, output_lists = read_test_sequences()
    reg_out_lists = []
    for i in input_lists:
        reg_output = shift_register(i)
        reg_out_lists.append(reg_output)
    assert reg_out_lists == output_lists
