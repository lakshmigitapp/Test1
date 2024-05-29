import re

data='''
Singanalluru Puttaswamaiah Muthuraj (24 April 1929 – 12 April 2006),[4] better known by his stage name Dr. Rajkumar,[a] was an Indian actor and singer who worked in Kannada cinema. Regarded as one of the greatest actors in the history of Indian cinema[6][7] and a versatile actor,[8][9] he is considered a cultural icon and holds a matinée idol status in the Kannada diaspora,[10][11] among whom he is popularly called as Nata Saarvabhouma (Emperor of Actors), Bangarada Manushya (Man of Gold), Vara Nata (Gifted actor), Gaana Gandharva (Celestial singer), Rasikara Raja (King of connoisseurs), Kannada Kanteerava and Rajanna/Annavru (Elder brother, Raj). He was honoured with Padma Bhushan in 1983 and Dadasaheb Phalke Award in 1995.[12] He is the only lead actor to win National Award for singing.[13] His 35 movies have been remade 58 times in 9 languages by 34 actors making him the first actor whose movies were remade more than fifty times [14] and the first actor whose movies were remade in nine languages.[15] He was the first actor in India to enact a role which was based on James Bond in a full-fledged manner.[16] The success of his movie Jedara Bale is credited to have widely inspired a Desi bond genre in other Indian film industries.[17] On the occasion of the "Centenary of Indian Cinema" in April 2013, Forbes included his performance in Bangaarada Manushya on its list of "25 Greatest Acting Performances of Indian Cinema".[18] Upon his death, The New York Times had described him as one of India's most popular movie stars.[19]

Rajkumar entered the film industry after his long stint as a dramatist with Gubbi Veeranna's Gubbi Drama Company, which he joined at the age of eight before he got his first break as a lead in the 1954 film Bedara Kannappa. He went on to work in over 205 films essaying a variety of roles and excelling in portraying mythological and historical characters in films such as Bhakta Kanakadasa (1960), Ranadheera Kanteerava (1960), Satya Harishchandra (1965), Immadi Pulikeshi (1967), Sri Krishnadevaraya (1970), Bhakta Kumbara (1974), Mayura (1975), Babruvahana (1977) and Bhakta Prahlada (1983).[20] 13 of his films have received National Film Award for Best Feature Film in Kannada (Rajat Kamal) within a span of 15 years from 1954 to 1968. 17 of his films have received Karnataka State Film Awards in five different categories.

Trained in classical music during his theatre days, Rajkumar also became an accomplished playback singer. He mostly sang for his films since 1974. The songs Yaare Koogadali, Huttidare Kannada, Hey Dinakara, Hrudaya Samudra, Manikyaveena and Naadamaya became widely popular. For his rendition of the latter song, he was awarded the National Film Award for Best Male Playback Singer.

He is the only Indian actor to be awarded the Kentucky Colonel, the highest honour bestowed by the Commonwealth of Kentucky in the United States.[21][22] Well known for his highly disciplined and simple lifestyle in both personal and professional fronts, Rajkumar was also an avid Yoga, Pranayama, and Carnatic music performer. In 2000, he was kidnapped from his farmhouse at Gajanur by Veerappan and was released after 108 days.[23] He died of cardiac arrest at his residence in Bangalore on 12 April 2006 at the age of 76.[24] His eyes were donated as per his last wish.[25]
'''

data1='ac abc abbc abbbc  abbbbc abbbbbc abbbbbbc'
pattern='abbbbbb$'

result=re.findall(pattern,data1)
print(result)