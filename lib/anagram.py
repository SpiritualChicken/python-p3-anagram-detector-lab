# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagram):
        return [anagram for anagram in possible_anagram if self.is_anagram(anagram)]
    
    def is_anagram(self, candidate):
        candidate = candidate.lower()
        return sorted(candidate) == sorted(self.word) and candidate != self.word