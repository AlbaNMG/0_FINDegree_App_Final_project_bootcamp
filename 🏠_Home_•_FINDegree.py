import streamlit as st
import pandas as pd
import numpy as np

#Streamlit documentation: https://docs.streamlit.io/

#Configuring the Home Page: name and icon that appear in the tab on Internet when the app is open
st.set_page_config(
    page_title='FINDegree App!', 
    page_icon='🎯', 
    layout="centered", 
    initial_sidebar_state="auto")

#Configuring the Sidebar
st.sidebar.markdown("# Welcome to FINDegree App!")
#st.sidebar.markdown("ㅤㅤㅤㅤㅤㅤㅤ👋            ")
st.sidebar.text("🎯 FINDegree is the App that helps"+'\n'+ "ㅤㅤstudents who are about to start"+'\n'+"ㅤㅤㅤuniversity to identify which"+'\n'+"ㅤㅤuniversity degrees would be the"+'\n'+ "ㅤㅤㅤbest ones for them based on"+'\n'+"ㅤㅤㅤtheir personality type. 🎯")
st.sidebar.markdown("# Steps:")
st.sidebar.write("▶ Step １: Identify your Enneagram"+'\n'+"personality type (*)")
st.sidebar.write("▶ Step ２: See your top professions"+'\n'+"and check the best degrees for you")
st.sidebar.write("▶ Step ３: Visit our Degree Finder"+'\n'+"to get more info about universities,"+'\n'+"access score, etc.")
st.sidebar.write("(*) Click [here](https://lifegoalsmag.com/career-path-enneagram-type/) if you would like to know more about the Enneagram")

#Header and introduction of the Home Page
st.title("Find your perfect degree!")
st.text("⭐ Please, note that for now, this option is only available for Health Science"+'\n'+"degrees of public universities of Madrid. However, the Degree Finder 🔎 is"+'\n'+"available for all the categories (not only for Health Science).")
st.write("\n")
st.write("If you would like to access to the Degree Finder directly, please click [here!](http://localhost:8501/Degree_Finder)")
st.header("Step 1:")
st.subheader("Let's identify your Enneagram personality type! :sunglasses:")
st.subheader("")

#Excel with traits of personality (Based on the eneagram's approach, there are 9 personality types)
#This Excel contains words that describe each type of personality
pers_words=pd.read_excel(r'C:\Users\amohedasgonzalez\Downloads\0.Ironhack\Proyectos\Final project\personalities_words.xlsx')



###### FIRST PART -----------------> IDENTIFY USER'S PERSONALITY TYPE



#Creating variables to store the words that describe each type of personality separately
words_1=pers_words['Description_ENG'][pers_words['Type of personality']==1]
words_2=pers_words['Description_ENG'][pers_words['Type of personality']==2]
words_3=pers_words['Description_ENG'][pers_words['Type of personality']==3]
words_4=pers_words['Description_ENG'][pers_words['Type of personality']==4]
words_5=pers_words['Description_ENG'][pers_words['Type of personality']==5]
words_6=pers_words['Description_ENG'][pers_words['Type of personality']==6]
words_7=pers_words['Description_ENG'][pers_words['Type of personality']==7]
words_8=pers_words['Description_ENG'][pers_words['Type of personality']==8]
words_9=pers_words['Description_ENG'][pers_words['Type of personality']==9]

#Users have to choose the 9 best words that describe themselves ("9" - odd number to avoid a tie between different personalities)
#First, we have to create the drop-down list of words (traits of personalities)
list_of_words=[]
all_words=[words_1,words_2,words_3,words_4,words_5,words_6,words_7,words_8,words_9]

#inserting in the empty list all the words that describe the 9 personalities together
for i in all_words:
    
    result=i.iloc[0].split(",")
    list_of_words.append(result)

final_list_of_words=set([element for sublist in list_of_words for element in sublist])

#creating a dataframe to order the words alpabethically
df_words=pd.DataFrame(final_list_of_words)
df_words.columns=["Words"]
df_words_ordered=df_words.sort_values("Words") #odering the list alphabetically

#creating the final drop-down list with all of the words
user_words=st.multiselect('Please, select the 9 words that best describe you: ',df_words_ordered)

#############Let's identify the user's personality

#Creating the empty counters for each personlaity type and a dictionary 
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
count_7=0
count_8=0
count_9=0

dict_count={'key_count_1':0,'key_count_2':0,'key_count_3':0,'key_count_4':0,'key_count_5':0,'key_count_6':0,'key_count_7':0,'key_count_8':0,'key_count_9':0}

