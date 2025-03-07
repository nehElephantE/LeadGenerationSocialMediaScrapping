
# !pip install vaderSentiment
from re import A
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from textblob import TextBlob

obj = SentimentIntensityAnalyzer()
sentence = "Is this even gold plated ?It so horrible "
sentiment_dict = obj.polarity_scores(sentence)
print(sentiment_dict)

from textblob import TextBlob
import pandas as pd


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



dict1 ={1:"I was unhappy with the phone I received from ICICI store as it was broken. However, their prompt assistance in resolving my problem won my heart.. The product was changed in 3-4 days.. Thanks for all your help.." , 
        2:"Please LIC requested that please stop calling my family for emi BajajFinance team continue calling  again and again and also abuse and misbehaving with my family.plz does not make my problem more.i pay all emi after coming from nepal.plz give me time" ,
        3: "I had a very bad experience with ICICI LOMBARD so am not interested to continue my car policy with them. When I bought my car and got this policy. When I went with claim for minor accident, they have been saying only these things will be covered and some is not included." ,
        4:"Every time, i used to visit HDFC showroom to renew my car insurance policy. I'm receiving the no claim bonus. This is a bumper to bumper covered policy. I pay the premium amount of Rs. 10000 and I'm not sure about the IDV value. They are providing the hard copy of the documents immediately. I do not have any claim experience" , 
        5:"The policy was overall good but end of the day i was not satisfied with the policy by Max Life Insurance . When i purchase the policy, they said its a zero depreciation policy and its nil dept. But when i applied the claim, they have given me a claim only for 50%. In that, my car steering was not covered, Some engine parts and bumper was not covered." , 
        6:"Since my friend is working in United India hence i have chosen the car insurance policy from them. Since the car is 5 years old, they won't provide the zero depreciation policy and its a third party policy. I have paid the premium amount of Rs. 1800 and the premium is very less and the coverage amount is less than lakhs. I have got my no claim bonus and i don't have any claim experience with them. They have sent the hard copy of the documents to the customer's address without any request.",
        7: "When i purchase my new car, the dealer has suggested me to take the car insurance policy from HDFC Ergo. Its not zero depreciation policy which covers only for 60% and i never had any claim experience. I do not remember about the premium amount and the dealer has taken care of all the formalities.",
        8:"The two wheeler insurance has been using with the LIC INSURANCE where i had no claim experience with this policy also the policy has the coverage for full along with that there is a no claim bonus in this insurance policy.",
        9:"I had a car insurance with Kotak, after claiming for Maruti car said they can't provide bumper to bumper so had a problem on the renewal for my father car so we had changed to HDFC Ergo for both the cars. Its a one year policy. The premium was better when compared to others, the benefits are same . I have received the insurance paper on time. Claim was fairly good",
        10:"I had taken this insurance policy a pretty long time back and i had been paying the premium amount of 13,000 annually. The insurance covers bumper to bumper and there has not been any claims made so far and there has not been any hassle faced with the services of them.",
        11:"My wife had company insurance of Tata, its worth less policy, they deduct amt with no reason and no body responds to us. Please dont buy this worst health insurance. I am spoken to company to cancel this insurance tie-up. Its a corporate plan we are paying 900rs per month.u dont deserve a single star too.",
        12:"I took My Home Policy after referred by my Banker.They'll claim mountains like any Salesperson will do. I knew how this work but I thought they'll do partial reclaim atleast.I paid 11000 as premium for 6 portal electronic equipments for years. In the document it says'Contents' insured for 5 lakhs & exclude objects greated than 5 years old. Sales person also suggested it'll include objects that are not 5 years old. When I claimed broken iPad they came up with new rules(out of nowhere) that it's 5 years already & it'll not be covered. they've also added new rue that Mobile phone more than 3 years are not covered. Why'd we need additional insurance for brand new items.Their Customer service keeps talking like a broken record. Completely unethical. Better not to take any insurance product(other than term 7 health) & rather take a chance.Hope this helps atleast 1 person who wants to take Insurance"}



list_comp=["HDFC Life Insurance Company",
"Max Life Insurance Company"
"Life Insurance Corporation of India"
"Tata AIA Life Insurance Company","Max Life Insurance","ICICI Life insurance","ICICI Prudential Life Insurance"]

