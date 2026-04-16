import wordcloud, json

with open('01-第1周/coding/meaningful_words.json', 'r', encoding='utf-8') as json_file:
    word_freq = dict(json.load(json_file))
wc = wordcloud.WordCloud(
    font_path='01-第1周/coding/PingFangSC-Medium.ttf', 
    width=3840, height=2160, 
    background_color='white')
wc.generate_from_frequencies(word_freq)
wc.to_file('01-第1周/coding/wordcloud.png')
