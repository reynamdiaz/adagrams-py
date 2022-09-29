LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2,'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2,  'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}

def draw_letters():
    letters_not_drawn = list(LETTER_POOL.keys())
    letters_drawn = []
    letter_count = 0

    for letter in letters_not_drawn:
        if letter not in letters_drawn and len(letters_drawn) < 10:
            letters_drawn.append(letter)
            letter_count += 1
    return letters_drawn

def uses_available_letters(word, letter_bank):
    word = word.upper()
    word_dict = {}
    is_valid = False
    letter_count = 0

    for letter in word:
        if letter in letter_bank and word.count(letter) <= letter_bank.count(letter):
            word_dict[letter] = True
            letter_count += 1
            is_valid = True
        elif not letter in letter_bank:
            word_dict[letter] = False
            is_valid = False
    return is_valid
    
def score_word(word):
    score = 0
    word = word.upper()
    points = {
        1:["A", "E", "I", "O", "U","L", "N", "R", "S", "T"], 
        2:["D", "G"], 
        3:["B", "C", "M", "P"], 
        4:["F", "H", "V", "W", "Y" ],
        5:["K"],
        8:["J", "X"],
        10: ["Q", "Z"] 
        }

    for letter in word:    
        for key, value in points.items():
            if letter in value:
                score += key    
    
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass
# word list is a list of strings
# 1. use score_word() to get the score of each word in word list:
    # for word in word_list:
        #word_score = score_word(word) -- 
        # ~~ do we want to append this to a list of word scores?
        # ~~ or make a dict with word : score as the key, value pair?

# 2. get highest score using list or dict w/ highest scores
        # for score in scores:
            # something
# 3. if tie: 
    # if len(tied_word) > len(other_tied_word):
        # tied_word wins!
        # unless len(other_tied_word) > 10
            # then 10 letter word wins
        # if len(tied_word) == len(other_tied_word):
        #   first one wins 
        # ? ???? ? 
        #    
# return: tuple with two elements, ([highest scoring word], [score])