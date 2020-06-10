# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("/Users/kamilya/Downloads/Codecademy docs/censor_dispenser/email_one.txt", "r").read()
email_two = open("/Users/kamilya/Downloads/Codecademy docs/censor_dispenser/email_two.txt", "r").read()
email_three = open("/Users/kamilya/Downloads/Codecademy docs/censor_dispenser/email_three.txt", "r").read()
email_four = open("/Users/kamilya/Downloads/Codecademy docs/censor_dispenser/email_four.txt", "r").read()

def censor_alg(text, phrase):
    phrase_split = phrase.split()
    phrase_split_cens = []
    for word in phrase_split:
        word = 'X' * len(word)
        phrase_split_cens.append(word)
    phrase_censored = ' '.join(phrase_split_cens)
    if phrase in text:
        text = text.replace(phrase, phrase_censored)
    else:
        print('No such phrase in email! Will return original email.')
    return text

email_one_censored = censor_alg(email_one, 'learning algorithms')
#print(email_one_censored)

def censor_lst(text, lst):
    upd_lst = []
    for i in lst:
        upd_lst.extend([i, i.upper(), i.title()])
    for item in upd_lst:
        if item in text:
            text = text.replace(item, 'CENSORED')
    return text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_two_censored = censor_lst(email_two, proprietary_terms)
#print(email_two_censored)

def censor_neg(text, negs, lst):
    order = []
    for word in negs:
        order.append(text.find(word))
    positive_order = [n for n in order if n >= 0]
    sorted_order = sorted(positive_order)
    start = sorted_order[2]
    first_part = text[:start]
    second_part = text[start:]
    for item in negs:
        if item in second_part:
            second_part = second_part.replace(item, 'CENSORED')
    for item in lst:
        if item in first_part:
            first_part = first_part.replace(item, 'CENSORED')
        if item in second_part:
            second_part = second_part.replace(item, 'CENSORED')
    return first_part + second_part

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
email_three_censored = censor_neg(email_three, negative_words, proprietary_terms)
#print(email_three_censored)

def censor_all(text, negs, lst):
    text_to_list = text.split()
    combined_censors = negs + lst
    n = 0
    while n < len(text_to_list):
        for word in text_to_list:
            if text_to_list[n] in combined_censors:
                text_to_list[n] = 'CENSORED'
                if n > 0 and (text_to_list[n] != '.' and ',' and '!' and '?'):
                    text_to_list[n-1] = 'CENSORED'
                if n < len(text_to_list) - 1 and (text_to_list[n] != '.' and ',' and '!' and '?'):
                    text_to_list[n+1] = 'CENSORED'
            n += 1
    new_text = ' '.join(text_to_list)
    return new_text

email_four_censored = censor_all(email_four, negative_words, proprietary_terms)
print(email_four_censored)
    
