def isValidSubsequence(array, sequence):
    arr_id, seq_id = 0, 0
    while arr_id < len(array) and seq_id < len(sequence):
        if array[arr_id] == sequence[seq_id]:
            seq_id += 1
        arr_id += 1
    return seq_id == len(sequence)

