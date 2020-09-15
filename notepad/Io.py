
def Save(path, text):
    f = open(path.name, "w")
    f.write(text)
    f.flush()
    f.close()


def Open(path):
    f = open(path.name, "r")
    return f.read()
