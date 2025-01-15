"""
Завдання 3
Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.
"""
import timeit


# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    skip = {c: skip.get(c, m) for c in text}
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == -1:
            return i
        i += skip.get(text[i + m - 1], m)
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    lps = [0] * m
    j = 0
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, q=101):
    n, m = len(text), len(pattern)
    if m > n:
        return -1
    d = 256
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Читання тексту з файлів
with open(r'C:\Users\Alona\Desktop\PROJECTS\goit-algo-hw-05\text1.md', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open(r'C:\Users\Alona\Desktop\PROJECTS\goit-algo-hw-05\text2.md', 'r', encoding='utf-8') as f:
    text2 = f.read()

# Підрядки
existing_substring_text1= "Експоненціальний пошук використовується для пошуку елементів шляхом"
non_existing_substring_text1 = "вигаданийпідрядок"
existing_substring_text2 = "кількість агентів 65536, кількість предметів 131072, кількість сесій 262144, розмір сесії 192, максимальна кількість вподобань 1536"
non_existing_substring_text2 = "фантастичнийпідрядок"

# Вимірювання часу для кожного алгоритму
def measure_time(text, pattern, algorithm):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

# Вимірювання часу виконання
for text, text_name, existing_substring, non_existing_substring in [(text1, "Text 1", existing_substring_text1, non_existing_substring_text1), (text2, "Text 2", existing_substring_text2, non_existing_substring_text2)]:
    for pattern, pattern_name in [(existing_substring, "Existing Substring"), (non_existing_substring, "Non-Existing Substring")]:
        print(f"{text_name} - {pattern_name}")
        print("Boyer-Moore:", measure_time(text, pattern, boyer_moore))
        print("Knuth-Morris-Pratt:", measure_time(text, pattern, kmp))
        print("Rabin-Karp:", measure_time(text, pattern, rabin_karp))
        print()

