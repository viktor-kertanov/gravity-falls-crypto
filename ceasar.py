import re
from big_cipher import text
initial_alphabet = [
    'а',
    'б',
    'в',
    'г',
    'д',
    'е',
    'ё',
    'ж',
    'з',
    'и',
    'й',
    'к',
    'л',
    'м',
    'н',
    'о',
    'п',
    'р',
    'с',
    'т',
    'у',
    'ф',
    'х',
    'ц',
    'ч',
    'ш',
    'щ',
    'ъ',
    'ы',
    'ь',
    'э',
    'ю',
    'я',
]

en_alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]


def shift_alphabet(shift_key: int, alphabet: list[str]) -> list[str]:
    first_part, last_part = alphabet[: shift_key], alphabet[shift_key: ]
    return last_part + first_part


def cypher(msg: str, correct_alphabet: list[str], shift_key: int):
    if shift_key > len(correct_alphabet):
        print(f'Shift key {shift_key} is bigger than the alphabet [{len(correct_alphabet)}.')
        shift_key = shift_key % len(correct_alphabet)
        print(f'New shift key: {shift_key}')

    shifted_alphabet = shift_alphabet(shift_key, correct_alphabet)
    transposition = dict(zip(correct_alphabet, shifted_alphabet))
    
    msg = list(msg.lower().strip())

    cyphered_msg = []
    for l in msg:
        if l in transposition:
            cyphered_msg.append(transposition[l])
        else:
            cyphered_msg.append(l)


    return ''.join(cyphered_msg)

def decypher_msg(cyphered_msg: str, correct_alphabet: list[str], shift_key: int):
    if shift_key > len(correct_alphabet):
        print(f'Shift key {shift_key} is bigger than the alphabet [{len(correct_alphabet)}.')
        shift_key = shift_key % len(correct_alphabet)
        print(f'New shift key: {shift_key}')
    
    shifted_alphabet = shift_alphabet(shift_key, correct_alphabet)
    transposition = dict(zip(shifted_alphabet, correct_alphabet))

    cyphered_msg = list(cyphered_msg.lower().strip())
    decyphered_msg = []
    for l in cyphered_msg:
        if l in transposition:
            decyphered_msg.append(transposition[l])
        else:
            decyphered_msg.append(l)
    
    return ''.join(decyphered_msg)


def brute_force(cyphered_msg: str, correct_alphabet: list[str]) -> None:
    for idx in range(len(correct_alphabet)):
        decyphered_msg = decypher_msg(cyphered_msg, correct_alphabet, idx)
        print(f'Key: {idx}. Msg: {decyphered_msg}')

def atbash(cyphered_msg: str, correct_alphabet: list[str]):
    reversed_alpha = correct_alphabet[::-1]
    transposition = dict(zip(reversed_alpha, correct_alphabet))

    cyphered_msg = list(cyphered_msg.lower().strip())
    decyphered_msg = []
    for l in cyphered_msg:
        if l in transposition:
            decyphered_msg.append(transposition[l])
        else:
            decyphered_msg.append(l)
    
    return ''.join(decyphered_msg)

def num_cipher(alphabet: list[str]):
    idxes = list(range(1, len(alphabet)+1))
    transposition = dict(zip(idxes, alphabet))

    return transposition

def visioner_decrypt(msg: str, keyword: str, alphabet: list[str]) -> str:
    msg = list(msg.lower().strip())
    keyword = keyword.lower().strip()

    keyword_letter_skipper = []
    cur_letter_idx = 0
    for letter in msg:
        if letter in alphabet:
            keyword_letter_idx = cur_letter_idx % len(keyword)
            keyword_letter_skipper.append(keyword[keyword_letter_idx])
            cur_letter_idx+=1
        else:
            keyword_letter_skipper.append(None)

    decrypted_msg = []
    for letter_idx, letter in enumerate(msg):
        key_letter_of_keyword = keyword_letter_skipper[letter_idx]
        if key_letter_of_keyword is None:
            decrypted_msg.append(letter)
            continue
        keyword_shift = alphabet.index(key_letter_of_keyword)
        first_part, last_part = alphabet[:keyword_shift], alphabet[keyword_shift:]
        alphabet_row = last_part + first_part
        if letter in alphabet_row:
            letter_idx = alphabet_row.index(letter)
            decrypted_letter = alphabet[letter_idx]
            decrypted_msg.append(decrypted_letter)         
        else:
            decrypted_msg.append(letter)
    
    return ''.join(decrypted_msg)



if __name__ == '__main__':
    # proper_msg = 'attackatdawn'
    # keyword = 'lemon'
    # crypted_msg = 'LXFOPVEFRNHR'

    # decrypted_msg = visioner_decrypt(crypted_msg, keyword, en_alphabet)

    crypted_grav = text
    keyword = 'ПАЙНС'
    decrypted_gravity = visioner_decrypt(crypted_grav, keyword, initial_alphabet)

    print(decrypted_gravity)

    with open('blendin.txt', 'w') as f:
        f.write(decrypted_gravity)

    # a = shift_alphabet(5, initial_alphabet)
    cipher = '1 3 4 5'
    print(num_cipher(initial_alphabet))
    msg = 'Зижцодыы юегчя: швцьывым ёележеддеще цщыдизишц Шябиеж Шцвыдияде я ыще зсд, Щжыщщя Шя.'
    gravity_msg = 'Х шзёегядцф ие выие, бещъц гс зе Зиудвя вешявя дц Зездешсл ёйзиеоцл "ъэыжзяазбеще ътхшевц". Гцгц з ёцъёеа ицб я ды ёешыжявя, ние гс ыще шяъывя... '

    # cyphered_msg = cypher(msg, initial_alphabet, 3)

    decyphered_msg = decypher_msg(msg, initial_alphabet, 23)
    
    print(f'Initial message: {msg}')
    # print(f'Cyphered msg: {cyphered_msg}')
    print(f'Decyphered msg: {decyphered_msg}')
    print('------------')

    gravity_msg = 'Шсъ бе аа эи киэю, я щюабтш гавех яьпзйан, штшом сы шоа ьно ыц реыэахотщъбь!'
    mod_msg = atbash(gravity_msg, initial_alphabet)

    brute_force(gravity_msg, initial_alphabet)
    brute_force(mod_msg, initial_alphabet)

    d_msg = atbash(gravity_msg, initial_alphabet)

    print(d_msg)
    
    print('hello world')