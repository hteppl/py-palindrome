import traceback


def palindrome(num):
    size = len(num)
    res = set()
    for i in range(size):
        for j in range(i + 1, size):
            sub_e = num[i:j + 1]
            if sub_e == sub_e[::-1] and int(sub_e) > 9:
                res.add(int(sub_e))
    return sorted(res)


try:
    assert palindrome("1551") == [55, 1551]
    assert palindrome("221122") == [11, 22, 2112, 221122]
    assert palindrome("10015885") == [88, 1001, 5885]
    assert palindrome("13598") == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
