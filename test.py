import TrieNode

# create a new trie
trie = TrieNode.Trie()

trie.insert("apple") # insert "apple" into the trie
trie.insert("app") # insert "app" into the trie
trie.insert("banana") # insert "banana" into the trie
trie.insert("orange") # insert "orange" into the trie
trie.insert("pear") # insert "pear" into the trie

print(trie.search("apple")) # True

print(trie.search("pineapple")) # False

print(trie.startsWith("pe")) # True

print(trie.startsWith("xe")) # False
