import re


class MultipleSentencesError(Exception):
    """Class that implements exceptions for inappropriate strings"""
    def __init__(self):
        self.message = "The sentence must be single."
        super().__init__(self.message)


class Sentence:
    def __init__(self, sentence: str):
        if self.check_input(sentence.strip()):
            self._sentence = sentence.strip()
            self._length = len(self._sentence)
            self._words_amount = len(self)

    @staticmethod
    def check_input(sentence):
        """Method that check correct of input"""
        if re.match(r"^\S+[0-9a-zA-Z_ ]+[.?!]*", sentence).string != sentence:
            raise MultipleSentencesError
        return True

    def _words(self):
        """Method, that returns generator for words in sentence"""
        for word in re.findall(r"\w+", self._sentence):
            yield word

    def _other_chars(self):
        """Method, that returns list of other chars in sentence"""
        return re.sub(r'[\w+]', " ", self._sentence).split()

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        try:
            if isinstance(item, slice):
                return " ".join(self.words[item.start:item.stop:item.step])
            return " ".join(self.words[item])
        except IndexError:
            raise IndexError("Sentence's word index out of range")

    @property
    def words(self):
        """Property, that returns list of words in sentence"""
        return list(self._words())

    @property
    def other_chars(self):
        """Property, that returns list of words in sentence"""
        return self._other_chars()

    def __iter__(self):
        return SentenceIterator(self._sentence, len(self))

    def __repr__(self):
        return f"Sentence({self._sentence})"


class SentenceIterator:
    """Class, that implements sentence iterator"""
    def __init__(self, sentence, length):
        self._sentence = sentence
        self._length = length
        self._index = -1

    def _get_word(self):
        if self._index < self._length - 1:
            self._index += 1
            return re.findall(r"\w+", self._sentence)[self._index]
        raise StopIteration

    def __next__(self):
        return self._get_word()

    def __iter__(self):
        return self


def main():
    s = Sentence("Все: и море, и суша – залито светом.")
    g = s._words()
    print(s)
    print(g)
    print(s.words)
    print(s.other_chars)
    print(s[-2:])
    print()
    for word in s:
        print(word)


if __name__ == '__main__':
    main()
