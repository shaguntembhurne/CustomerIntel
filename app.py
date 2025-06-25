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
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = sns.color_palette('Set2', n_colors=len(seg_counts))
    bars = ax.bar(seg_counts.index, seg_counts.values, color=colors, edgecolor='black')
    ax.set_ylabel('Number of Customers', fontsize=12)
    ax.set_xlabel('Segment', fontsize=12)
    ax.set_title('Number of Customers per Segment', fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.bar_label(bars, padding=3, fontsize=11)
    plt.xticks(rotation=15, ha='right', fontsize=11)
    plt.yticks(fontsize=11)
    plt.tight_layout()
    st.pyplot(fig)
    st.dataframe(seg_counts.rename_axis('Segment').reset_index(name='Count'))
    st.markdown("**Segment Descriptions:**")
    for seg, desc in descriptions.items():
        st.markdown(f"- **{seg}**: {desc}")

with tab2:
    st.header("RFM Feature Means by Segment")
    rfm_means = data.groupby('ClusterLabel')[['Recency', 'Frequency', 'MonetaryValue']].mean().round(2)
    st.dataframe(rfm_means)
    st.markdown("**Visual Comparison:**")
    features = ['Recency', 'Frequency', 'MonetaryValue']
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    colors = sns.color_palette('Set2', n_colors=len(rfm_means))
    for i, feature in enumerate(features):
        axes[i].bar(rfm_means.index, rfm_means[feature], color=colors, edgecolor='black')
        axes[i].set_title(f'{feature} by Segment', fontsize=13, fontweight='bold')
        axes[i].set_xlabel('Segment', fontsize=11)
        axes[i].set_ylabel(f'Mean {feature}', fontsize=11)
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)
        axes[i].tick_params(axis='x', rotation=15)  
        for bar in axes[i].patches:
            axes[i].annotate(f'{bar.get_height():.1f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                             ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

with tab3:
    st.header("Explore Segment Details")
    segment = st.selectbox("Select a segment to view details:", sorted(data['ClusterLabel'].unique()))
    st.markdown(f"**Description:** {descriptions.get(segment, 'No description available.')}")
    seg_df = data[data['ClusterLabel'] == segment]
    st.write(f"Number of customers: {len(seg_df)}")
    st.write("**RFM Statistics:**")
    st.dataframe(seg_df[['Recency', 'Frequency', 'MonetaryValue']].describe().T)
    st.write("**Sample Customers:**")
    st.dataframe(seg_df.head(10))

with tab4:
    st.header("Customer Lookup")
    cust_id = st.text_input("Enter CustomerID to lookup:")
    if cust_id:
        result = data[data['CustomerID'].astype(str) == cust_id]
        if not result.empty:
            st.write("**Customer Details:**")
            st.dataframe(result)
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
