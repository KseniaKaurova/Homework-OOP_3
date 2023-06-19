import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item')
words = {}
for new in news_list:
    rows = new.find('title')
    for row in rows:
        if len(row) > 5 and row not in words:
            words[row] = rows.count(row)
        elif len(row) > 5 and row in words:
            words[row] += rows.count(row)

    sorted_words = sorted(words.items(), key=lambda item: item[1]))
print(sorted_words.keys()[:10])
