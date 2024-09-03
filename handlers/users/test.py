from handlers.users.transliterate import to_cyrillic, to_latin


# msg = "salom"
# print(to_latin(msg))
# result = lambda msg: to_cyrillic(msg) if msg.isascii() else msg
# result_lo = lambda msg: to_latin(msg) if msg.isascii() else msg
# dori = result(msg)
# dori_lo =result_lo(msg)
# print(to_latin(dori))
# print(to_latin(dori_lo))
# print(to_latin("сум"))


def Togirlash(msg):
    lenthe = len(msg)
    text = ""
    for i in range(lenthe):
        if msg[i] == "қ":
            text = text + "к"
        elif msg[i] == "Қ":
            text = text + "К"

        elif msg[i] == "Ғ":
            text = text + "Г"
        elif msg[i] == "ғ":
            text = text + "г"

        elif msg[i] == "ҳ":
            text = text + "х"
        elif msg[i] == "Ҳ":
            text = text + "Х"

        elif msg[i] == "Ў":
            text = text + "У"
        elif msg[i] == "ў":
            text = text + "у"

        else:
            text = text + msg[i]
    return text

print(Togirlash("Bobomurod Sirojiddinov"))