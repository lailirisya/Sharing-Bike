import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header('DICODING : SUBMISSION ANALISIS DATA DENGAN PYTHON :sparkles:')

all_df = pd.read_csv("all_data.csv")

#Membuat komponen filter
datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


#menampilkan jumlah pelanggan registered berdasarkan season
def create_byseason_df(df):
    day_df.groupby("season",  observed=False).agg({
    "registered" : "sum"
    })
    
    return byseason_df

#Menampilkan data visual dengan jumlah pelanggan registered berdasarkan season

st. subheader("Customer Registered by season")

fig = plt.figure(figsize=(10, 5))
colors = ['grey','grey','grey','blue']
sns.barplot(y="registered", x="season", hue = 'season',  data=all_df.sort_values(by="registered",  ascending=False),
    palette=colors
)
plt.title("customer registered by season", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# #Melakukan groupby
sum_order_items_df = all_df.groupby("hr").cnt.sum().sort_values(ascending=False).reset_index()

def create_casualbyhour_df(df):
    hour_df.groupby(by="hr").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
    }) 
    return casualbyhour_df

#Menampilkan data visual pelanggan berdasarkan jam
st. subheader("Best & Worst Performing Product")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
colors= ['grey','grey','blue','grey','grey']
colors1= ['grey','grey','grey','grey','blue']
sns.barplot(x="hr", hue= 'hr', y="cnt", data=sum_order_items_df.head(5),
            palette=colors, legend=False, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)
 
sns.barplot(x="hr", hue='hr', y="cnt", data=sum_order_items_df.sort_values(
    by="hr", ascending=True).head(5), palette=colors1, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
 
plt.suptitle("Best and Worst Performing Sharing Bike by hour", fontsize=20)
st.pyplot(fig)