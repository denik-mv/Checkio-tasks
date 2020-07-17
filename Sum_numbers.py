def sum_numbers(text: str) -> int:
    text_lst = text.split()
    result = 0
    for is_num in text_lst:
        if is_num.isdigit():
            result = result + int(is_num)
    return result


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('my numbers is 2'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0

