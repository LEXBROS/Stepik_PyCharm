alphabet = {chr(i): (i - 96) for i in range(ord('a'), ord('z') + 1)}
for key, value in alphabet.items():
    print(key, value)
