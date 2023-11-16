from textblob import TextBlob

text_1 = "The movie was so awesome."
text_2 = "The food here tastes terrible."
text_3 = "i really love to killing time"

#Determining the Polarity 
p_1 = TextBlob(text_1).sentiment.polarity
p_2 = TextBlob(text_2).sentiment.polarity
p_3 = TextBlob(text_3).sentiment.polarity

#Determining the Subjectivity
s_1 = TextBlob(text_1).sentiment.subjectivity
s_2 = TextBlob(text_2).sentiment.subjectivity
s_3 = TextBlob(text_3).sentiment.subjectivity

print("Polarity of Text 1 is", p_1)
print("Polarity of Text 2 is", p_2)
print("Polarity of Text 3 is", p_3)
print("Subjectivity of Text 1 is", s_1)
print("Subjectivity of Text 2 is", s_2)
print("Subjectivity of Text 3 is", s_3)