# Upper & Lower
"Mountains".upper();
"MOUNTAINS".lower();

#Strip, remove space
" Yes ".strip();
" Yes ".lstrip();
" Yes ".rstrip();

#Count, to count how many substring occurs in string
"The number e occurs in this string is 3".count();

#Endswith, to check last string contain some substring
"Forest".endswith("rest");

#isNumeric, to check string contain number
"Forest".isnumeric();

#Join
" ".join(["This", "is", "the", "phrase", "joined"]);

#Split
"This is another example".split();

#Latihan, to get first letter of string
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS