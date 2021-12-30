import re
class Filter:
    def __init__(self, path):
        self.book = open(path)
        self.bookStr = self.book.read()
        self.bookToToken = ''

    def DeletePageNumbers(self):
        # Delete Page Numbers
        self.bookStr = re.sub(r'\bPage \| .*\b', '', self.bookStr)
        # print(firstFileRaw)

    def DeleteMultiLines(self):
        # Delete multilines
        self.bookStr = re.sub(r'\n[\n]*', '\n', self.bookStr)
        # print(firstFileRaw)

    def DeleteChaptersNames(self):
        # Delete chapters' names
        chapter = 1
        for line in self.bookStr.split('\n'):
            line = line.strip()
            if (line == ''):
                continue
            allUpper = True
            for flag in [(lambda ch: ch.isspace() or (ch.isalpha() and ch.isupper()))(ch) for ch in line]:
                allUpper = allUpper and flag
            if (allUpper):
                # print(f'chapter {chapter}-> {line}')
                chapter += 1
            else:
                self.bookToToken += line + " "

    def LowreringChars(self):
        # Lowering all chars
        tmp = ''
        for ch in self.bookToToken:
            to = ch
            if (ch.isalpha()):
                to = ch.lower()
            tmp += to
        self.bookToToken = tmp

    def GetText(self):
        return self.bookStr

    def GetWords(self):
        self.DeletePageNumbers()
        self.DeleteMultiLines()
        self.DeleteChaptersNames()
        self.LowreringChars()
        words = self.bookToToken.split(' ')
        # print(len(words))

        return words
