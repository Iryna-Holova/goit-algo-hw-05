# Substring Search Algorithm Comparison

This repository includes implementations and performance comparisons of three substring search algorithms:

1. Knuth-Morris-Pratt (KMP)
2. Boyer-Moore
3. Rabin-Karp

Additionally, it contains solutions for auxiliary tasks involving hash tables and binary search.

## Task 1: Adding delete Method to HashTable

Implemented a delete method for HashTable, enabling key-value pair removal to ensure efficient memory management and data consistency.

## Task 2: Binary Search for Sorted Arrays with Floating-Point Numbers

The binary search function returns a tuple with the number of iterations needed to find the element and the "upper bound," the smallest element that is greater than or equal to the target value.

## Task 3: Comparing Substring Search Algorithms

This task compares the efficiency of three substring search algorithms:

1. Knuth-Morris-Pratt (KMP)
2. Boyer-Moore
3. Rabin-Karp

### Goal

Compare the execution time of these algorithms for finding both an existing substring and a non-existent substring within two text files. The timeit module was used to measure execution times.

### Results

```bash
Execution times for Article 1:
--------------+------------------------+------------------------
  Algorithm   |   Existing substring   | Not existing substring
--------------+------------------------+------------------------
KMP           |      0.00322 sec       |      0.00204 sec
Boyer-Moore   |      0.00036 sec       |      0.00047 sec
Rabin-Karp    |      0.00322 sec       |      0.00646 sec
--------------+------------------------+------------------------

Execution times for Article 2:
--------------+------------------------+------------------------
  Algorithm   |   Existing substring   | Not existing substring
--------------+------------------------+------------------------
KMP           |      0.00262 sec       |      0.00363 sec
Boyer-Moore   |      0.00037 sec       |      0.00069 sec
Rabin-Karp    |      0.00493 sec       |      0.00710 sec
--------------+------------------------+------------------------
```

### Conclusions

**Boyer-Moore** is the fastest algorithm for both existing and non-existent substrings in both texts, due to its effective use of "bad character" and "good suffix" heuristics that skip irrelevant sections of the text.
**KMP** showed stable results but was slower than Boyer-Moore, particularly for non-existent substrings, likely due to its reliance on pattern preprocessing.
**Rabin-Karp** was the least efficient, especially for non-existent substrings, as its hashing-based approach is less optimal for large texts and mismatches.

### Running the Code

To run the tests and measure execution times, execute:

```bash
python task_3.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