list_comp_unf=["HDFC" , "Max Life" , "LIC" , "Tata" , "ICICI" , " @SBILife" , "@LICIndiaForever " , "@ExideLife " , "@HDFCLIFE" , " @Kotak_Li"]
final_list_positive=[]
final_list_negative=[]
print()
print("Hackrx 3.0")
print()

data = [
  {
    "author_id": "1525702200445399040",
    "id": "1540759925860798466",
    "text": "RT @rose_k01: Balasaheb Thackeray was the one who supported Narendra Modi : \"Everyone was hammering about Gujarat Ri0ts &amp; no one cared abou…"
  },
  {
    "author_id": "972763368145784832",
    "id": "1540759920303169536",
    "text": "RT @vikasbha: Despite NCERT's refusal to Teesta Sheetalvad's NGO Sabrang, the Ministry of Education gave 1,17,45000 crores in 2010, even Af…"
  },
  {
    "author_id": "1345629070214758400",
    "id": "1540759918512177152",
    "text": "RT @MumbaichaDon: 2002 to 2022...20 Yrs long time. Finally PM Modi Ji walks out Scot Free from all PLOTS to Malign him by Antonia Maino &amp; H…"
  },
  {
    "author_id": "346406417",
    "id": "1540759918185443329",
    "text": "ગુજરાતના વર્ષ 2002 રમખાણ કેસમાં તત્કાલીન મુખ્યમંત્રી નરેન્દ્ર મોદી વિરુદ્ધ કાવતરું રચવામાં આવ્યું : સી.આર. પાટીલ\n\n#Gujarat #Narendramodi #Gujarat2002riots #CRPaatil \n\nhttps://t.co/OOgq8YTZ6F"
  },
  {
    "author_id": "2340082358",
    "id": "1540759916381581313",
    "text": "RT @AgentVinod03: Gujarat Police has also arrested #RBSreekumar from Gandhinagar under the same FIR. He is a retired IPS, who had filed 9 f…"
  },
  {
    "author_id": "1510701026734579714",
    "id": "1540759914984837121",
    "text": "RT @AgentVinod03: Gujarat Police has also arrested #RBSreekumar from Gandhinagar under the same FIR. He is a retired IPS, who had filed 9 f…"
  },
  {
    "author_id": "1410916007779078147",
    "id": "1540759914930249728",
    "text": "RT @Iyervval: That Teesta &amp; Rana ran a false and libellous campaign against Modi is undeniable. But you can’t use state institutions to go…"
  },
  {
    "author_id": "1140921578441412609",
    "id": "1540759912657162240",
    "text": "RT @rose_k01: Teesta Setalvad Arrested.\nNext should be Rana Ayyub for lies she spread against Modi in her book \"The Gujarat Files\". Listen…"
  },
  {
    "author_id": "274913597",
    "id": "1540759911717830657",
    "text": "RT @fgautier26: Dear Friends, Here is all the EVIDENCE AGAINST TEESTA SETALVAD and her unpardonable crimes against Mother India &amp; Mr. Modi.…"
  },
  {
    "author_id": "228439153",
    "id": "1540759910417240066",
    "text": "RT @ManMundra: @sardesairajdeep who are u to judge Modi and pass verdicts? Paid Idiot!"
  },
  {
    "author_id": "111337200",
    "id": "1540759908911837184",
    "text": "RT @VP_Sanu: On 2002 Gujarat pogrom;\n\nConspirators:\n1)Teesta Setalvad\n2) RB Sreekumar (retired DGP)\n3) Sanjiv Bhatt (former IPS officer)\n\nI…"
  },
  {
    "author_id": "135582332",
    "id": "1540759908416897024",
    "text": "RT @amarprasadreddy: Modi Kabaddi League in 234 Constituencies!\n\nWith 1200 teams and 13000 players. \n\nThalaivar @annamalai_k Avl will annou…"
  },
  {
    "author_id": "1521906334387478528",
    "id": "1540759906059292672",
    "text": "RT @HeroOfTheSU: Supreme Court upheld that Modi had nothing to do with Anti-muslim riots in 2002.\n\nThis came as a big blow to Modi voters w…"
  },
  {
    "author_id": "2856315884",
    "id": "1540759905870938112",
    "text": "RT @indiantweeter: Meet RB Sreekumar \n\nFirst framed ex ISRO engineer and Padma award winner Nambi Narayan in false case \n\nThen gave stateme…"
  },
  {
    "author_id": "1692986629",
    "id": "1540759905849593857",
    "text": "RT @rose_k01: Balasaheb Thackeray was the one who supported Narendra Modi : \"Everyone was hammering about Gujarat Ri0ts &amp; no one cared abou…"
  },
  {
    "author_id": "189219395",
    "id": "1540759902951309312",
    "text": "RT @rose_k01: PM Modi giving Rajdeep Sardesai verbal bаshing &amp; taking his class on surviving in his career for years by writing falsehoods…"
  },
  {
    "author_id": "3601491732",
    "id": "1540759896244727810",
    "text": "RT @OpIndia_in: गर्भवती का भ्रूण आग में फेंकने से लेकर चूल्हे से गोधरा ट्रेन में आग तक: गुजरात दंगों पर वो 5 झूठ, जो नरेंद्र मोदी और हिन्दु…"
  },
  {
    "author_id": "850031984713715712",
    "id": "1540759892604391425",
    "text": "RT @ARanganathan72: It took twenty years for Modi to finally clear his name, and in those twenty years, tens of thousands of people - from…"
  },
  {
    "author_id": "414131040",
    "id": "1540759892411179008",
    "text": "RT @RuazaINC: Plight of Assam and Power games by Modi-Shah\nDon't forget while casting your vote"
  },
  {
    "author_id": "1396897763338506243",
    "id": "1540759892251639809",
    "text": "RT @vikasbha: Despite NCERT's refusal to Teesta Sheetalvad's NGO Sabrang, the Ministry of Education gave 1,17,45000 crores in 2010, even Af…"
  },
  {
    "author_id": "1131211759",
    "id": "1540759889882267648",
    "text": "RT @epanchjanya: पढ़िए @arungodda की रिपोर्ट\n\nhttps://t.co/0ywTSlVZhf"
  },
  {
    "author_id": "392576149",
    "id": "1540759885666693125",
    "text": "RT @eOrganiser: Gujarat ATS has arrested #RBSreekumar former DGP of Gujarat and #AAP leader.\nRB Sreekumar is the person who framed ex-ISRO…"
  },
  {
    "author_id": "1416022169172078600",
    "id": "1540759884270034945",
    "text": "RT @NewsArenaIndia: Amit Shah : There were no protests by BJP when Narendra Modi was investigated by SIT or when I was arrested."
  },
  {
    "author_id": "1483864470023962625",
    "id": "1540759881287798784",
    "text": "RT @singh_vvikram: #Justice_For_Technician RRB  CEN 01/2018  plz Clear Technicians Waiting list as Like ALPPost. Humse kya Galti hui.Hum bh…"
  },
  {
    "author_id": "1248130038915944452",
    "id": "1540759880276901888",
    "text": "Book Launch event of MODI@20 (Dreams meet Delivery) with our HCM Shri @himantabiswa sir at Srimanta Sankardev Kalakhetra.  🙏🏻\n\n@PhanindranathS3\n@SidhankuBJYM\n@BJYMAssamPrdsh\n@Nihar_Sarma\n@Bjym4guwahati https://t.co/cd0b8XevSL"
  },
  {
    "author_id": "1389840288",
    "id": "1540759878725435393",
    "text": "RT @svaradarajan: Gujarat Police Arrest Teesta Setalvad, Activist Who Pursued 2002 Riots Case Against Modi \n\nhttps://t.co/jfsxEvvI3a via @t…"
  },
  {
    "author_id": "1446463268101316621",
    "id": "1540759875558334467",
    "text": "RT @SatishKapur4: Supreme Court has set a wrong precedence by giving clean chit to Modi for Gujarat riots,the court even praised SIT that e…"
  },
  {
    "author_id": "1520781178088968192",
    "id": "1540759871863197697",
    "text": "RT @thehawkeyex: Life turns here. As soon as PM Modi assumed office, MHA cracked down on all foreign-funded NGOs &amp; subsequently more than 1…"
  },
  {
    "author_id": "3253387567",
    "id": "1540759869673787398",
    "text": "RT @indiantweeter: Teesta seetalwad ki arrest personal victory lag rahi hogi har Modi supporter ko jo 2014 se pehle se Iss aurat ke karanam…"
  },
  {
    "author_id": "1435133950867820546",
    "id": "1540759861675233281",
    "text": "RT @VarunKrRana: Now even activists don't have freedom of doing scams in Modi's India. \n\n- Rana Ayyub"
  },
  {
    "author_id": "1259410812231352320",
    "id": "1540759860643389443",
    "text": "RT @OpIndia_in: उधर कट्टर मुस्लिम भीड़ ने 59 हिन्दुओं को ज़िंदा जलाया, इधर नैरेटिव सेट करने में लगा मीडिया: अंदर के लोगों से ही जानिए 2002…"
  },
  {
    "author_id": "840526565435822080",
    "id": "1540759855136354304",
    "text": "RT @n_i_g_a_m: Rana Ayyub’s career exists due to Modi and they say Modi hasn’t created any jobs."
  },
  {
    "author_id": "160068029",
    "id": "1540759854255448064",
    "text": "@geetv79 https://t.co/mgWr7YFQza"
  },
  {
    "author_id": "1030063754661298183",
    "id": "1540759851973808129",
    "text": "RT @eOrganiser: Gujarat ATS has arrested #RBSreekumar former DGP of Gujarat and #AAP leader.\nRB Sreekumar is the person who framed ex-ISRO…"
  },
  {
    "author_id": "1540752285101223942",
    "id": "1540759851868966915",
    "text": "RT @indiacom: Postpone NEET UG 2022: Students continue their demand on Twitter, urge authorities to pay attention to their request. \n#Dharm…"
  },
  {
    "author_id": "107548394",
    "id": "1540759851223187457",
    "text": "RT @AIIndia: Setalvad’s detention comes a day after the Supreme Court dismissed a petition filed by her along with Zakia Jafri, whose husba…"
  },
  {
    "author_id": "1498166017406963714",
    "id": "1540759845422641153",
    "text": "@SpiritOfCongres Well she was best for that time now time demands for modi and he is best for now."
  },
  {
    "author_id": "2320078059",
    "id": "1540759844407451649",
    "text": "Next day Narendrmodi came to patiya and \"instigated Hindus\" and left,\nThat's why he came. Wherever riots were there he came to \"instigate Hindus\" and Modi said \"you did well. Keep doing\n\n(Babu Bajrangi on camera regarding 2002 Gujarat Riot) https://t.co/16guuFfy0B https://t.co/lhxSz6nvMX"
  },
  {
    "author_id": "58410046",
    "id": "1540759839701213184",
    "text": "RT @vikasbha: Despite NCERT's refusal to Teesta Sheetalvad's NGO Sabrang, the Ministry of Education gave 1,17,45000 crores in 2010, even Af…"
  },
  {
    "author_id": "3107325469",
    "id": "1540759839692955649",
    "text": "RT @lonelyredcurl: Teesta Setalvad in 2017 talking about how Modi's ascent to power relied on a corporate-backed campaign of lies designed…"
  },
  {
    "author_id": "1538914112025284609",
    "id": "1540759836375146496",
    "text": "RT @Harikes09057434: @Manoj13Dol1 @modi_yogi_ #संजय_राऊत_भड़वा_है \n#संजय_राऊत_भड़वा_है"
  },
  {
    "author_id": "1404664522913189890",
    "id": "1540759836282957824",
    "text": "RT @MJ_007Club: Who's Teesta Setalvad? She's a fraud activist who:\n\n- Tutored 22 people to become witness who actually didn't even witness…"
  },
  {
    "author_id": "1479158263094525953",
    "id": "1540759834106241025",
    "text": "RT @rkhuria2: #GujaratRiots2002 \n\nSpecial Court investigating Gujarat Riots accepted Babu Bajrangi’s recorded  confession as an evidence an…"
  },
  {
    "author_id": "1262003633861718016",
    "id": "1540759827357413377",
    "text": "RT @yoursurajnaik: Mr @AmitShah ji we Congress are not afraid of ED.. Infact you and Modi are Scared of our leader @RahulGandhi ji.. \nCongr…"
  },
  {
    "author_id": "1388038114044571652",
    "id": "1540759826699112449",
    "text": "RT @rose_k01: PM Modi giving Rajdeep Sardesai verbal bаshing &amp; taking his class on surviving in his career for years by writing falsehoods…"
  },
  {
    "author_id": "1017704211004510208",
    "id": "1540759823738105856",
    "text": "RT @fgautier26: Dear Friends, Here is all the EVIDENCE AGAINST TEESTA SETALVAD and her unpardonable crimes against Mother India &amp; Mr. Modi.…"
  },
  {
    "author_id": "4927949116",
    "id": "1540759809867128832",
    "text": "RT @AIIndia: Setalvad’s detention comes a day after the Supreme Court dismissed a petition filed by her along with Zakia Jafri, whose husba…"
  },
  {
    "author_id": "2860513068",
    "id": "1540759796084641793",
    "text": "RT @kharge: Largest Bank Frauds under Modi Govt\n- Vijay Mallya: 9,000 Cr\n- Nirav &amp; Choksi: 14,000 Cr\n- ABG Shipyard: 23,000 Cr\n- DHFL: 35,0…"
  },
  {
    "author_id": "1431091610125623296",
    "id": "1540759794570915841",
    "text": "@Manoj13Dol1 @modi_yogi_ #संजय_राऊत_भड़वा_है \n#संजय_राऊत_भड़वा_है"
  },
  {
    "author_id": "116217586",
    "id": "1540759794046230531",
    "text": "@anjanaomkashyap Last line video ki sab se best \"Modi ka badlapur\" 😂😂😂😂😂😂😂😂 https://t.co/47JoyfbBLv"
  }
]


