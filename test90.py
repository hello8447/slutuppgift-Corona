import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html


# skriva ut felmedelanden på skärmen
def errorMsg(txt):
  print(txt)
  print("")


# 1 - skapa ett cirkeldiagram för antal män och kvinnor som har dött 
# plotly express pie chart
def deathsByGenderPie():
  try:  
    df = pd.read_csv("Gender_Data.csv")   # Läsa in filen där data finns
      
    fig = px.pie(df, values='Total_Deaths', names='Gender', title='propotion male and female who have died due to the Corona virus',  color_discrete_sequence=px.colors.sequential.Rainbow) # skapar själva diagrammet och skapar namn,titlar och färger på diagrammet
    fig.show()  # ritar ut diagrammet som den skapade raden ovanför
  except IOError:   # skapar ett felmedelande 
    errorMsg("Installera databasen Gender_Data.csv först")    # om programmet inte hittar datafilen skriver den ut detta


# 2 - skapa ett stapeldiagram för antal döda per åldersgrupp
# pandas/matplotlib bar chart
def deathsByAgeBar():
  try:  
    df = pd.read_csv("National_Total_Deaths_by_Age_Group.csv", index_col="Age_Group") # Läsa in filen där data finns, man använder columnen Age_Group som x-värde

    df.plot.bar(stacked=True, figsize=(10,10)) # skapar flera lager på staplerna
    plt.ylabel('Cases')   # skpar ett namn till y-axeln
    plt.title('Outcomes per age group')   # skapar en title
    plt.show()    # ritar diagrammet
  except IOError:   # Ifall data filen inte finns på datorn ska man printa ut ett felmedelande
    errorMsg("Installera databasen National_Total_Deaths_by_Age_Group.csv först")   # om programmet inte hittar datafilen skriver den ut detta


# 3 - skapa ett stapeldiagram för antal döda per åldersgrupp med pyplot
# pandas subplot pie chart
def ageByCasePies():
  try:
    df = pd.read_csv("National_Total_Deaths_by_Age_Group.csv", index_col="Age_Group") # Läsa in filen där data finns, man använder columnen Age_Group som x-värde

    df.plot.pie(subplots=True, figsize=(30, 10))    # Man kan se flera diagram 
    plt.show()    # printar grafen
  except IOError:  
    errorMsg("Installera databasen National_Total_Deaths_by_Age_Group.csv först")  # om programmet inte hittar datafilen skriver den ut detta


# 4 - skapa ett linjediagram för antal döda per dag 
# plotly express line chart
def deathsByDayLine():
  try:  
    df = pd.read_csv("National_Daily_Deaths.csv") # Läsa in filen där data finns

    fig = px.line(df, x="Date", y="National_Daily_Deaths", title="National daily deaths")   # skapar linje diagramet, bestämmer även x och y axeln 
    fig.show()
  except IOError: # ifall man inte har installerat datan på datorn ska detta printas ut
    errorMsg("Installera databasen National_Daily_Deaths.csv först") # om programmet inte hittar datafilen skriver den ut detta


# 5 - skapa ett linjediagram för antal döda per vecka kommunvis 
# plotly dash line chart
def deathsByWeekCityLine(): 
  try:
    df = pd.read_csv("Municipality_Weekly_Data.csv") # Läsa in filen där data finns

    fig = px.bar(df, x="Week_Number", y="Weekly_Cases_per_100k_Pop", color="Municipality", opacity=0.2, barmode="overlay", title="Weekly cases per 100k population per municipaly", labels={"Week_Number": "1-5 is 2021     Week_Number     6-53 is 2020"}) # Skapar linjediagrammet, opacity är hur genomskinig färgen ska vara, barmode är att graferna ritas på lager på varandra, graferna står framför varadra från skillnad till stacked, color = Municipality talar om att de kolumnen ger den varje unikt värde tillges en färg 
    # lånad men anpassad kod från Hello Dash exemplet på http://dash.plotly.com/layout
    # skapar dashboarden
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']   
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div(children=[ 
      html.H1(children="Corona statistics"), # anpassad til mitt program, skapar en rubrik
      dcc.Graph(id="corona-graph", figure=fig) # anpassad til mitt program, skapar en graf
    ])  
    if __name__ == "__main__":    
      app.run_server(debug=False)
    # slut lånad kod
  except IOError:   
    errorMsg("Installera databasen Municipality_Weekly_Data.csv först") # om programmet inte hittar datafilen skriver den ut detta

    

# Det är här själva programmet börjar
menuChoice = 1 # sätt menuChoice till ett värde som är skillt från 0, vilket värde spelar ingen roll, det är bara för att gå igenom nedanstående test första gången
while (menuChoice != 0):  # Loop som snurrar runt tills man väljer 0 för att avsluta
  
  # skapar meny val till användaren 
  
  print("Välj diagram corona statistik:")   
  print("") # skapar ett mellanrum 
  print("1. Cirkeldiagram antal döda män/kvinnor               (plotly express)")
  print("2. Antal döda per åldersgrupp                         (pandas/matplotlib)")
  print("3. Åldersfördelning av sjukdomsfall/iva-fall/dödsfall (pandas subplot)")
  print("4. Antal döda per dag                                 (plotly express)")
  print("5. Döda per vecka kommunvis                           (plotly dash)")
  print("") # skapar ett mellanrum 
  print("0. Avsluta")
  print("")
 
  try:        
    menuChoice = int(input("Välj 0-5: "))   # personen ska välje vilken nummer man vill ha
  except ValueError:    # hit kommer du om det har angett ett ogiltligt värde 
    menuChoice = -1 # sätt menuChoice till -1 (vilket värde spelar ingen roll bara om det är skillt från 0-5 dvc de giltliga värderna). På detta sätt kommer vi att ramla in i fel testen nedan

  print("") # skapar ett mellanrum
  if menuChoice == 1: # Cirkeldiagram döda kön
    deathsByGenderPie()   # skriva ut grafen
  elif menuChoice == 2: # Döda per åldersgrupp
    deathsByAgeBar()    # skriva ut grafen
  elif menuChoice == 3: # Åldersfördelning per sjukdomskategori
    ageByCasePies()   # skriva ut grafen
  elif menuChoice == 4: # Döda per dag
    deathsByDayLine() # skriva ut grafen
  elif menuChoice == 5: # Döda kommunvis
    deathsByWeekCityLine()  # skrive ut grafen
  elif menuChoice == 0: # Avsluta
    print("Hej då!")    # ska säga hej då om man avslutar
  else: # ifall personen inte väljer några av alternativen 
    errorMsg("Du måste ange en siffra 0-5") # ska den printa detta
    