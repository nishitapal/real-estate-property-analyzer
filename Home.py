import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
)




st.title("📊 Gurgaon Real Estate Insights & Price Prediction")

st.markdown(
    """
    Welcome to your one-stop tool for Gurgaon property analysis.  
    - Explore **market trends** and **price analytics**.  
    - Get **instant property price predictions** using our ML model.  
    - Make smarter, data-driven decisions in seconds.
    """
)







st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### ⚡ Real-time Predictions")
    st.write("Instant property price estimates powered by advanced ML models.")

with col2:
    st.markdown("### 📊 Detailed Analytics")
    st.write("Explore Gurgaon property trends and market patterns effortlessly.")

with col3:
    st.markdown("### 🖱️ Easy to Use")
    st.write("Clean, beginner-friendly interface for quick navigation and smooth experience.")

