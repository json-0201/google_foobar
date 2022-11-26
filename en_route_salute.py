'''
Write a program that counts how many salutes are exchanged during a typical walk along a hallway.
The hall is represented by a string. For example:
"--->-><-><-->-"
'''

def solution(s: str) -> int:

    num_salute = 0

    for i in range(len(s)):
        if s[i] == ">":
            num_salute += list(s[i:]).count("<")
    
    for j in range(len(s)-1,0,-1):
        if s[j] == "<":
            num_salute += list(s[:j]).count(">")

    return num_salute


solution("<<>><")