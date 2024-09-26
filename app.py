from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Load 5-letter words from a text file
def load_five_letter_words(filename):
    with open(filename, 'r') as file:
        # Filter to include only 5-letter words
        five_letter_words = [line.strip().upper() for line in file if len(line.strip()) == 5]
    return five_letter_words

# Load the words into a list
word_list = load_five_letter_words('WORDS.txt')

# Choose a random word for the solution
solution_word = random.choice(word_list)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_word():
    guess = request.json['guess'].upper()
    result = []

    for i, letter in enumerate(guess):
        if letter == solution_word[i]:
            result.append('green')  # Correct position and letter
        elif letter in solution_word:
            result.append('yellow')  # Correct letter, wrong position
        else:
            result.append('gray')  # Incorrect letter

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    print(solution_word)
