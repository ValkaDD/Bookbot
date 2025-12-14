def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def word_count(ball):
    words = ball.split()
    return len(words)
def character_count(text):
    Characters ={}
    Lowered = text.lower()
    for i in Lowered:
        if i not in Characters.keys():
            Characters[i] = 1
        else:
            Characters[i] += 1
    return Characters