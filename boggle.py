dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def search(starty, startx, checkpos, split_word, boggle):
    cache = [[[-1 for x in range(5)] for y in range(5)] for z in range(10)]
    for i in range(8):
        if 0 <= starty + dy[i] < 5 and 0 <= startx + dx[i] < 5:
            if boggle[starty + dy[i]][startx + dx[i]] == split_word[checkpos]:
                if checkpos == len(split_word) - 1:
                    return 1
                ret = cache[checkpos][starty][startx]
                if ret != -1:
                    return ret
                cache[checkpos][starty][startx] = search(starty + dy[i], startx + dx[i], checkpos + 1, split_word, boggle)
    return cache[checkpos][starty][startx]


def check_word(boggle, word):
    for i in range(5):
        for j in range(5):
            w = list(word)
            if boggle[i][j] == w[0]:
                if search(i, j, 1, w, boggle) == 1:
                    print(str.format("{} {}", word, "YES"))
                    return
    print(str.format("{} {}", word, "NO"))


c = input()
boggle = []
for i in range(int(c)):
    for j in range(5):
        boggle_row = input()
        boggle.append(list(boggle_row))

    n = input()
    word = []
    for j in range(int(n)):
        word_row = input()
        word.append(word_row)
    for w in word:
        check_word(boggle, w)

# 1
# NNNNS
# NEEEN
# NEYEN
# NEEEN
# NNNNN
# 2
# YES
# SEVEN

# 1
# URLPM
# XPRET
# GIAET
# XTNZY
# XOQRS
# 6
# PRETTY
# GIRL
# REPEAT
# KARA
# PANDORA
# GIAZAPX
