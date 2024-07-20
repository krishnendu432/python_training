# We will check here how to replace a value with in a string
letter='''Dear <|name|>,
Your application has been shortlisted in our next project.
Date:- <|Date|> '''
print(f"General format of the letter is:\n {letter}")
candidate_name=input("Enter the candidate name to whom you want to send letter :")
send_date=input("Enter the date on which date you send the letter :")
print(f"Letter of the {candidate_name} is :")
# 'letter' string has been replaced by 'candidate_name' variable.
# again the same string has been replaced by 'send_date' variable.
print(letter.replace("<|name|>",candidate_name).replace("<|Date|>", send_date))
