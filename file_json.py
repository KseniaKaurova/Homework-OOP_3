import json
with open('newsafr.json') as f:
     d = json.load(f)
     words = {}
     for row in d['rss']['channel']['items']['title']:
         for word in row:
            if len(word) > 5 and word not in words:
                words[word] = row.count(word)
            elif len(word) > 5 and word in words:
                words[word] += row.count(word)

    sorted_words = dict(sorted(words.items(), key=lambda item: item[1]))
print(sorted_words.keys()[:10])
