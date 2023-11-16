from profanity_check import predict, predict_prob

predict(['predict() takes an array and returns a 1 for each string if it is offensive, else 0.'])
# [0]

print(predict(['i really hate to love you']))
# [1]

predict_prob(['predict_prob() takes an array and returns the probability each string is offensive'])
# [0.08686173]

print(predict_prob([ "And that'll be 650. Can I get a name please? Sure, it's Patrick. Alright, it'll be right with you sir. Thanks, Idiots. I have a latte for Pratip. Pratip. My name is Aaron. I have a flat white for air in... Bo. Bo. Bo. Just Bo. I've got an Americano for just bro. Mark with a C. Carc? And your name is Carc? Chris with a K. Um... Chris? My name is Su. Mexico. Mexico! Is this for real? Yes, it's me. A booty time. Hey Derek. Have you reached your quota of misspelled names for your first week? Yes sir. I did it just like it told me. Nice. Welcome to Starbucks."]))
