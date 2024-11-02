def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_len = len(substring)
    main_string_len = len(main_string)

    base = 256  # Base for the polynomial hash function
    modulus = 101  # Modulus for the polynomial hash function

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(
        main_string[:substring_len],
        base,
        modulus
    )

    # Calculate the multiplier for the polynomial hash function
    h_multiplier = pow(base, substring_len - 1) % modulus

    for i in range(main_string_len - substring_len + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_len] == substring:
                return i

        if i < main_string_len - substring_len:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
                ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_len])
                ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def main():
    text = "ABAAABCDABCAB"
    pattern = "ABC"
    print(rabin_karp_search(text, pattern))


if __name__ == "__main__":
    main()
