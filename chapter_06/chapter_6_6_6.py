# 6-6. Polling:

favorite_languages = {
    'josh': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }



respondents = ['phil', 'josh', 'david', 'rebecca', 'sarah', 'matt', 'danielle']
for respondent in respondents:
    if respondent in favorite_languages.keys():
        print("Thank you for taking the poll, " + respondent.title() + "!")
    else:
        print(respondent.title() + ", what's your favorite programming language?")