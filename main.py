
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from matplotlib.colors import ListedColormap

df = pd.read_csv("Mall_Customers.csv", sep=',')
print(df.info())
print(df.isna().sum().sum())
df.dropna(inplace=True)
print(df.isna().sum().sum())
print(df.columns)
print(df.shape)
print(df["Education"].value_counts())
print(df["Marital_Status"].value_counts())

df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True)
print(df["Dt_Customer"].dtype)

df["Age"] = 2025 - df["Year_Birth"]
print(df["Age"])

df = df[(df["Age"] < 100) & (df["Income"] < 200000)]

df["Total_Childen"] = df["Kidhome"] + df["Teenhome"]
print(df["Total_Childen"])
print(df.columns)

spend_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df["Total_Spending"] = df[spend_cols].sum(axis = 1)
print(df["Total_Spending"].head())

df["Customer_Since"] = (pd.Timestamp("today") - df["Dt_Customer"]).dt.days
print(df["Customer_Since"])

plt.hist(df["Age"], bins=30, edgecolor="black", alpha=0.6)
plt.title("Age Distribution")
plt.show()

plt.hist(df["Income"], bins=30, edgecolor="black", alpha=0.6)
plt.title("Income Distribution")
plt.show()

plt.hist(df["Total_Spending"], bins=30, edgecolor="black", alpha=0.6)
plt.title("Total Spending Distribution")
plt.show()

print(df.columns)

corr = df[['Income', 'Age', 'Recency', 'Total_Spending', 'NumWebPurchases','NumStorePurchases']].corr()
print(corr.head())

pivot_income = df.pivot_table(values = "Income", index = "Education", columns = "Marital_Status", aggfunc = "mean")
print(pivot_income)

group1 = df.groupby("Education")["Total_Spending"].mean().sort_values(ascending = False)
print(group1)

group1.plot(kind = "bar", color = "skyblue")
plt.title("Average Spending by Education")
plt.ylabel("Average Total Spending")
plt.xticks(rotation = 45)
plt.show()

df["AcceptedAny"] = df[["AcceptedCmp1","AcceptedCmp2","AcceptedCmp3","AcceptedCmp4", "Response"]].sum(axis=1)
print(df["AcceptedAny"].unique())

df["AcceptedAny"] = df["AcceptedAny"].apply(lambda x: 1 if x > 0 else 0)
print(df["AcceptedAny"].unique())

group2 = df.groupby("Marital_Status")["AcceptedAny"].mean().sort_values(ascending = False)
print(group2)

group2.plot(kind = "bar", color = "orange")
plt.title("Campaign Acceptance Rate by Marital Status")
plt.ylabel("Acceptence Rate")
plt.xticks(rotation = 45)
plt.show()

bins = [18, 30, 40, 50, 60, 70, 90]
labels = ["18-29", "30-39", "40-49", "50-59", "60-69", "70+"]
df["AgeGroup"] = pd.cut(df["Age"], bins = bins, labels = labels)
print(df["AgeGroup"])

group3 = df.groupby("AgeGroup")["Income"].mean()
print(group3)

group3.plot(kind = 'bar', color = "green")
plt.title("Average Income by Age Group")
plt.xlabel("Average Income")
plt.show()

print(df.head())
print(df.columns)

features = ["Age", "Income", "Total_Spending", "NumWebPurchases", "NumWebVisitsMonth", "Recency"]
X = df[features].copy()
print(X)

Scaler = StandardScaler()
X_scaled = Scaler.fit_transform(X)
print(X_scaled)

wcss = []
sil_scores = []
for i in range (2,10):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled )
    wcss.append(kmeans.inertia_)
    sil_scores.append(silhouette_score(X_scaled, kmeans.labels_))

print(wcss)
print(sil_scores)

fig, ax1 = plt.subplots(figsize=(10,6))

ax1.set_xlabel('Number of Clusters')
ax1.set_ylabel('WCSS', color='tab:red')
ax1.plot(range(2,10), wcss, marker='o', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Silhouette Score', color='tab:blue')
ax2.plot(range(2,10), sil_scores, marker='x', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title("Elbow Method & Silhouette Score")
plt.show()

kmeans = KMeans(n_clusters = 4, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)
print(df.head())

cluster_summary = df.groupby("Cluster")[features].mean()
print(cluster_summary)
print(df["Cluster"].value_counts())

pca = PCA(n_components = 2)
pca_data = pca.fit_transform(X_scaled)
df["PCA1"], df["PCA2"] = pca_data[:,0],pca_data[:,1]

print(pca_data)
print(df["PCA1"])
print(pca_data[:,1])

n_clusters = df["Cluster"].nunique()
colors = plt.cm.tab10.colors[:n_clusters]
cmap = ListedColormap(colors)

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    df["PCA1"],
    df["PCA2"],
    c=df["Cluster"],
    cmap=cmap,
    alpha=0.7
)

centers_pca = pca.transform(kmeans.cluster_centers_)
plt.scatter(
    centers_pca[:, 0],
    centers_pca[:, 1],
    marker="X",
    s=300,
    c="black",
    label="Centroid"
)

handles, labels = scatter.legend_elements()
plt.legend(
    handles,
    [f"Cluster {i}" for i in range(n_clusters)] + ["Centroid"],
    title="Clusters"
)

plt.title("Customer Segmentation (PCA)")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.show()

print(cluster_summary)