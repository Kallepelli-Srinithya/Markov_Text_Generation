import random

# Read training text
with open("sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into words
words = text.split()

# Create Markov Chain dictionary
markov_chain = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    if current_word not in markov_chain:
        markov_chain[current_word] = []

    markov_chain[current_word].append(next_word)

# Generate text
def generate_text(length=30):
    current_word = random.choice(words)
    generated = [current_word]

    for _ in range(length - 1):
        if current_word in markov_chain:
            current_word = random.choice(markov_chain[current_word])
            generated.append(current_word)
        else:
            break

    return " ".join(generated)

# Output
print("\nGenerated Text:\n")
print(generate_text(50))