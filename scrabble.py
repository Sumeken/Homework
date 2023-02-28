word1 = str(input("Player 1: "))
word2 = str(input("Player 2: "))

SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def scrabble_word_score1(word1):
    score1 = 0
    for letter in word1:
        score1 += SCORES[letter]
    return score1

def scrabble_word_score2(word2):
    score2 = 0
    for letter in word2:
        score2 += SCORES[letter]
    return score2

score1= scrabble_word_score1(word1)
score2=scrabble_word_score2(word2)

while True:
    if score1>score2:
        print("Player1 win!")
        break
    elif score1<score2:
        print("Player2 win!")
        break
    else:
     print("Both win!")
     break

