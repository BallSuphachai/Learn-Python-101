questions = [
    '    555    ',
    '   2 + 3 = ?   ',
    'what do you want ?   ',
    '   why you leave me ?'
]

# - MAP
# --- Map version
# cleaned_questions = list(map(lambda q:q.strip().capitalize(), questions))
# print(cleaned_questions)

# --- list one-lined version
# clean_questions = [q.strip().capitalize() for q in questions]
# print(clean_questions)

# - FILTER
# --- Filter version
# filter_questions = list(filter(lambda q: len(q) >= 6, clean_questions))
# print(filter_questions)

# --- List one-lined version
# filtered_questions = [q for q in clean_questions if len(q) >= 6]
# print(filtered_questions)

# -----------------------------------------------------------------------
# - Zip
questions = [
    '5 x 5 = ?',
    '2 + 3 = ?',
]

answers = [
    '25',
    '5'
]

q_and_a = list(zip(questions, answers))
print(q_and_a)






