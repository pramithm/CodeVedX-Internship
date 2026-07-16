from src.predict import predict_news

news = """
Kerry to go to Paris in gesture of sympathy

U.S. Secretary of State John F. Kerry said Monday that he will stop in Paris later this week, amid criticism that no top American officials attended Sunday's unity march against terrorism...

"""

prediction, confidence = predict_news(news)

print(prediction)
print(confidence)