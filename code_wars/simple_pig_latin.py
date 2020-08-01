'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.


'''


def pig_it(text):
    punc_ref = None
    if text.endswith("!"):
        punc_ref = text[text.find("!")]

    if text.endswith("."):
        punc_ref = text[text.find(".")]

    if text.endswith("?"):
        punc_ref = text[text.find("?")]

    word_list = text.split()
    new_list = ''
    for word in word_list:
        if word == '!' or word == '.' or word == '?':
            break

        f_letter = word[0]

        remain = word[1:]
        conv = remain + f_letter + 'ay' + ' '
        new_list += conv

    if punc_ref:
        result = str(str(new_list) + '' + str(punc_ref)).strip()
        return result
    else:
        return new_list.strip()


assert pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay'
assert pig_it('Hello world !'), 'elloHay orldway !'
