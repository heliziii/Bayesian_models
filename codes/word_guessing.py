import string

words = []

#reading file
with open("hw1_word_counts_05.txt") as f:
    for line in f:
        line = line.split(" ")
        words.append([line[0],int(line[1])])

#computing p for each word
sum_words = 0
for word in words:
    sum_words += word[1]

P_words = {}
for word in words:
    P_words[word[0]] = word[1]/sum_words

sorted_p_words = sorted(P_words.items(), key=lambda item: item[1])
print([x[0] for x in sorted_p_words[0:15]])
print([x[0] for x in sorted_p_words[-15:]])


#predict next
def predictive(P_words, correctly_guessed, incorrectly_guessed):
    words = P_words.keys()

    indices = [i for i in range(5)]
    for correct_guess in correctly_guessed:
        indices.remove(correct_guess[1])

    seen_letters = [correct_guess[0] for correct_guess in correctly_guessed]
    candidate_letters = []
    for letter in string.ascii_uppercase:
        if letter in seen_letters:
            continue
        elif letter in incorrectly_guessed:
            continue
        else:
            candidate_letters.append(letter)
    p_li = {k:0 for k in candidate_letters}

    #computing denuminator of posterior
    sum_on_words = 0
    for word_ in words:
        evidence_ = 1
        for correct_guess in correctly_guessed:
            if word_[correct_guess[1]] != correct_guess[0]:
                evidence_ = 0
        for seen_letter in seen_letters:
            for index in indices:
                if word_[index] == seen_letter:
                    evidence_ = 0
        for incorrect_letter in incorrectly_guessed:
            if incorrect_letter in word_:
                evidence_ = 0
        sum_on_words += evidence_ * P_words[word_]

    for word in words:
        evidence = 1

        #compute posterior
        for correct_guess in correctly_guessed:
            if word[correct_guess[1]] != correct_guess[0]:
                evidence = 0
        for seen_letter in seen_letters:
            for index in indices:
                if word[index] == seen_letter:
                    evidence = 0
        for incorrect_letter in incorrectly_guessed:
            if incorrect_letter in word:
                evidence = 0
        posterior = (evidence * P_words[word])/sum_on_words

        #compute p for each letter in not seen letters
        for candidate_letter in candidate_letters:
            flag = 0
            for index in indices:
                if word[index] == candidate_letter:
                    flag = 1
            if flag == 1:
                p_li[candidate_letter] += posterior

    max = 0
    max_letter = ""
    for key in p_li:
        if p_li[key] > max:
            max = p_li[key]
            max_letter = key
    print(max_letter,max)


predictive(P_words, [], [])
predictive(P_words, [], ['E','A'])
predictive(P_words, [['A',0], ['S',4]], [])
predictive(P_words, [['A',0], ['S',4]], ['I'])
predictive(P_words, [['O',2]], ['A', 'E', 'M', 'N', 'T'])

predictive(P_words, [], ['E','O'])
predictive(P_words, [['D',0],['I',3]], [])
predictive(P_words, [['D',0],['I',3]], ['A'])
predictive(P_words, [['U',1]], ['A','E','I','O','S'])












