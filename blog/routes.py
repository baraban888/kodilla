# blog/routes.py
import functools
from flask import render_template, request, redirect, url_for, session, flash
from blog import app, db
from blog.models import Entry
from blog.forms import EntryForm, LoginForm

def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        # якщо залогінений – запускаємо оригінальний view
        if session.get("logged_in"):
            return view_func(*args, **kwargs)

        # якщо ні – запам’ятати, звідки прийшли, і редірект на /login
        next_url = request.path
        return redirect(url_for("login", next=next_url))

    return check_permissions

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
@login_required
def create_entry():
    return _handle_entry()

# --- Редагування запису --- #

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()
    return _handle_entry(entry)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get("next")

    if request.method == "POST":
        if form.validate_on_submit():
            session.permanent = True   # сессионный cookie долгоживущий
            session["logged_in"] = True
            flash("You are now logged in.", "success")
            return redirect(next_url or url_for("index"))
        else:
            errors = form.errors

    return render_template("login_form.html", form=form, errors=errors)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "POST":
        session.clear()
        flash("You are now logged out.", "success")
        return redirect(url_for("index"))
    return redirect(url_for("index"))

@app.route("/drafts/")
@login_required
def list_drafts():
    drafts = Entry.query.filter_by(is_published=False).order_by(Entry.pub_date.desc()).all()
    return render_template("drafts.html", drafts=drafts)

@app.route("/delete/<int:entry_id>", methods=["POST"])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first_or_404()

    db.session.delete(entry)
    db.session.commit()

    flash("Wpis zostal usuniety.", "success")
    return redirect(url_for("index"))
