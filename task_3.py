import timeit
from search.kmp_search import kmp_search
from search.boyer_moore_search import boyer_moore_search
from search.rabin_karp_search import rabin_karp_search


def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def measure_time(func, text, pattern):
    timer = timeit.timeit(lambda: func(text, pattern), number=10)
    return timer / 10


def main():
    text1 = load_text('data/article_1.txt')
    text2 = load_text('data/article_2.txt')

    existing_substring_1 = "Жадібний алгоритм"
    existing_substring_2 = "Бінарні діаграми"
    non_existing_substring = "вигаданий підрядок"

    results = {
        "Article 1": {},
        "Article 2": {}
    }

    # Testing on text 1
    for name, func in [
        ("KMP", kmp_search),
        ("Boyer-Moore", boyer_moore_search),
        ("Rabin-Karp", rabin_karp_search)
    ]:
        results["Article 1"][name] = {
            "existing": measure_time(func, text1, existing_substring_1),
            "non_existing": measure_time(func, text1, non_existing_substring)
        }

    # Testing on text 2
    for name, func in [
        ("KMP", kmp_search),
        ("Boyer-Moore", boyer_moore_search),
        ("Rabin-Karp", rabin_karp_search)
    ]:
        results["Article 2"][name] = {
            "existing": measure_time(func, text2, existing_substring_2),
            "non_existing": measure_time(func, text2, non_existing_substring)
        }

    # Print results
    for article, data in results.items():
        print(f"\nExecution times for {article}:")
        print('-' * 14 + '+' + '-' * 24 + '+' + '-' * 24)
        print(f"{"Algorithm":^14}|{"Existing substring":^24}|"
              f"{"Not existing substring":^24}")
        print('-' * 14 + '+' + '-' * 24 + '+' + '-' * 24)
        for algorithm, times in data.items():
            print(f"{algorithm:<14}|{f"{times['existing']:.5f} sec":^24}|"
                  f"{f"{times['non_existing']:.5f} sec":^24}")
        print('-' * 14 + '+' + '-' * 24 + '+' + '-' * 24)


if __name__ == "__main__":
    main()
