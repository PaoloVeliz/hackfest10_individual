if __name__ == "__main__":
    f = open("dataejercicio1.txt", "r")
    data = []
    x = 0
    result = 0
    for line in f:
        line = line.strip()
        data.append(line.split(','))