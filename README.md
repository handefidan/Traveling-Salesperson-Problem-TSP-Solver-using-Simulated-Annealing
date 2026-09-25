# Traveling Salesperson Problem (TSP) Solver using Simulated Annealing
### Simüle Edilmiş Tavlama (Simulated Annealing) ile Gezgin Satıcı Problemi Çözücü

---

## 🇹🇷 Türkçe Açıklama

Bu proje, **Gezgin Satıcı Problemi**'ni (Traveling Salesperson Problem - TSP) çözmek için **En Yakın Komşu** (Nearest Neighbor) başlangıç sezgiseli ve **Simüle Edilmiş Tavlama** (Simulated Annealing) optimizasyon algoritmasını kullanan bir Python uygulamasıdır.

### 📌 Özellikler
- **Nearest Neighbor Başlangıcı:** Algoritmaya rastgele bir başlangıç yerine sezgisel olarak güçlü bir ilk rota sunar.
- **2-Opt Hamleleri:** Rota üzerinde çapraz kesişimleri çözmek için komşuluk aramasında 2-Opt yer değiştirme mantığı kullanılır.
- **Hızlı Delta Hesabı:** Tüm rotayı baştan hesaplamak yerine yalnızca değişen kenarların farkı alınarak yüksek iterasyon performansı sağlanır.
- **Zaman Sınırı & Soğutma:** Algoritma belirlenen süreye veya minimum soğuma eşiğine göre kontrollü çalışır.
- **Görselleştirme:** Matplotlib ile en iyi rotayı 2B koordinat düzleminde çizer.

### 🚀 Gereksinimler & Kurulum
Projeyi çalıştırmadan önce gerekli Python kütüphanelerini yükleyin:

```bash
pip install numpy pandas matplotlib
```

### 📁 Veri Formatı
Program, varsayılan olarak `coordinates.csv` isimli bir dosyayı okur. Dosya boşlukla, sekmeyle veya virgülle ayrılmış 3 sütun içermelidir:
```text
ID X Y
1 15.2 34.5
2 45.0 20.1
3 80.4 65.2
```

### ⚙️ Ayarlar
Kodun en üst kısmında yer alan parametreleri kendi veri setinize göre özelleştirebilirsiniz:
```python
DOSYA_ADI = 'coordinates.csv'  # Koordinat veri dosyası
ZAMAN_SINIRI = 4000            # Saniye cinsinden maksimum çalışma süresi
BASLANGIC_SICAKLIK = 5000.0    # Başlangıç sıcaklığı
SOGUTMA_ORANI = 0.9999999      # Geometrik soğuma katsayısı
```

### ▶️ Çalıştırma
```bash
python main.py
```

---

## 🇬🇧 English Description

This project provides a Python-based solver for the **Traveling Salesperson Problem (TSP)** using a hybrid heuristic approach: a **Nearest Neighbor** initialization followed by **Simulated Annealing** optimization.

### 📌 Features
- **Nearest Neighbor Initialization:** Boots up the search from a greedy initial tour instead of a completely random permutation.
- **2-Opt Local Search:** Employs 2-Opt edge swaps to untangle crossing paths and explore neighbor solutions.
- **Fast Delta Calculation:** Evaluates moves dynamically using local edge differences rather than recomputing the full cycle, maximizing iteration throughput.
- **Configurable Stopping Criteria:** Controlled by execution time limits and minimum temperature thresholds.
- **Plotting & Visualization:** Displays the optimal generated tour on a 2D plane with Matplotlib.

### 🚀 Requirements & Installation
Install the necessary Python packages before execution:

```bash
pip install numpy pandas matplotlib
```

### 📁 Data Format
The script expects a file named `coordinates.csv` by default. It supports space-, tab-, or comma-separated columns with the following structure:
```text
ID X Y
1 15.2 34.5
2 45.0 20.1
3 80.4 65.2
```

### ⚙️ Configuration
You can tweak the main hyperparameters at the top of the script:
```python
DOSYA_ADI = 'coordinates.csv'  # Input coordinates filename
ZAMAN_SINIRI = 4000            # Execution time cutoff in seconds
BASLANGIC_SICAKLIK = 5000.0    # Initial annealing temperature
SOGUTMA_ORANI = 0.9999999      # Geometric cooling rate
```

### ▶️ How to Run
```bash
python main.py
```

---
### 📄 License
This project is open-source and available under the [MIT License](LICENSE).
