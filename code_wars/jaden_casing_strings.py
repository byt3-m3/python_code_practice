def main():
    pass


def to_jaden_case(string):
    sting_list = string.split(" ")

    new_str = ""
    for word in sting_list:
        new_str += f'{word.capitalize()} '

    return new_str.strip()


if __name__ == "__main__":
    quote = "How can mirrors be real if our eyes aren't real"
    r = to_jaden_case(quote)
    print(r)
