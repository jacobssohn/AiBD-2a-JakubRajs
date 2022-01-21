from textblob import TextBlob
import random

def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    
    return word in text

twoByTwoDet = lambda squareM: squareM[0][0] * squareM[1][1] - squareM[1][0] * squareM[0][1]
def determinant(M):
    '''liczenie wyznacznika metodą Chia'''
    if len(M) == 2:
        return twoByTwoDet(M)

    changeOfSign = 1
    if M[0][0] == 0:
        for row in range(len(M)):
            replaced = False
            for col in range(len(M)):
                if M[row][col]:
                    for i in range(len(M)):
                        M[i][col], M[i][0] = M[i][0], M[i][col]
                        changeOfSign = -1
                    if not M[0][0]:
                        M[0], M[row] = M[row], M[0]
                        changeOfSign = 1
                    replaced = True
                    break
            if replaced:
                break

    res = []
    for row in range(1, len(M)):
        new_row = []
        for col in range(1, len(M)):
            elem = [[M[0][0], M[0][col]], [M[row][0], M[row][col]]]
            new_row.append(twoByTwoDet(elem))
        res.append(new_row)

    return changeOfSign * ( 1/ (M[0][0]) ** ( len(M) - 2 ) ) * determinant(res)
    

print(determinant([[random.randint(1, 100) for _ in range(5)] for _ in range(5)]))
