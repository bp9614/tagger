import re


def tag_part_of_speech(sample_words, file=None):
    if file:
        file = open(file, 'w')

    if file:
        file.close()


def main():
    with open('sample/greenEggs.txt', 'r') as smp_file:
        sample_words = {word for line in smp_file.read().splitlines() for word
                        in filter(None, re.split("[a-z']", line.lower()))}

    tag_part_of_speech(sample_words)


with open('', 'r') as _dictionary:
    _part_of_speech = {word.lower(): participle.split('/') for word, participle
                       in [filter(None, line.split('\t')) for line
                           in _dictionary.read().splitlines()]}

if __name__ == '__main__':
    main()
