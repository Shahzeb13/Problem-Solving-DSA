


def MorseCode(s):
    MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

    if not s:
        return "";

    upperCaseStr = s.upper();
    # print(upperCaseStr)
    EncodedStr = "";
    i = 0;
    while i < len(upperCaseStr):
        stringCharRef = upperCaseStr[i];

        if stringCharRef in MORSE_CODE:
            # EncodedStr += "".join(MORSE_CODE[stringCharRef]);
            EncodedStr += MORSE_CODE[stringCharRef] + " ";
        elif stringCharRef == " ":
            EncodedStr += "/";
        i +=1;
    return EncodedStr.strip();




res = MorseCode("sos sos");
print(res)
