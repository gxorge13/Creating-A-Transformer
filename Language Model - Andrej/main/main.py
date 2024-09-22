import urllib.request as ur

url = r"https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
path = r"C:\Users\georg\OneDrive\Desktop\Projects\Language Model - Andrej\Creating-A-Transformer\Language Model - Andrej\\input"

ur.urlretrieve(url, path)

#getting the dataset