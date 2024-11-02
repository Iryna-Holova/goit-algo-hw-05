def bad_char_heuristic(pattern):
    # Create an array to store the last occurrence of each character
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def good_suffix_heuristic(pattern):
    m = len(pattern)
    # Create an array to store the good suffix length
    good_suffix = [0] * (m + 1)
    # Initialize the good suffix array
    border_pos = [-1] * (m + 1)
    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        # Check if the current character matches the pattern
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            # If the character does not match, update the good suffix length
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            # Update the border position
            j = border_pos[j]
        i -= 1
        j -= 1
        # Update the border position
        border_pos[i] = j

    j = border_pos[0]
    for i in range(m + 1):
        # If the character does not match, update the good suffix length
        if good_suffix[i] == 0:
            good_suffix[i] = j
        # If the character matches the pattern, update the border position
        if i == j:
            j = border_pos[j]

    return good_suffix


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    bad_char = bad_char_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)

    i = 0  # Shift index for the search
    while i <= n - m:
        j = m - 1  # Shift index for the pattern

        # Check if the current character matches the pattern
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        # If patten is found
        if j < 0:
            return i
        else:
            # Shift the search index
            bad_char_shift = j - bad_char.get(text[i + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            i += max(bad_char_shift, good_suffix_shift)

    return -1


def main():
    text = "ABAAABCDABCAB"
    pattern = "ABC"
    print(boyer_moore_search(text, pattern))


if __name__ == "__main__":
    main()
