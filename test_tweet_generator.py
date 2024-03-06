from tweet_generator import generate_tweet

topics=["Technology", "LLMs", "Sam Altman"]
hastags=["innovation", "askSam"]
tone="surprising"
length_characters=240
style="news"

print(generate_tweet(topics,hastags,tone,length_characters,style))

