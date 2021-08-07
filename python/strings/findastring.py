
def count_substring(string, sub_string):
    i = 0
    l = len(sub_string)
    for item in range(0, len(string)):
        if string[item:l+item] == sub_string:
            i+=1
        else:
            continue
    return i


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)