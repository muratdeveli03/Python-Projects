import pandas as pd

# Örnek veriler
data = {
    'İsim': ['Ahmet', 'Mehmet', 'Ayşe'],
    'Yaş': [25, 30, 28],
    'Şehir': ['İstanbul', 'Ankara', 'İzmir']
}

# DataFrame oluşturma
df = pd.DataFrame(data)

# Verileri CSV dosyasına kaydetme
df.to_csv('veriler.csv', index=False)

# Verileri Excel dosyasına kaydetme
df.to_excel('veriler.xlsx', index=False)

# Verileri JSON dosyasına kaydetme
df.to_json('veriler.json', orient='records')
