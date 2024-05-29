# ) Write a Python program to display plain text and cipher text using a Caesar
# encryption.
s1=input("enter your string")
s2=""
for ch in s1:
    ch1=ord(ch)+2
    s2+=chr(ch1)
print(s2)