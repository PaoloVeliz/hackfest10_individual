import re

if __name__ == "__main__":
    f = open("data.txt", "r")
    data = []
    x = 0
    linexd = False
    result = ''
    for line in f:
        line = line
        data.append(line.replace('\n', ''))
    for line in data:
        linexd = False
        # print(len(line))
        result = ''
        for idx, char in enumerate(line):
            # result = result + char
            if char =="+":
                # result = result + 'eqid'
                if idx + 1 == len(line):
                    if x == 0:
                        result = result + char 
                    else:
                        equisde =  result + char
                        result = equisde + '\n' + equisde
                else:
                    result = result + char
            else:
                result = result + char
            #     if idx + 1 == len(line):
            #         continue
            #     else:
            #         if line[idx+1] == '-':
            #             continue
            #         else:
            #             result = result + char
            # else:
            #     result = result + char

        x = x + 1
        print(result)
