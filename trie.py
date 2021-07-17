class Trie:
    def __init__(self):
        self.child = {}
    

    def insert(self, word):
        current = self.child

        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        
        current["#"] = 1


    def search(self, word):
        current = self.child

        for c in word:
            if c not in current:
                return False
            current = current[c]
        
        return "#" in current
