import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Customer Segmentation Insights", layout="wide")

st.title("Customer Segmentation Dashboard")

st.markdown("""
Welcome! This dashboard helps you understand your customers using RFM (Recency, Frequency, Monetary) analysis and clustering. Each customer is grouped into a segment based on their shopping behavior. Use the tabs below to explore your customer base and discover actionable insights.

- **Recency**: How recently a customer made a purchase
- **Frequency**: How often they purchase
- **Monetary Value**: How much they spend

**Segments** are based on these patterns (e.g., DELIGHT, RE-ENGAGE, etc.).
""")

# Load data
data = pd.read_csv("customer_clusters.csv")

# Cluster descriptions
descriptions = {
    "RETAIN": "High-value, regular customers. Focus on retention.",
    "RE-ENGAGE": "Low-value, infrequent buyers. Target for re-engagement.",
    "NURTURE": "Recent but low-value customers. Nurture for growth.",
    "REWARD": "Top loyal customers. Reward their loyalty.",
    "PAMPER": "High spenders, infrequent. Offer luxury/personalized services.",
    "UPSELL": "Frequent buyers, low spend. Upsell opportunities.",
    "DELIGHT": "Top-tier, frequent and high spenders. VIP treatment."
}

# Tabs for navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Segment Overview", "RFM by Segment", "Segment Details", "Customer Lookup", "Download Data"
])

with tab1:
    st.header("Customer Segment Distribution")
    seg_counts = data['ClusterLabel'].value_counts().sort_values(ascending=False)
    st.bar_chart(seg_counts, use_container_width=True)
    st.dataframe(seg_counts.rename_axis('Segment').reset_index(name='Count'), use_container_width=True)
    st.markdown("**Segment Descriptions:**")
    for seg, desc in descriptions.items():
        st.markdown(f"- **{seg}**: {desc}")

with tab2:
    st.header("RFM Feature Means by Segment")
    rfm_means = data.groupby('ClusterLabel')[['Recency', 'Frequency', 'MonetaryValue']].mean().round(2)
    st.dataframe(rfm_means, use_container_width=True)
    st.markdown("**Visual Comparison:**")
    st.subheader("Recency by Segment")
    st.bar_chart(rfm_means['Recency'], use_container_width=True)
    st.subheader("Frequency by Segment")
    st.bar_chart(rfm_means['Frequency'], use_container_width=True)
    st.subheader("Monetary Value by Segment")
    st.bar_chart(rfm_means['MonetaryValue'], use_container_width=True)

with tab3:
    st.header("Explore Segment Details")
    segment = st.selectbox("Select a segment to view details:", sorted(data['ClusterLabel'].unique()))
    st.markdown(f"**Description:** {descriptions.get(segment, 'No description available.')}")
    seg_df = data[data['ClusterLabel'] == segment]
    st.write(f"Number of customers: {len(seg_df)}")
    st.write("**RFM Statistics:**")
    st.dataframe(seg_df[['Recency', 'Frequency', 'MonetaryValue']].describe().T, use_container_width=True)
    st.write("**Sample Customers:**")
    st.dataframe(seg_df.head(10), use_container_width=True)

with tab4:
    st.header("Customer Lookup")
    cust_id = st.text_input("Enter CustomerID to lookup:")
    if cust_id:
        # Ensure the input is always in the float format with .0
        cust_id_float = f"{float(cust_id):.1f}"
        result = data[data['Customer ID'].astype(str) == cust_id_float]
        if not result.empty:
            st.write("**Customer Details:**")
            st.dataframe(result, use_container_width=True)
            st.markdown(f"**Segment:** {result.iloc[0]['ClusterLabel']} - {descriptions.get(result.iloc[0]['ClusterLabel'], '')}")
        else:
            st.warning("CustomerID not found.")

with tab5:
    st.header("Download Segmentation Data")
    st.download_button(
        label="Download CSV",
        data=data.to_csv(index=False),
        file_name="customer_clusters.csv",
        mime="text/csv"
    )
    st.info("You can download the full customer segmentation data for further analysis.")


st.sidebar.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=180)
st.sidebar.title("Customer Segmentation App")
st.sidebar.markdown("""
This interactive dashboard helps you:
- Understand your customer segments
- Explore RFM features
- Lookup individual customers
- Download the data for further analysis

**Tip:** Use the tabs above to navigate!
""")
