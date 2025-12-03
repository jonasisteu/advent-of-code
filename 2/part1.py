file = open("input.txt").read().split(',')

invalid_sum = 0

for ranges in file:
    start, finish = ranges.split('-')

    start = int(start)
    finish = int(finish)

    for current_id in range(start, finish + 1):
        string_id = str(current_id)
        left, right = string_id[:len(string_id) // 2], string_id[len(string_id) // 2:]

        if left == right:
            invalid_sum += current_id

print(invalid_sum)
