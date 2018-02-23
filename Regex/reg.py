import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{2} - \d{5}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return False


def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{2} - \d{5}-\d{4}\b')
	match = phone_regex.findall(input)
	if match:
		return match
	return False

def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{2} - \d{5}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	else:
		return False

def parse_bytes(input):
    bytes_regex = re.compile(r'\b[0|1]{8}\b')
    return bytes_regex.findall(input)

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)

print(extract_phone("My number is 12 - 98174-5827"))
print(extract_phone("My number is 12 - 981745827"))
print(extract_phone("My number is 122 - 981745827"))
print(is_valid_phone("12 - 98174-5827"))
