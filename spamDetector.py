import streamlit as st
import pickle

model = pickle.load(open("naive-bayes-classifier.pkl",'rb'))
cv = pickle.load(open("vectorizer.pkl",'rb'))

def main():
    st.title("Email Spam Classification")
    st.write("This is a machine learinig algorithm to classify emails as spam or not spam.")
    st.subheader("Classfication")
    user_input = st.text_area("Enter email to classify", height=150)
    if st.button("Classify"):
        if(user_input):
            data = [user_input]
            print(data)
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.success("This is not a spam email")
            else:
                st.error("This is a spam email")
        else:
            st.write("Please enter an email to classify")
main()