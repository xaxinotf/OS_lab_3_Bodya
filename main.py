import math
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

filename = "analLisysSysRounded.txt"

try:
    with open(filename) as f:
        res = [line.rstrip() for line in f]
except FileNotFoundError:
    print(f"File {filename} not found.")
    exit()

sizes = []
freqs = []
for line in res:
    size, freq = line.split(' ')
    sizes.append(size)
    freqs.append(int(freq))

# Convert sizes to log scale for some plots
log_freqs = [math.log10(freq) for freq in freqs if freq > 0]

# Pie Chart
def autopct(pct):
    return ('%.2f%%' % pct) if pct > 5 else ''

def get_labels():
    labels = []
    for i, size in enumerate(sizes):
        if freqs[i] > sum(freqs) * 0.05:
            labels.append(f">{size}b")
        else:
            labels.append('')
    return labels

colors = sns.color_palette("pastel", n_colors=len(set(sizes)), desat=0.9)
plt.pie(freqs, labels=get_labels(), autopct=autopct, colors=colors)
plt.legend([f"size > {i}" for i in sizes], loc="best", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

# Log Size Plot
log_sizes = [f"10^{int(math.log10(int(size)))}" if size != '0' else '' for size in sizes]
plt.figure(figsize=(10, 6))
plt.plot(log_sizes, freqs, marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45)
plt.xlabel('Log Size')
plt.ylabel('Frequency')
plt.title('Log Size Distribution')
plt.tight_layout()
plt.show()

# Histogram of Frequencies
plt.figure(figsize=(10, 6))
plt.hist(log_freqs, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Log Frequency')
plt.ylabel('Count')
plt.title('Histogram of Log Frequencies')
plt.tight_layout()
plt.show()

# Boxplot for Frequencies
plt.figure(figsize=(10, 6))
sns.boxplot(data=log_freqs, orient="h", palette="pastel")
plt.xlabel('Log Frequency')
plt.title('Boxplot of Log Frequencies')
plt.tight_layout()
plt.show()

# CDF of File Sizes
sorted_freqs = np.sort(freqs)
cdf = np.arange(1, len(sorted_freqs)+1) / len(sorted_freqs)
plt.figure(figsize=(10, 6))
plt.plot(sorted_freqs, cdf, marker='.', linestyle='none')
plt.xlabel('File Size Frequency')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function of File Size Frequencies')
plt.tight_layout()
plt.show()
