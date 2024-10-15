import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data from S3 (Assuming data is downloaded locally)
top_domains = pd.read_csv('s3://your-bucket/phishing_data/output/top_domains.csv')

# Visualize Top Phishing Domains
plt.figure(figsize=(12, 6))
sns.barplot(data=top_domains, x='domain', y='count', palette='rocket')
plt.title('Top Phishing Domains')
plt.xlabel('Domain')
plt.ylabel('Number of Attempts')
plt.xticks(rotation=45)
plt.show()
