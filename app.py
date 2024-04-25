import streamlit as st

with st.expander("basic linux commands"):
    st.markdown("- check top 10 process running with memory%: **ps aux --sort=-%mem | head**")
    st.markdown("- kill any process with pid: **kill pid**")
    st.markdown("- check total , used , free, shared memory : **free -h**")
