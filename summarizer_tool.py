def run(text: str) -> str:
    """Return the first sentence as a simple 'summary'."""
    sentences = text.split('.')
    return sentences[0].strip() + '.' if sentences else text
