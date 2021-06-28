import re


def solution(s):

    s = " ".join(s.split())
    text = re.split('[.?!]', s)
    text = [s.strip() for s in text]
    dl_before = 0
    for x in text:
        temp = x.split(" ")
        dl = len(temp)
        if dl > dl_before:
            dl_before = dl
    return dl_before


solution("We test coders. Give us a try?")
