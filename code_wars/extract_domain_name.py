'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet
'''

import re


def domain_name(url):
    pattern = re.compile('(https://www.|http://www.|https://|http://|www\.|)(.*)')

    matches = pattern.match(url)

    if len(matches.groups()) == 2:
        _filtered = matches.groups()[1]

        return _filtered[:_filtered.find(".")]


if __name__ == "__main__":
    res = domain_name("http://google.co.jp")
    print(res)
