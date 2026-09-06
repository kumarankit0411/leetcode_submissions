class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.eow = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root

        for ch in word:
            idx = ord(ch)%ord('a')

            if temp.children[idx] is None:
                temp.children[idx] = self.TrieNode()

            temp = temp.children[idx]
        temp.eow = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, idx, node):

        if idx ==len(word):
            return node.eow

        ch = word[idx]

        if ch != '.':
            ch_idx = ord(ch)%ord('a')
            if node.children[ch_idx] is None:
                return False
            return self.searchHelper(word, idx+1, node.children[ch_idx])
        else:
            for possible_idx in range(26):
                if node.children[possible_idx] is not None:
                    rec_ans = self.searchHelper(word,idx+1,node.children[possible_idx])
                    if rec_ans:
                        return True

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)