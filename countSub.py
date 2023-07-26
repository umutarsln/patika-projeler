
def count_substring(string, sub_string):
    count = 0
    start = 0

    while True:
        index = string.find(sub_string, start)
        if index == -1:
            break
        count += 1
        start = index + 1

    return count

string="ABCDCDC"
sub_string="CDC"
count = count_substring(string, sub_string)
print(count)
