character='e'

match character:
    case 'A' |'E' | 'I' | 'O' | 'U' | 'a' | 'e' | 'i' | 'o' | 'u':
        print(character," is a Vowel")
    case _:
        print("It is not a Vowel")
