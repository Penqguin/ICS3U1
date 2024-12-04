def count_total_words(poem):
  words = poem.split()
  return len(words)


def count_vowel_words(poem):
  vowel_words = [word for word in poem.split() if word[0].lower() in 'aeiou']
  return len(vowel_words)


def find_words_starting_with_char(poem, char):
    return [word for word in poem.split() if word[0].lower() == char.lower()]

def combine_first_and_second_line(poem):
  line1 = poem.split('\n')[0]
  line2 = poem.split('\n')[1]
  return line1 + ' ' + line2

def main():
  with open('file handling\poem.txt', 'r') as file:
    poem = file.read()

  total_words = count_total_words(poem)
  vowel_words = count_vowel_words(poem)
  firstAndSecondLines = combine_first_and_second_line(poem)
  print(f'Total words: {total_words}')
  print(f'Words starting with a vowel: {vowel_words}')
  print(f"First and second lines: {firstAndSecondLines}")

  char = input('Enter a character: ')
  words_starting_with_char = find_words_starting_with_char(poem, char)

  if words_starting_with_char:
    print(f'Words starting with "{char}": {words_starting_with_char}')
  else:
    print(f'No words start with "{char}".')

main()