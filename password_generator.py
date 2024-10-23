# Import packages
import string
import random

# Write function to generate password
def pw_gen(size = 16, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

# Print generated password
print(pw_gen(int(input('How many characters in your password?'))))