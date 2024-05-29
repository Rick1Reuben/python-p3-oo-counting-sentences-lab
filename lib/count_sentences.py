class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if not self._value:
            return 0
        sentences = self._value.split()
        count = 0
        for sentence in sentences:
            if sentence.endswith('.') or sentence.endswith('!') or sentence.endswith('?'):
                count += 1
        return count
