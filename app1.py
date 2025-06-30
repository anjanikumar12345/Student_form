import streamlit as st
import pandas as pd
import os
from datetime import datetime




st.markdown("""
<div style="background-color:#ffcc00; padding:20px; border-radius:10px;">
  <marquee behavior="scroll" direction="left" scrollamount="6">
    📢 Admissions open for all classes from UKG to 10th – Register now at ANJANIKUMAR TUTORIALS! | Weekly Online Tests | Evening Classes 6PM - 8PM | Contact: 8328134929
  </marquee>
</div>
""", unsafe_allow_html=True)



# CSV file to store data
DATA_FILE = 'students.csv'
ADMIN_PASSWORD = 'admin123'  # Change this to a secure password

# Initialize data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Class", "School Name", "Parent Name", "Contact", "Address", "Date of Joining"])
    df.to_csv(DATA_FILE, index=False)

# Function to load data
def load_data():
    return pd.read_csv(DATA_FILE)

# Function to save data
def save_data(new_data):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# Function to delete a student by index
def delete_student(index):
    df = load_data()
    df = df.drop(index)
    df.to_csv(DATA_FILE, index=False)

# Streamlit app starts
st.title("📝 ANJANIKUMAR TUTORIALS - Student Registration Form")

# Option to select mode
mode = st.sidebar.selectbox("Select Mode", ["Register", "Admin"])

# --------------------------------
# 👦 STUDENT REGISTRATION FORM
# --------------------------------
if mode == "Register":
    st.subheader("Student Registration Form")
    with st.form("registration_form"):
        name = st.text_input("Student Name")
        student_class = st.selectbox("Class", [f"{i}th" for i in range(1, 11)])
        school = st.text_input("School Name")
        parent = st.text_input("Parent Name")
        contact = st.text_input("Contact Number")
        address = st.text_area("Address")
        date = st.date_input("Date of Joining", value=datetime.today())

        submitted = st.form_submit_button("Register")

        if submitted:
            if name and student_class and school and parent and contact and address:
                data = {
                    "Name": name,
                    "Class": student_class,
                    "School Name": school,
                    "Parent Name": parent,
                    "Contact": contact,
                    "Address": address,
                    "Date of Joining": date
                }
                save_data(data)
                st.success("✅ Student Registered Successfully!")
            else:
                st.warning("Please fill all fields.")

# --------------------------------
# 🔐 ADMIN PANEL
# --------------------------------
elif mode == "Admin":
    st.subheader("Admin Login")
    password = st.text_input("Enter Admin Password", type="password")

    if password == ADMIN_PASSWORD:
        st.success("Logged in as Admin")
        st.subheader("📋 Registered Students")
        df = load_data()

        if df.empty:
            st.info("No registrations yet.")
        else:
            st.dataframe(df, use_container_width=True)

            st.subheader("🗑️ Delete a Student Record")
            delete_index = st.number_input("Enter Row Index to Delete", min_value=0, max_value=len(df) - 1, step=1)
            if st.button("Delete Record"):
                delete_student(delete_index)
                st.success(f"Deleted record at index {delete_index}")
    elif password != "":
        st.error("Incorrect password!")


st.markdown("""
    <style>
    .stApp {
        background-color: #bce5f3; /* Light blue background */
    }
    .stButton > button {
        background-color: #f4fc0b ;
        color: white;
        font-size: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)



import streamlit as st

st.markdown("""
<div style="background-color:#ffcc00; padding:10px; border-radius:5px;">
  <marquee behavior="scroll" direction="left" scrollamount="6">
    📢 Admissions open for all classes from UKG to 10th – Register now at ANJANIKUMAR TUTORIALS! | Weekly Online Tests | Evening Classes 6PM - 8PM | Contact: 8328134929
  </marquee>
</div>
""", unsafe_allow_html=True)


