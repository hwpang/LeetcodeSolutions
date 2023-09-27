def string_arithmetic_operation(string: str, operations: list=["+", "-", "*", "/"]) -> float:
    assert string != '', 'Empty string'
    assert isinstance(string, str), 'Not a string'

    operation = operations[0]
    substrings = string.split(operation)
    nums = []
    for substring in substrings:
        if any(op in substring for op in operations[1:]):
            nums.append(float(string_arithmetic_operation(substring, operations=operations[1:])))
        else:
            nums.append(float(substring))

    first_num = nums.pop(0)
    for num in nums:
        if operation == '+':
            first_num += num
        elif operation == '-':
            first_num -= num
        elif operation == '*':
            first_num *= num
        elif operation == '/':
            first_num /= num
        else:
            raise Exception('Invalid operation')
        
    return first_num

assert string_arithmetic_operation('1+2+3+4') == 1+2+3+4
assert string_arithmetic_operation('1*2*3*4') == 1*2*3*4
assert string_arithmetic_operation('1+2*3+4') == 1+2*3+4
assert string_arithmetic_operation('1/2*3/4') == 1/2*3/4
assert string_arithmetic_operation('1+2-3*4/5') == 1+2-3*(4/5)
