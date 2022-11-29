MIN_NUMBER = 50

while True:
    userResponse = input('Please enter a number: ')
    if not userResponse.isdecimal():
        print('You did not enter a valid number.')
        continue # this will skip all code below
    userResponse = int(userResponse)
    if userResponse < MIN_NUMBER:
        print('Your number is too low.')
    else:
        print('This is a good number. I like it.')
        continue
print('Goodbye.')