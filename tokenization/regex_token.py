circuits = [
    'XXX/123245//NY',
    'XXX/1585//NY',
    'XXX/1232456//NY',
    'XXX/123//NY',
    'XXX/123456//NY',
    'XXX/1232455//NY',
    'XXX/123245//NY',
    'XXX-65415---NY',
    'XXX-65415//NY',
    'XXX 65456 NY',
]


def create_tokens(circuit: str):

    if circuit.find("-") > 0:
        circuit = circuit.replace("-", "/")

    if circuit.find("_") > 0:
        circuit = circuit.replace("_", "/")

    if circuit.find(" ") > 0:
        circuit = circuit.replace(" ", "/")

    if circuit.find("/") > 0:
        tokens = circuit.split("/")
        tokens = [token for token in tokens if token]
        tokens.sort()
        return tokens


def get_first_token(tokens: list):
    first_token, *_ = tokens
    return first_token


def main():
    for ckt in circuits:
        tokens = create_tokens(circuit=ckt)
        print(get_first_token(tokens))

    string = 'XXX-65415-NY'
    print(string.find("-"))


if __name__ == "__main__":
    main()
