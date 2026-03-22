class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        queue = deque()
        queue.append([beginWord])
        result = []
        while queue:
            level_size = len(queue)
            chosen_word = set()
            for _ in range(level_size):
                sequence = queue.popleft()
                curr_word = sequence[-1]
                if curr_word == endWord:
                    result.append(sequence)
                    continue
                for i in range(len(curr_word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == curr_word[i]:
                            continue
                        new_word = curr_word[:i] + ch + curr_word[i+1:]
                        new_sequence = sequence + [new_word]
                        if new_word in wordSet:
                            new_sequence = sequence + [new_word]
                            queue.append(new_sequence)
                            chosen_word.add(new_word)
            for words in chosen_word:
                    wordSet.remove(words)
        return result   
