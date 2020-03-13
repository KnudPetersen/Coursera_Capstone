
tal = 10
for i in range(tal):
    print("Hello world!")

print("doh")


s = "abcdollibolliefghijk"

current = s[1]
longest = current

for letter in s[1:]:
    if letter >= current:
        longest = current
    else:
        current += letter
print(longest)

