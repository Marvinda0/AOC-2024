import re
def mulFinder(data):
    result = 0
    arr = re.findall("mul\\(([0-9]+,[0-9]+)\\)", data)
    for i in range(len(arr)):
        x = list(map(int,arr[i].split(",")))
        product = x[0]*x[1]
        result +=product
    return result
def mulFinder2(data):
    do = True
    prods = ""
    refined_data = " ".join(re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", data))
    parts = refined_data.split()
    for part in parts:
        if part == "don't()":
            do=False
        elif part == "do()":
            do=True
        if (part.startswith("mul") and do):
            prods += part
    result = mulFinder(prods)
    return result

    

def main():
    tf = open("aoc3Input")
    data = tf.read()
    tf.close()
    print(mulFinder(data))
    print(mulFinder2(data))
if __name__ == "__main__":
    main()