#based on the selection of the user ("user_words"):
for i in user_words:
    if i in words_1.iloc[0]:
        count_1=count_1+1
        dict_count['key_count_1']=count_1
    elif i in words_2.iloc[0]:
        count_2=count_2+1
        dict_count['key_count_2']=count_2
    elif i in words_3.iloc[0]:
        count_3=count_3+1
        dict_count['key_count_3']=count_3
    elif i in words_4.iloc[0]:
        count_4=count_4+1
        dict_count['key_count_4']=count_4
    elif i in words_5.iloc[0]:
        count_5=count_5+1
        dict_count['key_count_5']=count_5
    elif i in words_6.iloc[0]:
        count_6=count_6+1
        dict_count['key_count_6']=count_6
    elif i in words_7.iloc[0]:
        count_7=count_7+1
        dict_count['key_count_7']=count_7
    elif i in words_8.iloc[0]:
        count_8=count_8+1
        dict_count['key_count_8']=count_8
    elif i in words_9.iloc[0]:
        count_9=count_9+1
        dict_count['key_count_9']=count_9
    else:
        print('the word'+i+"is not among the available ones")

import operator
#if the button is pressed:

if st.button("Press me to see what is your personality type and which are the best degrees for you!"):

    if bool(user_words)==False: #if the list that corresponds to the "user_words" is empty, it means that the user has not selected any words
        "Please, select the words that best describe you above"

    elif len(user_words) != 9: #if the user has selected less than 9 words:
        "Please, check that you have chosen exactly 9 words above"

    else: #this means that the user has already selected 9 words so:
        max_key = max(dict_count.items(), key=operator.itemgetter(1))[0] #I saw this code on Internet -> to get the key of the maximum value in the dictionary to identify the user's personality (the output will be the type of personality with the most number of selected words
        str_max_key=str(max_key[-1]) #converting max_key to string and obtaining the last number of the key which is the type of personality of the user

        #Personality types' descriptions source: https://www.success.com/the-enneagram-at-work/
        #Defining the output that will be shown in the app based on the final personality type of the user

        if str_max_key=="1":
            final_str_max_key="Type 1 - The Reformer"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Being ethical and right')
            st.write('**Fears**: Being wrong')
            st.write('On the surface, Type Ones are the employees with neat and tidy offices, but Ones are not just limited to perfection in their surroundings. These detail-oriented workers thrive with to-do lists and love routine, and their tolerance for tedious work makes them the office go-to for difficult tasks. Since they can always be counted on, they have very little patience with team members who don’t follow through, and their black and white thinking makes them prone to resentment and slow to offer forgiveness. Ones cannot stand it when someone breaks or bends the rules and, if they do so themselves, will struggle strongly with self-criticism. Ones can seem demanding, but only because they expect of their co-workers what they expect of themselves: commitment to constant personal and corporate improvement.')
        
        elif str_max_key=="2":
            final_str_max_key="Type 2 - The Helper"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Being needed')
            st.write('**Fears**: Rejection')
            st.write('Twos are sometimes referred to as the office “mom” or “dad” because of their warm dispositions and tendency to know what’s going on in everyone’s personal lives. They are the co-workers who ask to see vacation photos, have intel on whose marriage is on the rocks, and bring baked goods to share. Like a good parent, they intuit their co-workers’ needs well and find themselves the sounding board for co-workers who need to vent or ask for help. This makes Twos caring leaders and excellent customer service reps, but can also hinder efficiency. Twos love open office settings and group work, but they’ll work much faster without the distraction of a budding office friendship.')
        
        elif str_max_key=="3":
            final_str_max_key="Type 3 - The Achiever"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Appearing successful')
            st.write('**Fears**: Being exposed as a failure')
            st.write('Threes are the teammate everyone wants for the annual company volleyball tournament—not necessarily because of their athleticism, but because they’re always out to win. This winning drive comes in handy in performance-based positions like sales, but also in schmoozing clients, as Threes can turn on the charm and make friends with just about anyone. Their first impressions are hard to beat and, in an interview, Threes have a way of making past failures look like success. Threes are a momentum-building asset to any team, but they also have a tendency to cut corners and run over co-workers in the name of results, so accountability is key.')
        
        elif str_max_key=="4":
            final_str_max_key="Type 4 - The Individualist"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Expressing uniqueness')
            st.write('**Fears**: Being ordinary')
            st.write('Fours are the big idea people, thanks to their creative or artistic streak. They’re often misunderstood as eccentric or dramatic, but their unconventional approach to life is what makes them so effective. Authenticity is paramount to them, and because of this they can’t help but call out half-truths and serve as the office “BS monitor.” Fours are very comfortable with sadness—their office Spotify list is likely flush with ballads—and so melancholy and moody behavior comes with the territory. They’re not like the rest of their co-workers, which, to them, is a relief.')
        
        elif str_max_key=="5":
            final_str_max_key="Type 5 - The Investigator"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Knowledge and competence')
            st.write('**Fears**: Being thought of as ignorant')
            st.write('Fives are the co-worker who says nothing during an hour-long meeting and then sends an email with follow-up thoughts a day or two later. Because they long to be informed, Fives don’t speak up until they have a chance to process information, preferring instead to listen rather than jump right in. Gathering information is their passion and it makes them an invaluable resource for companies who need an in-house expert. An open office setting would rapidly exhaust their limited energy, but Fives don’t need much more than a quiet space and the autonomy to learn at their own pace. They don’t crave the corner office; they crave independence.')
        
        elif str_max_key=="6":
            final_str_max_key="Type 6 - The Loyalist"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Security and support')
            st.write('**Fears**: Chaos, blame and fear itself')
            st.write('Sixes are the most loyal employees of all the Enneagram types, sometimes putting up with a difficult boss or lackluster salary for longer than they should. When it comes to meetings, they show up prepared. Their often witty and trustworthy demeanor makes them well-liked by the whole staff, but their self-doubt and “what if” questions can slow down a company’s forward motion. Sixes possess an uncanny ability to spot the potential worst-case scenarios in a business deal and good leaders will be patient enough to harness this superpower, rather than be annoyed by their seemingly negative outlook.')
        
        elif str_max_key=="7":
            final_str_max_key="Type 7 - The Enthusiast"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Happiness')
            st.write('**Fears**: Boredom, feeling trapped')
            st.write('Sevens light up a room. Ever in the pursuit of fun, they’re the co-worker who uses up every drop of their vacation days, invites the office staff over for a themed party, and impulsively buys a round for the table at happy hour. Sevens possess a popularity and enthusiasm that can speed up group projects and boost morale, but if left in charge, can sometimes send the group bouncing from task to task, leaving each one unfinished, in the name of FOMO.')
        
        elif str_max_key=="8":
            final_str_max_key="Type 8 - The Challenger"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Protecting themselves')
            st.write('**Fears**: Being controlled')
            st.write('Eights run meetings even when they’re not in charge. Although their propensity to take over can seem condescending, their motivation is often founded in a selfless desire to help protect the mission or the co-workers at stake. Their natural ability to make fast-paced decisions paired with their thick-skinned personality makes them almost immune from worrying about what others think of their choices. Since conflict isn’t scary to them, they easily sniff out others’ weaknesses and can be powerful negotiators. To earn their respect, you’ll need to stand your ground and be willing to go toe-to-toe.')
        
        else:
            final_str_max_key="Type 9 - The Peacemaker"
            "Your personality type is: "+final_str_max_key
            st.subheader("Your personality type at work...")
            st.write('**Motivated by**: Stability and peace of mind')
            st.write('**Fears**: Conflict')
            st.write('Keeping the peace for a Nine is about preventing disconnection from others. Since they strive to go along with what others think or feel in order to not rock the boat, nines can be easy to get along with and assimilate well into a variety of office cultures. Leading a Nine means creating a safe space for their opinions, developing predictable routines, and providing margin for them to escape their duties after they clock out. Nines have the ability to see all sides of an issue, which makes them diplomatic mediators for divisive teams. Although they want no part in office politics, a lack of expression can manifest into passive aggression when left unchecked, so kindly demanding their honest feedback from time to time is necessary.')

        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------


        ###### SECOND PART -----------------> WORD SIMILARITY BETWEEN traits of personality & skills of professions TO RECOMMEND THE BEST Degrees

        import gensim
        import gensim.downloader as api
        from sklearn.metrics.pairwise import cosine_similarity
        from gensim.models import Word2Vec
        import pickle

        #reading the model that I created in Jupyter Notebook previously 
        model=pd.read_pickle(r'C:\Users\amohedasgonzalez\Downloads\0.Ironhack\Proyectos\Final project\model.p')
        
        #Reading the Excel file that I need with the words of personalities
        pers_words=pd.read_excel(r"C:\Users\amohedasgonzalez\Downloads\0.Ironhack\Proyectos\Final project\personalities_words.xlsx")
        
        #"gensim.utils.simple_preprocess" is a gensim's function that tokenize words
        #Applying the previous function to the "Description_ENG" column of my Excel file
        review_traits = pers_words.Description_ENG.apply(gensim.utils.simple_preprocess)

        #reading the Excel file with the skills of each proffesion
        skills_professions=pd.read_excel(r"C:\Users\amohedasgonzalez\Downloads\0.Ironhack\Proyectos\Final project\skills_professions.xlsx")

        #Applying the  function to the "Skills_ENG" column of my Excel file
        review_skills = skills_professions.Skills_ENG.apply(gensim.utils.simple_preprocess)

        ##### CALCULATING WORD SIMILARITY: CREATING THE FINAL DATAFRAME ("skills_professions") WITH THE FINAL SIMILARITY SCORE FOR EACH PROFESSION REGARDING EACH TYPE OF PERSONALITY (ONLY PROFESSIONS RELATED TO THE HEALTH SCIENCE DEGREES)
        
        number_rows=skills_professions.shape[0]-1 #calculating number of rows to know how many times thw while loop should be executed belowm (number of rows (30 rows -> from 0 to 29 index))
        

        ### Calculating word similarity between the skills of all professions and traits of type of personality 1

        traits_highest_similarity_type1=[]
        sums_traits_highest_similarity_type1=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[0]: #0 because personality type 1 is in the first row [0] of the dataframe

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0] #using cosine_similarity to calculate words similarity between trait and skill

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits of personality 1:
                traits_highest_similarity_type1.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 1 with the aim of creating the new column in the dataframe with these results
            sums_traits_highest_similarity_type1.append(sum(traits_highest_similarity_type1))
            
            #reset the list in each while loop
            traits_highest_similarity_type1=[]

        skills_professions["Type_1"]=sums_traits_highest_similarity_type1

        ### Calculating word similarity between the skills of all professions and traits of type of personality 2

        traits_highest_similarity_type2=[]
        sums_traits_highest_similarity_type2=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[1]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type2.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 2 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type2.append(sum(traits_highest_similarity_type2))
            
            #reset the list in each while loop
            traits_highest_similarity_type2=[]

        skills_professions["Type_2"]=sums_traits_highest_similarity_type2

        ### Calculating word similarity between the skills of all professions and traits of type of personality 3

        traits_highest_similarity_type3=[]
        sums_traits_highest_similarity_type3=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[2]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type3.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 3 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type3.append(sum(traits_highest_similarity_type3))
            
            #reset the list in each while loop
            traits_highest_similarity_type3=[]

        skills_professions["Type_3"]=sums_traits_highest_similarity_type3

        ### Calculating word similarity between the skills of all professions and traits of type of personality 4

        traits_highest_similarity_type4=[]
        sums_traits_highest_similarity_type4=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[3]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type4.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 4 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type4.append(sum(traits_highest_similarity_type4))
            
            #reset the list in each while loop
            traits_highest_similarity_type4=[]

        skills_professions["Type_4"]=sums_traits_highest_similarity_type4

        ### Calculating word similarity between the skills of all professions and traits of type of personality 5

        traits_highest_similarity_type5=[]
        sums_traits_highest_similarity_type5=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[4]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type5.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 5 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type5.append(sum(traits_highest_similarity_type5))
            
            #reset the list in each while loop
            traits_highest_similarity_type5=[]

        skills_professions["Type_5"]=sums_traits_highest_similarity_type5

        ### Calculating word similarity between the skills of all professions and traits of type of personality 6

        traits_highest_similarity_type6=[]
        sums_traits_highest_similarity_type6=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[5]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type6.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 6 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type6.append(sum(traits_highest_similarity_type6))
            
            #reset the list in each while loop
            traits_highest_similarity_type6=[]

        skills_professions["Type_6"]=sums_traits_highest_similarity_type6

        ### Calculating word similarity between the skills of all professions and traits of type of personality 7

        traits_highest_similarity_type7=[]
        sums_traits_highest_similarity_type7=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[6]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type7.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 7 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type7.append(sum(traits_highest_similarity_type7))
            
            #reset the list in each while loop
            traits_highest_similarity_type7=[]

        skills_professions["Type_7"]=sums_traits_highest_similarity_type7

        ### Calculating word similarity between the skills of all professions and traits of type of personality 8

        traits_highest_similarity_type8=[]
        sums_traits_highest_similarity_type8=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[7]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type8.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 8 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type8.append(sum(traits_highest_similarity_type8))
            
            #reset the list in each while loop
            traits_highest_similarity_type8=[]

        skills_professions["Type_8"]=sums_traits_highest_similarity_type8 

        ### Calculating word similarity between the skills of all professions and traits of type of personality 9

        traits_highest_similarity_type9=[]
        sums_traits_highest_similarity_type9=[]

        m=0
        while m<=number_rows:

            for skill in review_skills.loc[m]:

                max_answer_trait=-100 #number at random because I believe that any similarity is as low as -100
                trait_max=0

                for trait in review_traits.loc[8]: 

                    answer_trait=cosine_similarity([model[trait]],[model[skill]])[0][0]

                    if answer_trait>max_answer_trait:
                        max_answer_trait=answer_trait
                        trait_max=trait

                #Extracting the highest similarity between the specific skill and all of the traits:
                traits_highest_similarity_type9.append(max_answer_trait)
                
            m=m+1
            
            #append the result of each profession regarding type 9 with the aim of creating the new column with these results in the dataframe
            sums_traits_highest_similarity_type9.append(sum(traits_highest_similarity_type9))
            
            #reset the list in each while loop
            traits_highest_similarity_type9=[]

        skills_professions["Type_9"]=sums_traits_highest_similarity_type9

        #--------------------------------------------------------------------

        ##### CALCULATING WORD SIMILARITY: FILTERING THE FINAL DATAFRAME THAT WE HAVE JUST CREATED ("skills_professions") WITH THE TOP PROFESSIONS WITH THE HIGHEST SCORE IN EACH PERSONALITY TYPE (ONLY HEALTH SCIENCE DEGREES)
        
        personality_types=["Type_1","Type_2","Type_3","Type_4","Type_5","Type_6","Type_7","Type_8","Type_9" ]

        for i in personality_types:
            top=skills_professions.nlargest(5, [i]) #identifying the top 5 professions & degree
            top_professions= top[["Top Professions","Degree"]].to_markdown(index=False) #.to_markdown(index=False) to remove the index in the dataframe that is printed in the table that is shown in the app
            
            if i == "Type_1":
                top_professions_type_1=top_professions    
                
            elif i == "Type_2":
                top_professions_type_2=top_professions
                
            elif i == "Type_3":
                top_professions_type_3=top_professions
                
            elif i == "Type_4":
                top_professions_type_4=top_professions
                
            elif i == "Type_5":
                top_professions_type_5=top_professions
            
            elif i == "Type_6":
                top_professions_type_6=top_professions
                
            elif i == "Type_7":
                top_professions_type_7=top_professions
            
            elif i == "Type_8":
                top_professions_type_8=top_professions
            
            else:
                top_professions_type_9=top_professions
     
        if final_str_max_key=="Type 1 - The Reformer":
            st.header("Step 2:")
            st.write('**Top professions for Type 1 - The Reformer**: ')
            top_professions_type_1
    
        elif final_str_max_key=="Type 2 - The Helper":
            st.header("Step 2:")
            st.write('**Top professions for Type 2 - The Helper**: ')
            top_professions_type_2

        elif final_str_max_key=="Type 3 - The Achiever":
            st.header("Step 2:")
            st.write('**Top professions for Type 3 - The Achiever**: ')
            top_professions_type_3
        
        elif final_str_max_key=="Type 4 - The Individualist":
            st.header("Step 2:")
            st.write('**Top professions for Type 4 - The Individualist**: ')
            top_professions_type_4

        elif final_str_max_key=="Type 5 - The Investigator":
            st.header("Step 2:")
            st.write('**Top professions for Type 5 - The Investigator**: ')
            top_professions_type_5

        elif final_str_max_key=="Type 6 - The Loyalist":
            st.header("Step 2:")
            st.write('**Top professions for Type 6 - The Loyalist**: ')
            top_professions_type_6

        elif final_str_max_key=="Type 7 - The Enthusiast":
            st.header("Step 2:")
            st.write('**Top professions for Type 7 - The Enthusiast**: ')
            top_professions_type_7

        elif final_str_max_key=="Type 8 - The Challenger":
            st.header("Step 2:")
            st.write('**Top professions for Type 8 - The Challenger**: ')
            top_professions_type_8

        else:
            st.header("Step 2:")
            st.write('**Top professions for Type 9 - The Peacemaker**: ')
            top_professions_type_9

        st.write("\n")
        st.header("Step 3: ")
        st.write("Now, it's time to visit the [Degree Finder](http://localhost:8501/Degree_Finder)!")
#--------------------------------------------------------------------


#--------------------------------------------------------------------


#--------------------------------------------------------------------
