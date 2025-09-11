def marsExploration(s):
    sos_count = len(s)//3
    original_sos = sos_count * "SOS"
    changed_chars = sum(1 for i in range(len(s)) if s[i] != original_sos[i])
    return changed_chars


# Python Solution
def marsExploration(s):
    messages = [s[i:i + 3] for i in range(0, len(s), 3)]
    errors = 0

    for message in messages:
        print(message)
        if message != "SOS":
            if message[0] != "S":
                errors += 1
            if message[1] != "O":
                errors += 1
            if message[2] != "S":
                errors += 1

    return errors

def marsExploration(s):
    # Write your code here
    testStr = "SOS"
    lengthOfTestStr = len(testStr)
    index = 0
    result = 0
    for char in s:
        if char != testStr[index % lengthOfTestStr]:
            result += 1
        index += 1
    return result


def marsExploration(s):
    count = 0
    segments = re.findall(r'...', s)
    print(segments)

    for i in segments:
        for j, l in enumerate('SOS'):
            if l != i[j]:
                count += 1

    return count