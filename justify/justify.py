"""Module providing justify function."""


def justify(text: str, justify_len: int) -> list[str]:
    """Break text into justified lines of 'justify_len' length

    Arguments:
        text -- string to be justified
        justify_len -- length of each justified line

    Returns:
        Array of justified lines
    """
    words = text.split()
    result = []

    while len(words):
        words_line = []
        while len(words) and sum(map(len, words_line))+len(words_line)+len(words[0]) <= justify_len:
            words_line.append(words.pop(0))

        line_len = sum(map(len, words_line)) + len(words_line)
        spaces_to_add = justify_len - line_len

        if len(words) == 0:
            result.append(' '.join(words_line))
            break

        for i in range(spaces_to_add + 1):
            words_line[i % (len(words_line) - 1)] += ' '

        result.append(' '.join(words_line))

    return result
