def all_combination(target: str, word_bank, memo=None):
    """
    Optimized solution to find all of the target word's substrings from a word bank, and return them as a list.
    The word from the word bank can be used as many as possible
    """
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    edge_array = []

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            edges = all_combination(suffix, word_bank, memo)
            for edge in edges:
                edge_array.append([word, *edge])
    memo[target] = edge_array
    return edge_array


if __name__ == "__main__":
    assert all_combination('purple', ['purp', 'p', 'ur', 'le', 'purpl']) == [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    assert all_combination('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']) == [
        ['ab', 'cd', 'ef'],
        ['ab', 'c', 'def'],
        ['abc', 'def'],
        ['abcd', 'ef']
    ]
    assert all_combination('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) == []
    assert all_combination('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']) == []