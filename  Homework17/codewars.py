#https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []

    for start, end in intervals:
        if merged_intervals and merged_intervals[-1][1] >= start:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
        else:
            merged_intervals.append([start, end])

    total_length = sum(end - start for start, end in merged_intervals)

    return total_length
