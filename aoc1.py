def main():
    tf = open("aoc1Input")
    data = tf.read()
    tf.close()
    result = 0
    similarity_score = 0
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
        count = list2.count(list1[i]) #count of how many times a number from the left column appears on the right one
        score = list1[i]*count
        similarity_score += score

    print(result) #Result for part 1 of day 1
    print(similarity_score) #Result for part 2 of day 1

if __name__=="__main__":
    main()