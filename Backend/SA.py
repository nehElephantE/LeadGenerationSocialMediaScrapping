!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
[12:31 PM, 6/25/2022] Yash: from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
[12:33 PM, 6/25/2022] Yash: from textblob import TextBlob
list1=["I was unhappy with the phone I received from Bajaj Finserv EMI store as it was broken. However, their prompt assistance in resolving my problem won my heart.. The product was changed in 3-4 days.. Thanks for all your help.." , "Please @Bajaj_Financeit requested that please stop calling my family for emi BajajFinance team continue calling  again and again and also abuse and misbehaving with my family.plz does not make my problem more.i pay all emi after coming from nepal.plz give me time" , 
       "I had a very bad experience with ICICI LOMBARD so am not interested to continue my car policy with them. When I bought my car and got this policy. When I went with claim for minor accident, they have been saying only these things will be covered and some is not included." 
       ,"Every time, i used to visit their showroom to renew my car insurance policy. I'm receiving the no claim bonus. This is a bumper to bumper covered policy. I pay the premium amount of Rs. 10000 and I'm not sure about the IDV value. They are providing the hard copy of the documents immediately. I do not have any claim experience" , 
       "The policy was overall good but end of the day i was not satisfied with the policy. When i purchase the policy, they said its a zero depreciation policy and its nil dept. But when i applied the claim, they have given me a claim only for 50%. In that, my car steering was not covered, Some engine parts and bumper was not covered." , 
       "Since my friend is working in United India hence i have chosen the car insurance policy from them. Since the car is 5 years old, they won't provide the zero depreciation policy and its a third party policy. I have paid the premium amount of Rs. 1800 and the premium is very less and the coverage amount is less than lakhs. I have got my no claim bonus and i don't have any claim experience with them. They have sent the hard copy of the documents to the customer's address without any request.",
       "When i purchase my new car, the dealer has suggested me to take the car insurance policy from HDFC Ergo. Its not zero depreciation policy which covers only for 60% and i never had any claim experience. I do not remember about the premium amount and the dealer has taken care of all the formalities.",
       "The two wheeler insurance has been using with the ICICI LOMBARD GENERAL INSURANCE where i had no claim experience with this policy also the policy has the coverage for full along with that there is a no claim bonus in this insurance policy.",
       "I had a car insurance with Kotak, after claiming for Maruti car said they can't provide bumper to bumper so had a problem on the renewal for my father car so we had changed to HDFC Ergo for both the cars. Its a one year policy. The premium was better when compared to others, the benefits are same . I have received the insurance paper on time. Claim was fairly good",
       "I had taken this insurance policy a pretty long time back and i had been paying the premium amount of 13,000 annually. The insurance covers bumper to bumper and there has not been any claims made so far and there has not been any hassle faced with the services of them.",
       "My wife had company insurance of Bajaj alliance, its worth less policy, they deduct amt with no reason and no body responds to us. Please dont buy this worst health insurance. I am spoken to company to cancel this insurance tie-up. Its a corporate plan we are paying 900rs per month.u dont deserve a single star too.",
       "I took My Home Policy after referred by my Banker.They'll claim mountains like any Salesperson will do. I knew how this work but I thought they'll do partial reclaim atleast.I paid 11000 as premium for 6 portal electronic equipments for years. In the document it says'Contents' insured for 5 lakhs & exclude objects greated than 5 years old. Sales person also suggested it'll include objects that are not 5 years old. When I claimed broken iPad they came up with new rules(out of nowhere) that it's 5 years already & it'll not be covered. they've also added new rue that Mobile phone more than 3 years are not covered. Why'd we need additional insurance for brand new items.Their Customer service keeps talking like a broken record. Completely unethical. Better not to take any insurance product(other than term 7 health) & rather take a chance.Hope this helps atleast 1 person who wants to take Insurance"]
print()
print("Hackrx")
print()
for i in list1:
    analysis=TextBlob(i)
    obj = SentimentIntensityAnalyzer()
    sentiment_dict = obj.polarity_scores(i)
    if(sentiment_dict['pos']>sentiment_dict['neg']):
      if((sentiment_dict['neu']<0.877) ):
        print()
        print(i)
        print("Positive")
        print(sentiment_dict)
      else:
        print()
        print(i)
        print("Neutral")
        print(sentiment_dict)
    elif(sentiment_dict['neg']>sentiment_dict['pos']):
      if((sentiment_dict['neu']<0.877) ):
        print()
        print(i)
        print("Negative")
        print(sentiment_dict)
      else:
        print()
        print(i)
        print("Neutral")
        print(sentiment_dict)