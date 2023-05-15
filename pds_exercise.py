import pandas as pd
import sqlite3

data = {
    'apples' : [3,6,7,8],
    'pears' : [6,10,5,0]
}

df = pd.DataFrame(data, index =['Burkhard', 'Johannes', 'Berin', 'Peter'])

# loc = locate
#print(df.loc['Berin'])

#df = pd.read_csv("purchases.csv", index_col=0)  #index kann man wegmachen, durch index_col = 0
#print(df)

#con = sqlite3.connect("database.db")
#df = pd.read_sql_query("SELECT * FROM purchases", con)
#print(df)

movies_df = pd.read_csv("movies.csv")
#print(movies_df.head(20))#Einschränkung auf 20 Zeilen
#print(movies_df.tail(10))
#print(movies_df.info())


#temp_df = movies_df.append(movies_df)
#print(movies_df.shape)

#temp_df = temp_df.drop_duplicates()
#print(temp_df.shape)

#print(temp_df[['Genre', 'Title']])
#print(temp_df.columns)

#revenue = movies_df['Revenue (Millions)'] #Gewinn wird geprintet
#print(revenue.dropna().mean()) #diejenigen die Leer sind, werden nicht geprintet durch dropna()
#print(revenue.describe())

#print(movies_df['Genre'].describe())
#print(movies_df['Genre'].value_counts())

#print(movies_df.corr())
#print(movies_df.columns)
#condition = (movies_df['Director'] == "Ridley Scott")
#print(condition)
#filtered_df = movies_df[movies_df['Director'] == "Ridley Scott"] #Condition, die nur die Filme ausgibt, wo der Direktor Ridley Scott ist

#print(filtered_df)
#filtered_df = movies_df[movies_df['Rating'] >= 8.0]
#print(filtered_df)


#Aufgabe 4, weitere Befehle:

#hier werden alle Filme aufsteigend nach ihrem Erscheinungsjahr sortiert
sortierter_df = movies_df.sort_values(by='Year', ascending=True)
print(sortierter_df[['Title','Year']])

gesamt_revenue = movies_df['Revenue (Millions)']
print("Revenue gesamt in Mio. betraegt:", round(gesamt_revenue.sum()))

low_rating = movies_df['Rating']
print("Das niedrigste Rating betraegt:", low_rating.min())

high_rating = movies_df['Rating']
print("Das hoechste Rating betraegt:", high_rating.max())







