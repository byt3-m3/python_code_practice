def DNA_strand(dna):
    DNA_COMP_MAP = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    RNA = []
    for s in dna:
        r = DNA_COMP_MAP.get(s)
        RNA.append(r)

    return f"".join(RNA)


print(DNA_strand("AAAA"))
