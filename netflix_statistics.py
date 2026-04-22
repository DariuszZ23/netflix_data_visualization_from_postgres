import re
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
        productions_by_country(cursor)
        netflix_productions_by_type(cursor)
        generate_movie_duration_histogram(cursor)
        generate_titles_per_year_chart(cursor)
        cursor.close()
        connection.close()

    except Exception as e:
        print("Connection error:", e)

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

    plt.xlabel("Country")
    plt.ylabel("Number of production")
    plt.title("Top 10 production country on Netflix")

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

    plt.title("Share of films and series on Netflix")
    plt.show()

def generate_movie_duration_histogram(cursor):
    cursor.execute("""
        SELECT duration
        FROM netflix_titles
        WHERE type = 'Movie'
          AND duration IS NOT NULL
    """)

    results = cursor.fetchall()

    durations = []
    for (duration,) in results:
        match = re.search(r'\d+', duration)
        if match:
            durations.append(int(match.group()))

    # wykres
    plt.figure()
    plt.hist(durations, bins=20, edgecolor='black')
    plt.title("Histogram of film lengths")
    plt.xlabel("Length (minutes)")
    plt.ylabel("Number of films")
    plt.show()

def generate_titles_per_year_chart(cursor):
    cursor.execute("""
        SELECT release_year, COUNT(*) AS total_titles
        FROM netflix_titles
        WHERE release_year IS NOT NULL
        GROUP BY release_year
        ORDER BY release_year
    """)

    results = cursor.fetchall()

    years = [row[0] for row in results]
    counts = [row[1] for row in results]

    # wykres liniowy
    plt.figure()
    plt.plot(years, counts, marker='o')

    plt.title("Number of Netflix productions over time")
    plt.xlabel("Year")
    plt.ylabel("Number of titles")
    plt.show()


if __name__ == '__main__':
    netflix_statistics()
