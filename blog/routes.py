# blog/routes.py

from flask import render_template, request, redirect, url_for
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm


@app.route("/")
def index():
    all_posts = Entry.query.order_by(Entry.pub_date.desc()).all()
    return render_template("homepage.html", all_posts=all_posts)


# --- Допоміжна функція для створення / редагування --- #

def _handle_entry(entry=None):
    """Спільна логіка для створення та редагування запису."""
    # якщо entry не передали – створюємо новий об'єкт
    is_new = entry is None
    if is_new:
        entry = Entry()

    # форма заповнюється існуючим об'єктом (або порожнім, якщо новий)
    form = EntryForm(obj=entry)
    errors = None

    if form.validate_on_submit():
        # переносимо дані з форми в об'єкт entry
        form.populate_obj(entry)

        if is_new:
            db.session.add(entry)

        db.session.commit()
        return redirect(url_for("index"))
    else:
        errors = form.errors

    return render_template("entry_form.html", form=form, errors=errors)


# --- Створення запису --- #

@app.route("/add", methods=["GET", "POST"])
def create_entry():
    return _handle_entry()      # без entry → створення нового


# --- Редагування запису --- #

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    return _handle_entry(entry)  # передаємо існуючий запис
