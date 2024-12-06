def is_decreasing(arr):
   return all(arr[i]>arr[i+1] for  i in range(len(arr)-1))

def is_increaing(arr):
   return all(arr[i]<arr[i+1] for  i in range(len(arr)-1))

def safe_reports1(data):
    count = 0 # count of safe reports
    for line in data.splitlines():
        arr = list(map(int, line.split()))
        if (is_decreasing(arr) or is_increaing(arr)) and (all((abs(arr[i]-arr[i+1]) <=3) for i in range(len(arr)-1))):
            count = count + 1
    print(count)

def safe_reportsPM(data):
    def is_safe(arr):
        increasing = all(arr[i] < arr[i+1] and 1 <= abs(arr[i] - arr[i+1]) <= 3 for i in range(len(arr)-1))
        decreasing = all(arr[i] > arr[i+1] and 1 <= abs(arr[i] - arr[i+1]) <= 3 for i in range(len(arr)-1))
        return increasing or decreasing

    count = 0  # Count of safe reports
    for line in data.splitlines():
        arr = list(map(int, line.split()))
        # Check if the report is already safe
        if is_safe(arr):
            count += 1
            continue
        # Try removing one level and check if it becomes safe
        for i in range(len(arr)):
            modified_arr = arr[:i] + arr[i+1:]  # Remove one element
            if is_safe(modified_arr):
                count += 1
                break  # No need to try further
    print(count)

def main():
    tf = open("aoc2Input")
    data = tf.read()
    tf.close()
    safe_reports1(data)
    safe_reportsPM(data)

if __name__ =="__main__":
    main()