def deepest_lake(array=[]):
    if not array:
        return "no heights given"
    if not all(isinstance(x, (int, float)) for x in array):
        return "heights should be indicated in digits"

    array_length = len(array)
    if array_length < 3:
        return "no lakes here"

    deepest = 0
    lake_ranges = []
    start = None

    for i in range(array_length):
        if start is None and i != array_length - 1:
            if (array[i] > array[i - 1] and array[i] > array[i + 1]) or\
               (i == 0 and array[i] > array[i + 1]):
                start = i
                continue
        if (start is not None and i == array_length - 1) or\
           (i == array_length - 1 and array[i] > array[i - 1]):
            end = i
            lake_ranges.append((start, end))
            start = None

    if not lake_ranges:
        return "no lakes here"

    for start, end in lake_ranges:
        lake = array[start:end + 1]
        lake_depth = max(lake) - min(lake)
        deepest = max(deepest, lake_depth)

    return deepest