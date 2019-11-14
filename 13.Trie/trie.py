"""
    实现字典树
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for char in word:
            cur = cur.child[char]
        cur.word = True

    def search(self,word):
        cur = self.root
        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return cur.word == True

    def start_with(self,prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return False