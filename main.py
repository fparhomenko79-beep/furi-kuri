def clean_text(raw_text: str) -> list[str]:
    """Очищает текст от пунктуации и разбивает на отдельные слова."""
    punctuation = ".,!?;:()[]{}*&^%$#@-_=+`~'\"\\"
    cleaned = raw_text.lower()
    for char in punctuation:
        cleaned = cleaned.replace(char, " ")
    return cleaned.split()


def analyze_sentiment(words: list[str]) -> str:
    """Определяет эмоциональную окраску текста по маркерам."""
    positive_markers = {"круто", "классно", "хорошо", "отлично", "рад", "люблю", "интересно", "успех", "кайф", "fun"}
    negative_markers = {"плохо", "грустно", "ошибка", "сложно", "устал", "скучно", "проблема", "баг", "бесит"}

    pos_count = sum(1 for word in words if word in positive_markers)
    neg_count = sum(1 for word in words if word in negative_markers)

    if pos_count > neg_count:
        return "Позитивный 😊"
    elif neg_count > pos_count:
        return "Негативный 😔"
    return "Нейтральный 😐"


def calculate_stats(words: list[str]) -> dict[str, float | int]:
    """Считает количество слов и их среднюю длину."""
    if not words:
        return {"total_words": 0, "avg_word_len": 0.0}

    total_words = len(words)
    total_len = sum(len(word) for word in words)
    return {
        "total_words": total_words,
        "avg_word_len": round(total_len / total_words, 2)
    }


# Основной блок программы (работает последовательно)
print("--- Добро пожаловать в Умный Анализатор Текста! ---")
print("Введите любой текст (например, как прошел ваш день):")

user_input = input().strip()

if user_input:
    # Процесс обработки
    words_list = clean_text(user_input)
    stats = calculate_stats(words_list)
    sentiment = analyze_sentiment(words_list)

    # Вывод результатов
    print("\n==================================")
    print("       РЕЗУЛЬТАТЫ АНАЛИЗА         ")
    print("==================================")
    print(f"📊 Всего слов найдено: {stats['total_words']}")
    print(f"📏 Средняя длина слова: {stats['avg_word_len']} симв.")
    print(f"🎭 Настроение текста: {sentiment}")
    print("==================================")
else:
    print("Вы ничего не ввели. Перезапустите программу.")