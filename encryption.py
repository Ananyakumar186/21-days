while(True):

    code1 = {
        'A': 1835,
        'B': 716467,
        'C': 842,
        'D': 7167,
        'E': 8745412,
        'F': 874541,
        'G': 84265,
        'H': 7145693,
        'I': 852,
        'J': 8521,
        'K': 714842,
        'L': 712,
        'M': 17593,
        'N': 1739,
        'O': 5,
        'P': 17854,
        'Q': 87453,
        'R': 178542,
        'S': 8451,
        'T': 7982,
        'U': 7139,
        'V': 729,
        'W': 71539,
        'X': 73591,
        'Y': 7591,
        'Z': 4826,
        ' ': 0
    }

    code2 = {
        '1835': 'A',
        '716467': 'B',
        '842': 'C',
        '7167': 'D',
        '8745412': 'E',
        '874541': 'F',
        '84265': 'G',
        '7145693': 'H',
        '852': 'I',
        '8521': 'J',
        '714842': 'K',
        '712': 'L',
        '17593': 'M',
        '1739': 'N',
        '5': 'O',
        '17854': 'P',
        '87453': 'Q',
        '178542': 'R',
        '8451': 'S',
        '7982': 'T',
        '7139': 'U',
        '729': 'V',
        '71539': 'W',
        '73591': 'X',
        '7591': 'Y',
        '4826': 'Z',
        '0': ' '




    }

    print(' press 1 to encrypt the code')
    print(' press 2 to decrypt the code')
    x = int(input("enter your choice"))

    if(x == 1):
        txt = input('enter data to be encoded')
        x = txt.split()

        if(len(x) == 0):
            raise ValueError('Data is empty')
        for k in range(0, len(x)):
            for j in code2:
                if(x[k] == j):
                    print(code2[j], end='')

    if(x == 2):
        data = input("Enter data to be decoded : ")
        if (len(data) == 0):
            raise ValueError('Data is empty')
        for k in range(0, len(data)):
            for j in code1:
                if(data[k] == j):
                    print(code1[j], end=" ")

       
