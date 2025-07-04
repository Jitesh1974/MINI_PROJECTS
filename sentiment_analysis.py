# TO CHECK WHETHER THE STATEMENT IS POSITIVE,NEGATIVE OR NEUTRAL //
from textblob import TextBlob

# Define a text
text = input("ENTER THE STATEMENT :")

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment = blob.sentiment
polarity = blob.sentiment.polarity

# Output the results
if (polarity > 0):
    print("THE STATEMENT IS POSITIVE ")
    
elif (polarity < 0 ):
    print("THE STATEMENT IS NEGATIVE")

else:print("THE STATEMENT IS NEUTRAL")











