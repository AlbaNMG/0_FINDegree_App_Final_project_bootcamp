import streamlit as st
import pandas as pd
import numpy as np

#This is the second page in the app, so please, review the Code of the Home Page .py file first
#Refresh Streamlit documentation is essential to understand the code: https://docs.streamlit.io/

#Configuring the Degree Finder Page: name and icon that appear in the tab on Internet when the app is open
st.set_page_config(
    page_title='Degree Finder', 
    page_icon='🔎', 
    layout="centered", 
    initial_sidebar_state="auto")

#Header and Introduction of the page
st.title('Find your perfect degree!')
st.text("⭐ Available for all categories")
st.header('Step 1:')
st.subheader("Please, select one university")
#Configuring the Sidebar
st.sidebar.markdown("# Degree Finder tool 🔎")
#\n'+ "ㅤㅤstudents who are about to start"+'\n'+"ㅤㅤㅤuniversity to identify which"+'\n'+"ㅤㅤuniversity degrees would be the"+'\n'+ "ㅤㅤㅤbest ones for them based on"+'\n'+"ㅤㅤㅤtheir personality type. 🎯")
st.sidebar.markdown("# Steps:")
st.sidebar.write("▶ Step １: Select one university")
st.sidebar.write("▶ Step ２: Select one category and see all available degrees")
st.sidebar.write("▶ Step ３: Look for one specific degree and see the access grade for the last 3 years")

#Degree finder
from openpyxl import Workbook

#Reading the Excel file where all the degrees, category, access score, etc. from the last 3 school years (2019-20// 2020-21 // 2021-22) of all the public universities of Madrid are stored
degrees_database=pd.read_excel('220802_Integrated database.xlsx')

#converting the following 2 columns of the Excel file to string because otherwise there are a lot of decimals
degrees_database['University_credits']= degrees_database['University_credits'].map(str)
degrees_database['Courses_(Years)']=degrees_database['Courses_(Years)'].map(str)

#creating the drop-down list/ options of universities of Madrid. I added "No selection" because by default always one option is selected
unique_universities=['No selection','Universidad de Alcalá','Universidad Carlos III','Universidad Autónoma de Madrid','Universidad Politécnica de Madrid','Universidad Complutense de Madrid','Universidad Rey Juan Carlos']

#creating the section to select the university
chosen_university = st.radio(
    "Public universities of Madrid:",
    unique_universities)  



