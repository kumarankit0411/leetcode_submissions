class Trie:
    class TrieNode:
        def __init__(self):
            self.eow = False
            self.children = [None] * 26

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root

        for ch in word:
            idx = ord(ch)%ord('a')

            if temp.children[idx] is None:
                temp.children[idx] = self.TrieNode()

            temp = temp.children[idx]
        temp.eow = True

    def search(self, word: str) -> bool:
        temp = self.root

        for ch in word:
            idx = ord(ch)%97

            if temp.children[idx] is None:
                return False

            temp = temp.children[idx]

        return temp.eow

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for ch in prefix:
            idx = ord(ch)%97

            if temp.children[idx] is None:
                return False

            temp = temp.children[idx]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)