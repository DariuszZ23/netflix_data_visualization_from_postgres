# 🎬 Netflix Data Visualization (PostgreSQL)

Projekt analityczny, którego celem jest eksploracja i wizualizacja danych dotyczących filmów i seriali dostępnych na Netflixie, z wykorzystaniem bazy danych PostgreSQL oraz języka Python.

---

## 📌 Opis projektu

Projekt pobiera dane z bazy danych PostgreSQL i wykonuje zapytania SQL w celu uzyskania interesujących informacji, takich jak:

* Top 10 krajów produkujących najwięcej treści
* Analiza liczby produkcji
* Wizualizacje danych w formie wykresów

Całość została zaprojektowana w sposób modularny, zgodnie z dobrymi praktykami programowania.

---

## 🧱 Struktura projektu

```
project/
│
├── main.py              # Punkt wejścia programu
├── db_connection.py     # Obsługa połączenia z bazą danych
├── queries.py           # Zapytania SQL
└──  config.yaml          # Dane konfiguracyjne (ignorowane przez Git)
```

---

## ⚙️ Wymagania

Zainstaluj wymagane biblioteki:

```
pip install psycopg2-binary pyyaml matplotlib
```

---

## 🔐 Konfiguracja

Utwórz plik `config.yaml` w głównym katalogu projektu:

```yaml
database:
  host: localhost
  port: 5432
  name: postgres
  user: postgres
  password: twoje_haslo
```

---

## 🚀 Uruchomienie

```
python main.py
```

---

## 📊 Przykładowe zapytanie

```sql
SELECT country, COUNT(*) AS total_titles
FROM netflix_titles
WHERE country IS NOT NULL
  AND country != ''
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;
```

---

## 📈 Przykładowe wyniki

```
United States: 3000
India: 1000
United Kingdom: 800
...
```

---

## 🖼️ Wizualizacje

Poniżej przykładowe wykresy wygenerowane w projekcie:

### 📊 Wykres słupkowy – Top 10 krajów

![Figure_1.png](Figure_1.png)

### 🥧 Wykres kołowy – Udział filmów i seriali na Netflixie

![Figure_2.png](Figure_2.png)

## 📊 Histogram długości filmów

Wykres przedstawia rozkład długości filmów dostępnych w bazie danych Netflix.

- Oś X: długość filmu w minutach  
- Oś Y: liczba filmów  

Histogram pozwala szybko zauważyć, w jakich przedziałach czasowych znajduje się najwięcej produkcji. Dzięki temu można określić typową długość filmów oraz zidentyfikować ewentualne wartości odstające.
![Figure_3.png](Figure_3.png)

## 📊 Liczba produkcji w czasie

Wykres liniowy przedstawia liczbę filmów i seriali dodawanych na przestrzeni lat.

- Oś X: rok produkcji (`release_year`)  
- Oś Y: liczba tytułów  

Dzięki temu wykresowi można zaobserwować dynamikę rozwoju biblioteki Netflixa oraz okresy największego wzrostu liczby dostępnych produkcji.

![Figure_4.png](Figure_4.png)
---

## 🧠 Technologie

* Python
* PostgreSQL
* SQL
* YAML
* Matplotlib

---

## 💡 Możliwe rozszerzenia

* Analiza gatunków filmów
* Analiza trendów w czasie
* Dashboard (np. Streamlit)
* API do pobierania danych

---

## 👨‍💻 Autor

Dariusz Zerynger
Projekt wykonany w celach edukacyjnych oraz jako element portfolio.

---
