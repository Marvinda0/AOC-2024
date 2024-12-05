def main():
    tf = open("aoc1Input")
    data = tf.read()
    tf.close()
    result = 0
    list1 = []
    list2 = []
    for line in data.splitlines():
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
        list1s = sorted(list1)
        list2s = sorted(list2)
    for i in range(len(list1)):
        d = abs(list1s[i]-list2s[i])
        result += d
    print(result)
if __name__=="__main__":
    main()