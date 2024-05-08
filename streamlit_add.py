import streamlit as st
import pandas as pd
import plotly.express as px 
import os

st.title("My Dashboard")

df = pd.read_csv(r"apple_products.csv",encoding="ISO-8859-1")
st.write(df)


df.sort_values(['Star Rating','Number Of Ratings'],axis=0,ascending=[False,False],inplace=True)
print(df.head(10))


### Graph  b/w no of rating and its sales price
fig=px.bar(df,x="Sale Price",y='Star Rating',color="Product Name",width=1000,title='Graph  b/w No of rating and sales price')
st.plotly_chart(fig)


### Graph  b/w Product Name and Sales price
fig=px.bar(df.head(10),x="Product Name",y='Sale Price',color="Product Name",title='Graph  b/w Product Name and Sales price')
st.plotly_chart(fig)


### Graph b/w No of Reviews and Product Name
fig=px.pie(df.head(10),names='Product Name',values='Number Of Reviews',title='Graph b/w No of Reviews and Product Name')
st.plotly_chart(fig)



### Graph  b/w MRP and its Discount Percentage
fig=px.scatter(df.head(20),x="Product Name",y='Discount Percentage',size='Mrp',color='Mrp',height=700,
               width=1000,title='Graph  b/w MRP and  Discount Percentage')
st.plotly_chart(fig)