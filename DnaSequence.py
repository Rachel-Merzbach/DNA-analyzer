class DnaSequence:
    def __init__(self, seq):
        self.dna_sequence = ""
        self.__set(seq)

    def insert(self, char, index):
        if char not in ['A', 'T', 'C', 'G']:
            raise ValueError("char must be from A, T, C, G")
        if len(self.dna_sequence) >= index >= 0:
            self.dna_sequence = self.dna_sequence[:index] + char + self.dna_sequence[index:]

    def assignment(self, other):
        self.__set(other)
        return self.dna_sequence

    def get(self):
        return self.dna_sequence

    def __set(self, value):
        if not self.is_valid_dna(value):
            raise ValueError("value must be from A, T, C, G")
        self.dna_sequence = value

    def __str__(self):
        return self.dna_sequence

    def __eq__(self, other):
        return self.dna_sequence == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        return self.dna_sequence[item]

    def __setitem__(self, key, value):
        tmp_seq = list(self.dna_sequence)
        if type(key) == int and type(value) == str:
            tmp_seq[key] = value
            tmp_seq = "".join(tmp_seq)
            self.__set(tmp_seq)

    def __len__(self):
        return len(self.dna_sequence)

    @staticmethod
    def is_valid_dna(seq):
        return all(char in ['A', 'T', 'C', 'G'] for char in seq)
