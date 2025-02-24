def isZigzag(numbers):
    result = []
    for i in range(len(numbers) - 2):
        a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
        if (a < b > c) or (a > b < c):
            result.append(1)
        else:
            result.append(0)
    return result

# Example usage
if __name__ == '__main__':
    numbers = list(map(int, input().split()))  # Read input as a list of integers
    result = isZigzag(numbers)
    print(result)

