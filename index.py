import streamlit as st
import os
from pymongo import MongoClient
 
# ---- MongoDB connection ----
# Local MongoDB: "mongodb://localhost:27017"
# MongoDB Atlas: paste your connection string instead

MONGO_URI = os.getenv("MONGO_URI", "mongodb://Admin:Anirudh123@localhost:27017/?authSource=admin")
 
client = MongoClient(MONGO_URI)
db = client["mydatabase"]        # database name (created automatically)
collection = db["students"]      # collection name (created automatically)
 
# ---- Frontend ----
st.title("Add Data to MongoDB")
 
with st.form("data_form", clear_on_submit=True):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    submitted = st.form_submit_button("Save")
 
if submitted:
    if name and email:
        collection.insert_one({"name": name, "email": email, "age": int(age)})
        st.success("Data saved to MongoDB!")
    else:
        st.warning("Please fill in name and email.")
 
# ---- Show data stored in MongoDB ----
st.subheader("Data in MongoDB")
records = list(collection.find({}, {"_id": 0}))  # hide the _id field
if records:
    st.table(records)
else:
    st.info("No data yet.")
 