def getSentiments(dataList):
    answers = []
    for data in dataList:
        analysis=TextBlob(data['text'])
        obj = SentimentIntensityAnalyzer()
        sentiment_dict = obj.polarity_scores(data['text'])
        if sentiment_dict['compound'] > 0.3:
            sentiment_dict['sentiment'] = "possitive"
        elif sentiment_dict['compound'] < 0.3:
            sentiment_dict['sentiment'] = "negative"
        else:
            sentiment_dict['sentiment'] = "neutral"
        answers.append(sentiment_dict)
    #     if(sentiment_dict['pos']>sentiment_dict['neg']):
    #         if((sentiment_dict['neu']<0.877) ):
    #           print()
    #           print(dict1[j])
    #           print(j)
    #           final_list_positive.append(j)
    #           print("Positive")
    #           print(sentiment_dict)
    #         else:
    #           print()
    #           print(dict1[j])
    #           print(j)
    #           print("Neutral")
    #           print(sentiment_dict)
    #     elif(sentiment_dict['neg']>sentiment_dict['pos']):
    #         if((sentiment_dict['neu']<0.877) ):
    #           print()
    #           print(dict1[j])
    #           print(j)
    #           for x in list_comp_unf:
    #             result=dict1[j].find(x)
    #             if(result>-1):
    #               final_list_negative.append(j)
    #               break
    #           print("Negative")
    #           print(sentiment_dict)
    #         else:
    #           print()
    #           print(dict1[j])
    #           print("Neutral")
    #           print(sentiment_dict)
    # print("Final list")
    # print(final_list_positive)
    # print(final_list_negative)

    # df_pos = pdDataFrame({'links' : final_list_positive})
    # df_neg = pd.DataFrame({'links' : final_list_negative})
    # print(df_pos)

    # print(df_neg).

    # df_pos.to_csv('final_list_pos.csv', encoding = 'utf-8-sig') 
    # #files.download('final_list_pos.csv')

    # df_neg.to_csv('final_list_neg.csv', encoding = 'utf-8-sig') 
    # # files.download('final_list_neg.csv')

    # df_pos.to_csv('/drive/My Drive/HACKRX/final_list_pos.csv')

    # df_neg.to_csv('/drive/My Drive/HACKRX/final_list_neg.csv')
    return answers
print(getSentiments(data))