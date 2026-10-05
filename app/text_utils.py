"""Small text helpers used in the Git exercises."""


def slugify(text):
    return "-".join(text.lower().split())


def title_case(text):
    return " ".join(word.capitalize() for word in text.split())


def truncate(text, limit):
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."
