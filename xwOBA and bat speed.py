import pandas as pd
import plotly.express as px

hitting = pd.read_csv('stats.csv')

twovar = px.scatter(hitting, x = hitting['xwoba'], y = hitting['avg_swing_speed'], trendline= 'ols')

twovar.add_annotation(
    x= 0.333, y= 78.8,  
    text='Oneil Cruz',             
    ax=0, ay=-30,               
    font=dict(color='red', size=14)
)
twovar.add_annotation(
    x= 0.476, y= 77, 
    text='Aaron Judge',             
    ax=0, ay=-30,               
    font=dict(color='red', size=14)
)
twovar.add_annotation(
    x= 0.303, y= 62.6,
    text='Luis Arraez',             
    ax=0, ay=-30,               
    font=dict(color='red', size=14)
)