import streamlit as st


st.title("What is Machine Learning?")
st.write("ML is technique to train the computer , how to work like a human brain!!")



col1,col2,col3 = st.tabs(['Basics','Python','ML-Lifecycle'])
with col1:
    with st.expander("Tree based Algorithm"):
        st.subheader("Decision Tree:\n")

        st.markdown("- This alogrithm is based on tree like structure. In which we have a root node, leaf node and will split the given sample on the features. It is easy to explain.\n")

        st.subheader("Random Forest\n")
        st.markdown("It is a ensemble technique which is based on bagging, \n")
        st.subheader("Xgboost\n")
        st.subheader("LightGBM")

with col2:
    st.subheader("Python: 🐍 ")
    st.markdown("Python has so many liberary to evaluate the data , and solve problem using ML")

    with st.expander("Data"):
        st.markdown("## pandas\n"
                    "- df.head(),df.describe(), df.isnull().sum()")
        st.link_button("try yourself", "https://evaluate-your-data.streamlit.app/")


