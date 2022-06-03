"""
HackerRank Day 8 Dictionaries and Maps


*Task*
Given names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of names
to query your phone book for. For each name queried, print the associated entry from your
phone book on a new line in the form name=phoneNumber;
if an entry for name is not found, print Not found instead.
"""

n = int(input())
all_entries = [input().split() for _ in range(n)]
phone_book = {k: v for k, v in all_entries}

while True:
    try:
        query = input()
        if query in phone_book:
            print(query + "=" + phone_book[query])
        else:
            print("Not found")
    except EOFError:
        break