#Output based on the selection:
if chosen_university != 'No selection': #"!="" means: if chosen_university "is different" to "No selection"...

    st.header("Step 2:")
    st.subheader('Please, select one category')

    if chosen_university=='Universidad de Alcalá':
        #creating the section to select the category
        chosen_category=st.multiselect('Categories: ',('All categories','Rama de conocimiento de Ciencias Sociales y Jurídicas','Rama de conocimiento de Artes y Humanidades','Rama de conocimiento de Ciencias','Rama de conocimiento de Ciencias de la Salud','Rama de conocimiento de Ingeniería y Arquitectura','Dobles Grados'))

    elif chosen_university=='Universidad Carlos III':
        chosen_category=st.multiselect('Categories: ',('All categories','Rama de conocimiento de Ciencias Sociales y Jurídicas','Rama de conocimiento de Artes y Humanidades','Rama de conocimiento de Ingeniería y Arquitectura','Dobles Grados','Grados conjuntos'))

    elif chosen_university=='Universidad Autónoma de Madrid':
        chosen_category=st.multiselect('Categories: ',('All categories','Rama de conocimiento de Ciencias Sociales y Jurídicas','Rama de conocimiento de Artes y Humanidades','Rama de conocimiento de Ciencias','Rama de conocimiento de Ciencias de la Salud','Rama de conocimiento de Ingeniería y Arquitectura','Dobles Grados','Grados conjuntos'))

    elif chosen_university=='Universidad Politécnica de Madrid':
        chosen_category=st.multiselect('Categories: ',('All categories','Rama de conocimiento de Ciencias Sociales y Jurídicas','Rama de conocimiento de Ciencias','Rama de conocimiento de Ingeniería y Arquitectura','Dobles Grados'))

    elif chosen_university=='Universidad Complutense de Madrid':
        chosen_category=st.multiselect('Categories: ',('All categories','Rama de conocimiento de Ciencias Sociales y Jurídicas','Rama de conocimiento de Artes y Humanidades','Rama de conocimiento de Ciencias','Rama de conocimiento de Ciencias de la Salud','Rama de conocimiento de Ingeniería y Arquitectura','Dobles Grados','Grados conjuntos'))

    else:
        chosen_category=st.multiselect('Categories: ',('All categories','Rama de conocimiento de Ciencias Sociales y Jurídicas','Rama de conocimiento de Artes y Humanidades','Rama de conocimiento de Ciencias','Rama de conocimiento de Ciencias de la Salud','Rama de conocimiento de Ingeniería y Arquitectura','Dobles Grados'))

    #If the user has selected at least one university and one category:
    if bool(chosen_category)==True: #this means that the chosen_category is not empty (it is a list) -> the user has selected one category

 ###### if chosen_category is "All categories", print this (we are creating specific lines of code because there is not a category called "All categories" in the integrated_database with all the degrees and we can not filter the dataframe by that):
        if (chosen_category[0]=='All categories'): #[0] because it is a list and we want to get the first element which is the chosen_category

            st.write('**You have selected:** "'+chosen_category[0]+'" in "'+chosen_university+'"')   
            st.write('See below all the degrees available in 2021-22') 
            
            #removing duplicates rows because casi siempre there are the same degrees in the 3 years (2019, 2021, 22) and we would like to have only one row per degree (not 3 times the same degree)
            degrees_database_without=degrees_database.drop_duplicates(subset=None, 
                                            keep='first', 
                                            inplace=False, 
                                            ignore_index=False)
            
            #show only available degrees in 2021-2022 and sorting the values alphabetically
            filtered_dataframe=degrees_database_without[['University','Category','Degree','University_credits','Courses_(Years)']][(degrees_database['University']==chosen_university)&(degrees_database['Year']=='2021-22')].sort_values('Degree')
            st.write(filtered_dataframe) #printing the dataframe in the app
            
            st.header("Step 3:")
            st.subheader("Please, select or write one specific degree among the available options in "+chosen_university+"...")
            #creating the drop-down list to select a degree
            list_of_degrees=degrees_database[(degrees_database['University']==chosen_university)&(degrees_database['Year']=='2021-22')].sort_values('Degree')
            unique_list_of_degrees=list_of_degrees['Degree'].unique()

            
            chosen_degree=st.multiselect("... and see the access grade evolution",unique_list_of_degrees)

            #Output
            if bool(chosen_degree) == True: 
                data_degree=degrees_database[(degrees_database['University']==chosen_university)&(degrees_database['Degree']==chosen_degree[0])]
                st.write(data_degree[['Year','University','Degree','Access_score']])

                year_2019_20='2019-20'
                year_2020_21='2020-21'
                year_2021_22='2021-22'

                list=[year_2019_20,year_2020_21,year_2021_22]

                for i in list:
                
                    if i == '2019-20':
                        if i in data_degree['Year'].values: #".values" para que te lo busque entre todos los valores de la columna
                            year_2019_20_final=data_degree['Access_score'][data_degree['Year']==i][data_degree['University']==chosen_university][data_degree['Degree']==chosen_degree[0]]
                            year_2019_20_final_number=year_2019_20_final.iloc[0] #iloc[0] para que solo te imprima el contenido de la celda sin info adicional
                            #year_2019_20_final_number
                            
                        else:
                            '2019 - 2020 : no data available'
                            year_2019_20_final_number=0
                            
                    elif i == '2020-21':
                        if i in data_degree['Year'].values:
                            year_2020_21_final=data_degree['Access_score'][data_degree['Year']==i][data_degree['University']==chosen_university][data_degree['Degree']==chosen_degree[0]]
                            year_2020_21_final_number=year_2020_21_final.iloc[0]
                            #year_2020_21_final_number

                        else:
                            '2020 - 2021 : no data available'
                            year_2020_21_final_number=0

                    else: # i == '2021-22':
                                        
                        if i in data_degree['Year'].values:
                            year_2021_22_final=data_degree['Access_score'][data_degree['Year']==i][data_degree['University']==chosen_university][data_degree['Degree']==chosen_degree[0]]
                            year_2021_22_final_number=year_2021_22_final.iloc[0]
                            #year_2021_22_final_number

                        else:
                            '2021 - 2022 : no data available'
                            year_2021_22_final_number=0


                ##############################GRAPH

                #I saw this code on Internet
                
                import altair as alt
                
                #creating a table with this info
                table={'Year':[year_2019_20,year_2020_21,year_2021_22],'Score':[year_2019_20_final_number,year_2020_21_final_number,year_2021_22_final_number]}
                
                #converting table to dataframe
                table_df=pd.DataFrame(table)
                table_index = table_df.set_index(['Year'])

                #Chart
                line_chart = alt.Chart(table_df).mark_line(interpolate='basis').encode(
                                alt.X('Year', title='Year'),
                                alt.Y('Score', title='Access score'),
                                ).properties(
                                title='Access score evolution for the last 3 years:'
                                )

                #printing the
                st.altair_chart(line_chart, use_container_width=True)


 ###### if chosen_category is not "All categories" (chosen_category[0] != 'All categories':)
        else: 

            st.write('**You have selected:** "'+chosen_category[0]+'" category in "'+chosen_university+'"')    
            st.write('See below all the degrees available in 2021-22') 

            degrees_database_without=degrees_database.drop_duplicates(subset=None, 
                                            keep='first', 
                                            inplace=False, 
                                            ignore_index=False)

            #show available degrees in 2021-2022
            filtered_dataframe=degrees_database_without[['University','Category','Degree','University_credits','Courses_(Years)']][(degrees_database['University']==chosen_university)&(degrees_database['Category']==chosen_category[0])&(degrees_database['Year']=='2021-22')].sort_values('Degree')
            st.write(filtered_dataframe)

            st.header("Step 3:")
            st.subheader("Please, select or write one specific degree among the available options in "+chosen_university+"...")

            list_of_degrees=degrees_database[(degrees_database['University']==chosen_university)&(degrees_database['Category']==chosen_category[0])&(degrees_database['Year']=='2021-22')].sort_values('Degree')
            unique_list_of_degrees=list_of_degrees['Degree'].unique()

            chosen_degree=st.multiselect("... and see the access grade evolution",unique_list_of_degrees)

            #Output:

            if bool(chosen_degree) == True: 
                data_degree=degrees_database[(degrees_database['University']==chosen_university)&(degrees_database['Degree']==chosen_degree[0])]
                st.write(data_degree[['Year','University','Degree','Access_score']])

                year_2019_20='2019-20'
                year_2020_21='2020-21'
                year_2021_22='2021-22'

                list=[year_2019_20,year_2020_21,year_2021_22]

                for i in list:
                
                    if i == '2019-20':
                        if i in data_degree['Year'].values: #".values" para que te lo busque entre todos los valores de la columna
                            year_2019_20_final=data_degree['Access_score'][data_degree['Year']==i][data_degree['University']==chosen_university][data_degree['Degree']==chosen_degree[0]]
                            year_2019_20_final_number=year_2019_20_final.iloc[0] #iloc[0] para que solo te imprima el contenido de la celda sin info adicional
                            
                        else:
                            '**** 2019 - 2020 : no data available'
                            year_2019_20_final_number=0
                            
                    elif i == '2020-21':
                        if i in data_degree['Year'].values:
                            year_2020_21_final=data_degree['Access_score'][data_degree['Year']==i][data_degree['University']==chosen_university][data_degree['Degree']==chosen_degree[0]]
                            year_2020_21_final_number=year_2020_21_final.iloc[0]

                        else:
                            '**** 2020 - 2021 : no data available'
                            year_2020_21_final_number=0

                    else: # i == '2021-22':
                                        
                        if i in data_degree['Year'].values:
                            year_2021_22_final=data_degree['Access_score'][data_degree['Year']==i][data_degree['University']==chosen_university][data_degree['Degree']==chosen_degree[0]]
                            year_2021_22_final_number=year_2021_22_final.iloc[0]

                        else:
                            '**** 2021 - 2022 : no data available'
                            year_2021_22_final_number=0


        ##############################GRAPH

                import altair as alt

                table={'Year':[year_2019_20,year_2020_21,year_2021_22],'Score':[year_2019_20_final_number,year_2020_21_final_number,year_2021_22_final_number]}
                table_df=pd.DataFrame(table)
                table_index = table_df.set_index(['Year'])

                line_chart = alt.Chart(table_df).mark_line(interpolate='basis').encode(
                    alt.X('Year', title='Year'),
                    alt.Y('Score', title='Access score'),
                ).properties(
                    title='Access score evoluation for the last 3 years:'
                )

                st.altair_chart(line_chart, use_container_width=True)
