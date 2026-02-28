import re


def replace_gender_word(text, pattern, replacement):
    return re.sub(pattern, replacement, text, flags=re.IGNORECASE)


def create_gender_pairs(text):

    patterns = [
        (r"\bhe\b", "she"),
        (r"\bshe\b", "he"),
        (r"\bhim\b", "her"),
        (r"\bher\b", "him"),
        (r"\bhis\b", "her"),
        (r"\bher\b", "his"),
    ]

    pairs = []

    for pattern, replacement in patterns:
        new_text = replace_gender_word(text, pattern, replacement)

        if new_text.lower() != text.lower():
            pairs.append((text, new_text))

    return pairs


def calculate_bias(analyzer, text):

    pairs = create_gender_pairs(text)

    if not pairs:
        return "Гендерні слова не знайдені", 0

    diffs = []

    for t1, t2 in pairs:
        _, s1 = analyzer.analyze(t1)
        _, s2 = analyzer.analyze(t2)
        diffs.append(abs(s1 - s2))

    bias = sum(diffs) / len(diffs)

    return "Bias calculated", bias

def interpret_bias(bias):
    
    if bias < 0.02:
        return "LOW bias"
    elif bias < 0.05:
        return "MEDIUM bias"
    else:
        return "HIGH bias"
