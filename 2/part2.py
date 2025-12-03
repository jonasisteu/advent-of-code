file = open("input.txt").read().split(',')

invalid_sum = 0

for ranges in file:
    start, finish = ranges.split('-')

    start = int(start)
    finish = int(finish)

    for current_id in range(start, finish + 1):
        string_id = str(current_id)
        for step in range(1, len(string_id)):
            is_invalid = True
            pattern = string_id[:step]
            for i in range(0, len(string_id), step):
                bit = string_id[i:step + i]
                if pattern != bit:
                    is_invalid = False
                    break
            if is_invalid:
                invalid_sum += current_id
                break

print(invalid_sum)
