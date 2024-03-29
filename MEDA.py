import numpy as np
import pandas as pd
import plotly.express as px

df =pd.read_csv("./Sources/german_cars_cleaned.csv")

def tob_10_carss (col):
    df_top25_hp=df.groupby('hp')['price'].count().sort_values(ascending = False).reset_index().head(25)
    df_top_25 = df[df.hp.isin(df_top25_hp.hp.unique())].reset_index(drop= True)
    # df_top_10 = df_top_25.sort_values(by= 'price', ascending= False).head(10)
    df_fuel_price = df_top_25.loc[df_top_25.groupby('fuel')['price'].idxmax()]
    # df_top_10 =df.sort_values(by=col ,ascending=False).head(10)
    fig =px.bar(df,x='hp',y=col ,color_continuous_scale='purp',hover_data=['make','model'])
    fig = px.bar(df_fuel_price, x= 'fuel', y= col, color=  'price' , color_continuous_scale= 'inferno',hover_data=['make','model'])
    fig.update_layout(title= {'text': "Relation Between Fuel And Price", 'x':.2, 'y': 0.95})
    return fig



                             
