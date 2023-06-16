

if __name__ == "__main__":
    f = open("dataejercicio1.txt", "r")
    data = []
    x = 0
    result = 0
    for line in f:
        line = line.strip()
        data.append(line.split(','))
    
    unclean_areas = []
    for level in data:
        unclean_areas.append((int(level[0])-int(level[2]))*(int(level[1])-int(level[3])))
    # obtener los cuadrados dentro
    inside_list = []
    inside_square = 0
    first_point = []
    second_point = []
    for idx, level in enumerate(data):
        for i in range(0,4):
            # print(data[1])
            if idx+1 < 3:
                if level[i] == data[idx+1][i]:
                    if i < 2:
                        first_point.append([data[idx][i],data[idx+1][i-1]])
                    else:
                        second_point.append([data[idx][i+1],data[idx+1][i]])
        inside_square = (int(first_point[0][0])-int(second_point[0][0]))*(int(first_point[0][1])-int(second_point[0][1]))                

    inside_list.append(inside_square)
    for square in unclean_areas:
        result = result + square
    for inside in inside_list:
        result = result - inside
    print(result)

