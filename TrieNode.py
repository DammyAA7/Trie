class TrieNode:
    def __init__(self):
        self.children = {} # dictionary of children nodes
        self.is_End_Of_Word = False # True if the node represents the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode() # root node of the trie

    def insert(self, word): # insert a word into the trie
        node = self.root # start at the root node
        for char in word: # iterate through the characters in the word
            if char not in node.children: # if the character is not in the children of the node
                node.children[char] = TrieNode() # create a new node if the character is not in the children
            node = node.children[char] # move to the child node
        node.is_End_Of_Word = True # mark the end of the word

    def search(self, word): # search for a word in the trie
        node = self.root
        for char in word:
            if char not in node.children:
                return False # return False if the character is not in the children of the node
            node = node.children[char] # move to the child node
        return node.is_End_Of_Word # return True if the node represents the end of a word
    
    def startsWith(self, prefix): # search for a prefix in the trie
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char] # move to the child node
        return True # return True if the prefix is found in the trie
