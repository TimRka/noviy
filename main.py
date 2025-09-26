import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from collections import Counter


class LabWorkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Языки программирования 2 - Циклы, Списки, Словари, Множества")
        self.root.geometry("700x500")

        # Создаем notebook (вкладки)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Создаем вкладки
        self.create_cycles_tab()
        self.create_lists_tab()
        self.create_dicts_tab()
        self.create_sets_tab()
        self.create_combined_tab()

        # Поле для вывода результатов
        self.result_text = scrolledtext.ScrolledText(root, height=12, wrap=tk.WORD)
        self.result_text.pack(fill='x', padx=10, pady=5)
        self.result_text.config(state='disabled')

    def show_result(self, result):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))
        self.result_text.config(state='disabled')

    # ==================== ЦИКЛЫ ====================
    def create_cycles_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Циклы")

        # Поле ввода для задач с вводом
        tk.Label(tab, text="Введите число n:").pack(pady=5)
        self.cycles_entry = tk.Entry(tab, width=20)
        self.cycles_entry.pack(pady=5)
        self.cycles_entry.insert(0, "5")

        # Кнопки
        frame = tk.Frame(tab)
        frame.pack(pady=10)

        buttons = [
            ("Таблица умножения", self.multiplication_table),
            ("Сумма нечётных 1-100", self.sum_odd_100),
            ("Делители числа", self.find_divisors),
            ("Факториал", self.calculate_factorial),
            ("Последовательность Фибоначчи", self.fibonacci_sequence)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(frame, text=text, command=command, width=25)
            btn.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    def multiplication_table(self):
        result = "Таблица умножения:\n"
        for i in range(1, 10):
            for j in range(1, 10):
                result += f"{i}×{j}={i * j:2d}\t"
            result += "\n"
        self.show_result(result)

    def sum_odd_100(self):
        total = sum(i for i in range(1, 101) if i % 2 != 0)
        self.show_result(f"Сумма нечётных чисел от 1 до 100: {total}")

    def find_divisors(self):
        try:
            n = int(self.cycles_entry.get())
            divisors = [i for i in range(1, n + 1) if n % i == 0]
            self.show_result(f"Делители числа {n}: {divisors}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")

    def calculate_factorial(self):
        try:
            n = int(self.cycles_entry.get())
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            self.show_result(f"Факториал {n}! = {fact}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")

    def fibonacci_sequence(self):
        try:
            n = int(self.cycles_entry.get())
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[i - 1] + fib[i - 2])
            self.show_result(f"Последовательность Фибоначчи ({n} элементов):\n{fib}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")

    # ==================== СПИСКИ ====================
    def create_lists_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Списки")

        # Генерация случайного списка
        self.numbers = [random.randint(-50, 50) for _ in range(10)]
        tk.Label(tab, text=f"Сгенерированный список: {self.numbers}").pack(pady=5)

        # Кнопки
        frame = tk.Frame(tab)
        frame.pack(pady=10)

        buttons = [
            ("Чётные элементы", self.show_even_numbers),
            ("Макс и мин", self.show_min_max),
            ("Ввод 5 чисел", self.input_and_sort),
            ("Удалить дубликаты", self.remove_duplicates),
            ("Поменять местами", self.swap_first_last)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(frame, text=text, command=command, width=20)
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)

    def show_even_numbers(self):
        even = [x for x in self.numbers if x % 2 == 0]
        self.show_result(f"Чётные элементы: {even}")

    def show_min_max(self):
        self.show_result(f"Мин: {min(self.numbers)}, Макс: {max(self.numbers)}")

    def input_and_sort(self):
        def get_numbers():
            try:
                numbers = [int(entry.get()) for entry in entries]
                numbers.sort()
                self.show_result(f"Отсортированный список: {numbers}")
                dialog.destroy()
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректные числа")

        dialog = tk.Toplevel(self.root)
        dialog.title("Ввод 5 чисел")

        entries = []
        for i in range(5):
            tk.Label(dialog, text=f"Число {i + 1}:").grid(row=i, column=0, padx=5, pady=2)
            entry = tk.Entry(dialog, width=10)
            entry.grid(row=i, column=1, padx=5, pady=2)
            entries.append(entry)

        tk.Button(dialog, text="Готово", command=get_numbers).grid(row=5, column=0, columnspan=2, pady=10)

    def remove_duplicates(self):
        unique = []
        for num in self.numbers:
            if num not in unique:
                unique.append(num)
        self.show_result(f"Без дубликатов: {unique}")

    def swap_first_last(self):
        if len(self.numbers) >= 2:
            self.numbers[0], self.numbers[-1] = self.numbers[-1], self.numbers[0]
            self.show_result(f"После замены: {self.numbers}")
        else:
            self.show_result("Список слишком короткий для замены")

    # ==================== СЛОВАРИ ====================
    def create_dicts_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Словари")

        # Поле для ввода строки
        tk.Label(tab, text="Введите строку:").pack(pady=5)
        self.dicts_entry = tk.Entry(tab, width=30)
        self.dicts_entry.pack(pady=5)
        self.dicts_entry.insert(0, "hello world")

        # Кнопки
        frame = tk.Frame(tab)
        frame.pack(pady=10)

        buttons = [
            ("Средний балл", self.average_grade),
            ("Количество букв", self.letter_count),
            ("Квадраты чисел", self.number_squares),
            ("Из двух списков", self.from_two_lists)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(frame, text=text, command=command, width=20)
            btn.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    def average_grade(self):
        students = {"Иван": 85, "Мария": 92, "Петр": 78, "Анна": 95, "Сергей": 88}
        average = sum(students.values()) / len(students)
        result = f"Оценки: {students}\nСредний балл: {average:.2f}"
        self.show_result(result)

    def letter_count(self):
        text = self.dicts_entry.get()
        count_dict = {}
        for char in text:
            if char != ' ':
                count_dict[char] = count_dict.get(char, 0) + 1
        self.show_result(f"Количество букв в '{text}':\n{count_dict}")

    def number_squares(self):
        squares = {i: i ** 2 for i in range(1, 11)}
        self.show_result(f"Квадраты чисел 1-10:\n{squares}")

    def from_two_lists(self):
        keys = ['a', 'b', 'c', 'd']
        values = [1, 2, 3, 4]
        result_dict = dict(zip(keys, values))
        self.show_result(f"Ключи: {keys}\nЗначения: {values}\nСловарь: {result_dict}")

    # ==================== МНОЖЕСТВА ====================
    def create_sets_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Множества")

        # Поле для ввода
        tk.Label(tab, text="Введите число для фильтрации:").pack(pady=5)
        self.sets_entry = tk.Entry(tab, width=20)
        self.sets_entry.pack(pady=5)
        self.sets_entry.insert(0, "10")

        # Кнопки
        frame = tk.Frame(tab)
        frame.pack(pady=10)

        buttons = [
            ("Пересечение и объединение", self.set_operations),
            ("Уникальные слова", self.unique_words),
            ("Общие элементы", self.common_elements),
            ("Подмножество", self.check_subset),
            ("Фильтр по числу", self.filter_set)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(frame, text=text, command=command, width=25)
            btn.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    def set_operations(self):
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        intersection = set1 & set2
        union = set1 | set2
        result = f"Множество 1: {set1}\nМножество 2: {set2}\n"
        result += f"Пересечение: {intersection}\nОбъединение: {union}"
        self.show_result(result)

    def unique_words(self):
        text = self.dicts_entry.get()
        words = text.split()
        unique = set(words)
        self.show_result(f"Уникальные слова: {unique}")

    def common_elements(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        common = set(list1) & set(list2)
        self.show_result(f"Общие элементы: {common}")

    def check_subset(self):
        set_a = {1, 2, 3}
        set_b = {1, 2, 3, 4, 5}
        is_subset = set_a.issubset(set_b)
        self.show_result(f"{set_a} {'является' if is_subset else 'не является'} подмножеством {set_b}")

    def filter_set(self):
        try:
            threshold = int(self.sets_entry.get())
            numbers_set = {random.randint(-20, 20) for _ in range(10)}
            filtered = {x for x in numbers_set if x >= threshold}
            self.show_result(f"Исходное множество: {numbers_set}\nПосле фильтрации (≥{threshold}): {filtered}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")

    # ==================== КОМБИНИРОВАННЫЕ ====================
    def create_combined_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Комбинированные")

        # Поле для ввода
        tk.Label(tab, text="Введите предложение:").pack(pady=5)
        self.combined_entry = tk.Entry(tab, width=40)
        self.combined_entry.pack(pady=5)
        self.combined_entry.insert(0, "hello world hello python world")

        # Кнопки
        frame = tk.Frame(tab)
        frame.pack(pady=10)

        buttons = [
            ("Уникальные значения", self.unique_values),
            ("Частота элементов", self.element_frequency),
            ("Слова >5 символов", self.long_words),
            ("Количество слов", self.word_count),
            ("Убрать дубликаты", self.remove_dups_via_set),
            ("Самый дорогой товар", self.most_expensive),
            ("Частые имена", self.common_names),
            ("Индексы символов", self.char_indices)
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(frame, text=text, command=command, width=20)
            btn.grid(row=i // 4, column=i % 4, padx=2, pady=2)

    def unique_values(self):
        numbers = [random.randint(1, 10) for _ in range(20)]
        unique = {}
        true_unique = []
        for i in numbers:
            unique[i] = unique.get(i, 0) + 1
        for number, count in unique.items():
            if count == 1:
                true_unique.append(number)
        self.show_result(f"Случайные числа: {numbers}\nУникальные: {true_unique}")

    def element_frequency(self):
        numbers = [random.randint(1, 5) for _ in range(15)]
        freq = {}
        for num in numbers:
            freq[num] = freq.get(num, 0) + 1
        self.show_result(f"Числа: {numbers}\nЧастота: {freq}")

    def long_words(self):
        words = ["apple", "banana", "cat", "dog", "elephant", "fox"]
        long = {word for word in words if len(word) > 5}
        self.show_result(f"Слова: {words}\nДлиннее 5 символов: {long}")

    def word_count(self):
        text = self.combined_entry.get()
        words = text.split()
        count_dict = {}
        for word in words:
            count_dict[word] = count_dict.get(word, 0) + 1
        self.show_result(f"Количество слов: {count_dict}")

    def remove_dups_via_set(self):
        numbers = [random.randint(1, 5) for _ in range(10)]
        unique = list(set(numbers))
        self.show_result(f"Список: {numbers}\nБез дубликатов: {unique}")

    def most_expensive(self):
        products = {"apple": 50, "banana": 30, "orange": 70, "grape": 100}
        most_expensive = max(products, key=products.get)
        self.show_result(f"Товары: {products}\nСамый дорогой: {most_expensive} ({products[most_expensive]} руб.)")

    def common_names(self):
        names = ["Иван", "Мария", "Петр", "Иван", "Анна", "Мария", "Иван"]
        counter = Counter(names)
        duplicates = [name for name, count in counter.items() if count > 1]
        most_common = counter.most_common(1)[0]

        result = f"Имена: {names}\n"
        result += f"Повторяются: {duplicates}\n"
        result += f"Самое частое: {most_common[0]} ({most_common[1]} раз)"
        self.show_result(result)

    def char_indices(self):
        text = self.combined_entry.get()
        indices = {}
        for i, char in enumerate(text):
            if char not in indices:
                indices[char] = i
        self.show_result(f"Индексы символов: {indices}")


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = LabWorkApp(root)
    root.mainloop()