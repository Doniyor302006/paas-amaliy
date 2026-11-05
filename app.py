import streamlit as st
st.title("PaaS bulutli ilovasi")
ism = st.text_input("Ismingizni kiriting")
guruh = st.text_input("Guruhingizni kiriting")
Fakultitet =  st.text_input("Fakultetingizni kiriting")

if st.button("Natijani ko'rsatish"):
 if ism.strip() and guruh.strip(): 
  st.success(f"Salom, {ism}!")
  st.write(f"Guruhingiz: {guruh}")
  st.write(f"Fakultetingiz: {Fakultitet}")
 else:
  st.warning("Barcha maydonlarni to'ldiring")
