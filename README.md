# Mój pierwszy blog — projekt Flask (Kodilla)

Prosty system blogowy stworzony w ramach kursu Kodilla Bootcamp (Moduł 16).  
Aplikacja pozwala na:
- tworzenie nowych wpisów,
- edytowanie istniejących wpisów,
- oznaczanie wpisów jako opublikowane / szkice,
- podgląd listy szkiców,
- usuwanie wpisów,
- logowanie administratora (wymagane do tworzenia, edycji i usuwania wpisów).

---

## 🚀 Technologie

- Python 3.x  
- Flask  
- Flask-WTF  
- SQLAlchemy  
- Bootstrap 4  
- Jinja2  

---

## 🔧 Uruchomienie projektu

1. Sklonuj repozytorium:
   ```bash
   git clone <adres_repozytorium>
Przejdź do folderu:

bash
Копировать код
cd projekt
Stwórz i aktywuj środowisko wirtualne:

bash
Копировать код
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Zainstaluj zależności:

bash
Копировать код
pip install -r requirements.txt
Uruchom aplikację:

bash
Копировать код
flask run
🔑 Logowanie
Dane logowania są pobierane z pliku config.py lub zmiennych środowiskowych:

ini
Копировать код
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "change-me"
🗂 Funkcjonalności
Widoczne publicznie:
lista wszystkich opublikowanych wpisów

Dostępne po zalogowaniu:
dodawanie nowego wpisu

edytowanie wpisu

usuwanie wpisu

wyświetlanie listy szkiców

ukrywanie szkiców przed publicznością

przyciski logowania / wylogowania w navbarze

🧹 Struktura projektu
arduino
Копировать код
blog/
 ├── templates/
 │    ├── base.html
 │    ├── homepage.html
 │    ├── entry_form.html
 │    ├── drafts.html
 │    └── login_form.html
 ├── routes.py
 ├── models.py
 ├── forms.py
 ├── config.py
 └── __init__.py
✔️ Status
Projekt ukończony zgodnie z wymaganiami modułu 16 na Kodilli.

📌 Autor
Wykonane przez uczestnika kursu Kodilla Bootcamp.


