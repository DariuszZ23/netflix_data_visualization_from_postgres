import psycopg2
import yaml
import matplotlib.pyplot as plt

def netflix_statistics():
    # Wczytanie konfiguracji z YAML
    with open("config_local.yaml", "r") as file:
        config = yaml.safe_load(file)

    db_config = config["database"]

    try:
        # Połączenie z PostgreSQL
        connection = psycopg2.connect(
            host=db_config["host"],
            port=db_config["port"],
            dbname=db_config["name"],
            user=db_config["user"],
            password=db_config["password"]
        )

        cursor = connection.cursor()
        # Testowe zapytanie
        cursor.execute("SELECT version();")
        result = cursor.fetchone()
        print("Wersja PostgreSQL:", result)

        productions_by_country(cursor)
        netflix_productions_by_type(cursor)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Błąd połączenia:", e)

def productions_by_country(cursor):
    # top 10 krajów produkcji
    cursor.execute("""
                    SELECT country, COUNT(*) AS total_titles
                   FROM netflix_titles
                   WHERE country IS NOT NULL
                     AND country != ''
                   GROUP BY country
                   ORDER BY total_titles DESC
                       LIMIT 10;
                    """)

    results = cursor.fetchall()

    countries = []
    totals = []

    for country, total in results:
        countries.append(country)
        totals.append(total)

    plt.figure(figsize=(12, 6))
    plt.bar(countries, totals)

    plt.xlabel("Kraj")
    plt.ylabel("Liczba produkcji")
    plt.title("10 najpopularniejszych krajów produkcji na Netflix")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()

def netflix_productions_by_type(cursor):
    # ilość filmów (movies) i seriali
    cursor.execute("""
                   SELECT type, COUNT(*)
                   FROM netflix_titles
                   GROUP BY type;
                   """)

    results = cursor.fetchall()

    labels = []
    sizes = []

    for row in results:
        labels.append(row[0])
        sizes.append(row[1])

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.title("Udział filmów i seriali na Netflix")
    plt.show()

if __name__ == '__main__':
    netflix_statistics()
