import re
import csv

def query_yes_no(question):
    while True:
        print(question)
        choice = input().lower()
        if choice == 'n':
            print("Exiting Script")
            exit()
        elif choice == 'y':
            return
        else:
            print("Please respond with Y/N:\n")

def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        fileName = "Replacement Rulebook.txt"
        accessMode = "r"
        with open(fileName, accessMode) as file:
            dataFromFile = csv.reader(file, delimiter="=")
            _str = re.sub('[^a-zA-Z0-9-_.$]', '', _str)
            for row in dataFromFile:
                if _str.upper() == row[0]:
                    user_string[j] = row[1]
            file.close()
        j = j + 1
    return (' '.join(user_string))

def is_number(x):
    if type(x) == str:
        x = x.replace(',', '')
    try:
        float(x)
    except:
        return False
    return True

def text2num (textnum, numwords={}):
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']

    if not numwords:
        numwords['and'] = (1, 0)
        for idx, word in enumerate(units): numwords[word.lower()] = (1, idx)
        for idx, word in enumerate(tens): numwords[word.lower()] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word.lower()] = (10 ** (idx * 3 or 2), 0)

    textnum = textnum.replace('-', ' ')

    current = result = 0
    curstring = ''
    onnumber = False
    lastunit = False
    lastscale = False

    def is_numword(x):
        if is_number(x):
            return True
        if word.lower() in numwords:
            return True
        return False

    def from_numword(x):
        if is_number(x):
            scale = 0
            increment = int(x.replace(',', ''))
            return scale, increment
        return numwords[x]

    for word in textnum.split():
        if (not is_numword(word.lower())) or (word.lower() == 'and' and not lastscale):
            if onnumber:
                curstring += repr(result + current) + " "
            curstring += word + " "
            result = current = 0
            onnumber = False
            lastunit = False
            lastscale = False
        else:
            scale, increment = from_numword(word.lower())
            onnumber = True

            if lastunit and (word.lower() not in scales):
                curstring += repr(result + current)
                result = current = 0

            if scale > 1:
                current = max(1, current)

            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

            lastscale = False
            lastunit = False
            if word.lower() in scales:
                lastscale = True
            elif word.lower() in units:
                lastunit = True

    if onnumber:
        curstring += repr(result + current)

    return curstring

def repeater(s):
    repeat_keywords = {'Double': 2, 'double': 2, 'Triple': 3, 'triple': 3}
    repeats = 0
    s = [ss.strip() for ss in s.split()][::-1]

    for i in range(len(s) - 1):
        if s[i - repeats + 1] in repeat_keywords:
            if len(s[i - repeats])!=1:
                continue
            s[i - repeats] *= repeat_keywords[s[i - repeats + 1]]
            del s[i - repeats + 1]
            repeats += 1
    return ' '.join(s[::-1])

while True:
    print("\nProvide Input Below:")
    myinput = input()
    if myinput.upper() == 'EXIT':
        print("Exiting Script")
        exit()
    myinput=text2num(translator(repeater(myinput)))
    print(myinput+"\n")
    query_yes_no("Do you want to continue? (Y|N)")