# 🧠 CustomerIntel – Customer Segmentation Dashboard

An interactive **Streamlit** dashboard for visualizing customer segmentation using RFM analysis and clustering. This tool helps businesses identify high-value customers, churn risks, and upsell opportunities with actionable insights.

---

## 📁 Repository Structure

```
CustomerIntel/
├── app.py                  # Streamlit dashboard
├── customer_clusters.csv   # Final data with RFM and cluster labels
├── online-data-clustering.ipynb # Notebook with RFM & clustering logic
├── online_retail_II.xlsx   # Raw transactional data
├── requirements.txt        # Python dependencies
└── README.md               # Project overview & instructions
```

---

## 📊 What is RFM?

**RFM** is a proven method to evaluate customer value based on:

- **Recency** – How recently a customer made a purchase (in days)
- **Frequency** – How often they make purchases
- **Monetary** – How much they spend in total

By scoring and clustering customers on these metrics, we can group them into actionable segments like:

- **DELIGHT** – Frequent, recent buyers with high spend  
- **NURTURE** – Low frequency and low value  
- **RE-ENGAGE** – Previously active but now inactive  
- **UPSELL** – Mid-value customers with potential to grow  

These insights guide targeted marketing and retention strategies.

---

## 🚀 Features

- 🏠 **Home**  
  Project summary & key use cases

- 📊 **Cluster Overview**  
  - Bar chart showing number of customers per segment  
  - Visualizations of average Recency, Frequency, and Monetary value per cluster  

- 🔍 **Customer Lookup**  
  - Search by CustomerID to see RFM score and assigned segment  

- ⬆️ **(Optional) Upload New Data**  
  - Upload CSV file and apply clustering model (if available)

---

## 🛠 Tech Stack

- **Python** – Data analysis with Pandas & Numpy  
- **Scikit-learn** – KMeans clustering  
- **Streamlit** – Dashboard frontend  
- **Matplotlib / Plotly** – Visualizations  
- **Jupyter Notebook** – Data preparation and logic

---

## 📈 Business Benefits

- 🎯 **Target high-value customers** with specific campaigns  
- 🔁 **Win back lost users** using RE-ENGAGE group  
- 💰 **Upsell** based on user purchasing patterns  
- 📊 **Turn raw data into real-time insights** for marketing teams

---

## 🧪 How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/shaguntembhurne/CustomerIntel.git
   cd CustomerIntel
   ```

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is for educational and demonstration purposes.

---

**Made with ❤️ using Streamlit**