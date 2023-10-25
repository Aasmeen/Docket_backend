import re

def camel_to_snake_case(body):
    result = {}
    for key, value in body.items():
        result.update({re.sub(r'([A-Z])', r'_\1', key).lower(): value})
    return result


def snake_to_camel_case(body):
    def convert(word):
        # Split the string by underscores and capitalize each word
        words = word.split('_')
        camel_words = [word.capitalize() for word in words]

        # Join the words together without spaces
        camel_case_string = ''.join(camel_words)

        # Make the first character lowercase (traditional camel case)
        camel_case_string = camel_case_string[0].lower() + camel_case_string[1:]

        return camel_case_string

    result = {}
    for key, value in body.items():
        result.update({convert(key): value})
    return result
