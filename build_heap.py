# python3

def build_heap(data):
    n = len(data)
    swaps = []

    def heapify(i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and data[left] > data[largest]:
            largest = left

        if right < n and data[right] > data[largest]:
            largest = right

        if largest != i:
            swaps.append((i, largest))
            data[i], data[largest] = data[largest], data[i]
            heapify(largest)

    for i in range(n//2, -1, -1):
        heapify(i)

    return swaps


def main():
    
    input_text = input()
    if 'F' in input_text:
        input_file = input()
        input_file = "test/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    n = int(f.readline())          
                    data = list(map(int, f.readline().split()))

                    # checks if lenght of data is the same as the said lenght
                    assert len(data) == n

                    # calls function to assess the data 
                    # and give back all swaps
                    swaps = build_heap(data)

                    # TODO: output how many swaps were made, 
                    # this number should be less than 4n (less than 4*len(data))

                    # output all swaps
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)

            except FileNotFoundError:
                return print("File_not_found_error")

    if 'I' in input_text:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

        # calls function to assess the data 
        # and give back all swaps
        swaps = build_heap(data)

        # TODO: output how many swaps were made, 
        # this number should be less than 4n (less than 4*len(data))

        # output all swaps
        print(len(swaps))
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()