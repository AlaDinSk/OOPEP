from flask import Blueprint, render_template, request, redirect, flash, jsonify
from flask_login import login_required
from sqlalchemy import desc, cast, Integer
from ..extensions import db
from ..models.post import Post, Operator_db, Holder_db, Unqualified_db, Cancellation_db
from ..models.user import User
from ..functions import extract_text_from_image, extract_name, extract_conditional_name
from flask_wtf import FlaskForm
from wtforms import SelectField
import os
from PIL import Image
import re

post = Blueprint('post', __name__)

@post.route('/', methods=['POST', 'GET'])
def all():
    post = Post.query.order_by(Post.date.desc()).all()
    return render_template('post/all.html', post=post, user=User)

@post.route('/post/operators_table', methods=['POST', 'GET'])
def operators_table():
    operators = Operator_db.query.order_by(cast(Operator_db.item_journal, Integer).desc()).all()
    return render_template('post/operators_table.html', operator_db=operators, user=User)

@post.route('/post/holders_table', methods=['POST', 'GET'])
def holders_table():
    holders = Holder_db.query.order_by(cast(Holder_db.item_journal, Integer).desc()).all()
    return render_template('post/holders_table.html', holder_db=holders, user=User)

@post.route('/post/unqualified_table', methods=['POST', 'GET'])
def unqualified_table():
    unqualified = Unqualified_db.query.order_by(cast(Unqualified_db.item_journal, Integer).desc()).all()
    return render_template('post/unqualified_table.html', unqualified_db=unqualified, user=User)


@post.route('/post/cancellation_table', methods=['POST', 'GET'])
def cancellation_table():
    cancellation = Cancellation_db.query.order_by(cast(Cancellation_db.item_journal, Integer).desc()).all()
    return render_template('post/cancellation_table.html', cancellation_db=cancellation, user=User)

@post.route('/post/operators_add', methods=['POST', 'GET'])
@login_required
def operators_add():
    if request.method == 'POST':
        item_journal = request.form['item_journal']
        conditional_name = request.form['conditional_name']
        valid_name = request.form['valid_name']
        subordination = request.form['subordination']
        out_number = request.form['out_number']
        in_number = request.form['in_number']
        oid = request.form['oid']
        name = request.form['name']
        type_certificate = request.form['type_certificate']
        status = request.form['status']
        electronic_request = request.form['electronic_request']
        release = request.form['release']
        number_notification = request.form['number_notification']
        date_notification = request.form['date_notification']
        return_certificate = request.form['return_certificate']
        filing_case = request.form['filing_case']
        note = request.form['note']

        new_operator = Operator_db(
            item_journal=item_journal,
            conditional_name=conditional_name,
            valid_name=valid_name,
            subordination=subordination,
            out_number=out_number,
            in_number=in_number,
            oid=oid,
            name=name,
            type_certificate=type_certificate,
            status=status,
            electronic_request=electronic_request,
            release=release,
            number_notification=number_notification,
            date_notification=date_notification,
            return_certificate=return_certificate,
            filing_case=filing_case,
            note=note
        )
        try:
            db.session.add(new_operator)
            db.session.commit()
            return redirect('/post/operators_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/operators_add.html')

@post.route('/post/holders_add', methods=['POST', 'GET'])
@login_required
def holders_add():
    if request.method == 'POST':
        item_journal = request.form['item_journal']
        conditional_name = request.form['conditional_name']
        valid_name = request.form['valid_name']
        subordination = request.form['subordination']
        out_number = request.form['out_number']
        in_number = request.form['in_number']
        oid = request.form['oid']
        name = request.form['name']
        status = request.form['status']
        electronic_request = request.form['electronic_request']
        release = request.form['release']
        number_notification = request.form['number_notification']
        date_notification = request.form['date_notification']
        return_certificate = request.form['return_certificate']
        filing_case = request.form['filing_case']
        note = request.form['note']

        new_holder = Holder_db(
            item_journal=item_journal,
            conditional_name=conditional_name,
            valid_name=valid_name,
            subordination=subordination,
            out_number=out_number,
            in_number=in_number,
            oid=oid,
            name=name,
            status=status,
            electronic_request=electronic_request,
            release=release,
            number_notification=number_notification,
            date_notification=date_notification,
            return_certificate=return_certificate,
            filing_case=filing_case,
            note=note
        )
        try:
            db.session.add(new_holder)
            db.session.commit()
            return redirect('/post/holders_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/holders_add.html')

@post.route('/post/unqualified_add', methods=['POST', 'GET'])
@login_required
def unqualified_add():
    if request.method == 'POST':
        item_journal = request.form['item_journal']
        conditional_name = request.form['conditional_name']
        valid_name = request.form['valid_name']
        subordination = request.form['subordination']
        out_number = request.form['out_number']
        in_number = request.form['in_number']
        oid = request.form['oid']
        name = request.form['name']
        status = request.form['status']
        electronic_request = request.form['electronic_request']
        release = request.form['release']
        number_notification = request.form['number_notification']
        date_notification = request.form['date_notification']
        return_certificate = request.form['return_certificate']
        filing_case = request.form['filing_case']
        note = request.form['note']

        new_unqualified = Unqualified_db(
            item_journal=item_journal,
            conditional_name=conditional_name,
            valid_name=valid_name,
            subordination=subordination,
            out_number=out_number,
            in_number=in_number,
            oid=oid,
            name=name,
            status=status,
            electronic_request=electronic_request,
            release=release,
            number_notification=number_notification,
            date_notification=date_notification,
            return_certificate=return_certificate,
            filing_case=filing_case,
            note=note
        )
        try:
            db.session.add(new_unqualified)
            db.session.commit()
            return redirect('/post/unqualified_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/unqualified_add.html')

@post.route('/post/cancellation_add', methods=['POST', 'GET'])
@login_required
def cancellation_add():
    if request.method == 'POST':
        item_journal = request.form['item_journal']
        conditional_name = request.form['conditional_name']
        valid_name = request.form['valid_name']
        subordination = request.form['subordination']
        out_number = request.form['out_number']
        in_number = request.form['in_number']
        oid = request.form['oid']
        name = request.form['name']
        status = request.form['status']
        date_cancellation = request.form['date_cancellation']
        oid_cancellation = request.form['oid_cancellation']
        number_notification = request.form['number_notification']
        date_notification = request.form['date_notification']
        filing_case = request.form['filing_case']
        note = request.form['note']

        new_cancellation = Cancellation_db(
            item_journal=item_journal,
            conditional_name=conditional_name,
            valid_name=valid_name,
            subordination=subordination,
            out_number=out_number,
            in_number=in_number,
            oid=oid,
            name=name,
            status=status,
            date_cancellation=date_cancellation,
            oid_cancellation=oid_cancellation,
            number_notification=number_notification,
            date_notification=date_notification,
            filing_case=filing_case,
            note=note
        )
        try:
            db.session.add(new_cancellation)
            db.session.commit()
            return redirect('/post/cancellation_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/cancellation_add.html')

@post.route('/post/<int:item_journal>/operator_update', methods=['POST', 'GET'])
@login_required
def operator_update(item_journal):
    operator_post = Operator_db.query.get(item_journal)
    if request.method == 'POST':
        operator_post.item_journal = request.form.get('item_journal')
        operator_post.conditional_name = request.form.get('conditional_name')
        operator_post.valid_name = request.form.get('valid_name')
        operator_post.subordination = request.form.get('subordination')
        operator_post.out_number = request.form.get('out_number')
        operator_post.in_number = request.form.get('in_number')
        operator_post.oid = request.form.get('oid')
        operator_post.name = request.form.get('name')
        operator_post.type_certificate = request.form.get('type_certificate')
        operator_post.status = request.form.get('status')
        operator_post.electronic_request = request.form.get('electronic_request')
        operator_post.release = request.form.get('release')
        operator_post.number_notification = request.form.get('number_notification')
        operator_post.date_notification = request.form.get('date_notification')
        operator_post.return_certificate = request.form.get('return_certificate')
        operator_post.filing_case = request.form.get('filing_case')
        operator_post.note = request.form.get('note')
        try:
            db.session.commit()
            return redirect('/post/operators_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/operator_update.html', operator_post=operator_post)

@post.route('/post/<int:item_journal>/holder_update', methods=['POST', 'GET'])
@login_required
def holder_update(item_journal):
    holder = Holder_db.query.get(item_journal)
    if request.method == 'POST':
        holder.item_journal = request.form.get('item_journal')
        holder.conditional_name = request.form.get('conditional_name')
        holder.valid_name = request.form.get('valid_name')
        holder.subordination = request.form.get('subordination')
        holder.out_number = request.form.get('out_number')
        holder.in_number = request.form.get('in_number')
        holder.oid = request.form.get('oid')
        holder.name = request.form.get('name')
        holder.status = request.form.get('status')
        holder.electronic_request = request.form.get('electronic_request')
        holder.release = request.form.get('release')
        holder.number_notification = request.form.get('number_notification')
        holder.date_notification = request.form.get('date_notification')
        holder.return_certificate = request.form.get('return_certificate')
        holder.filing_case = request.form.get('filing_case')
        holder.note = request.form.get('note')
        try:
            db.session.commit()
            return redirect('/post/holders_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/holder_update.html', holder=holder)

@post.route('/post/<int:item_journal>/unqualified_update', methods=['POST', 'GET'])
@login_required
def unqualified_update(item_journal):
    unqualified = Unqualified_db.query.get(item_journal)
    if request.method == 'POST':
        unqualified.item_journal = request.form.get('item_journal')
        unqualified.conditional_name = request.form.get('conditional_name')
        unqualified.valid_name = request.form.get('valid_name')
        unqualified.subordination = request.form.get('subordination')
        unqualified.out_number = request.form.get('out_number')
        unqualified.in_number = request.form.get('in_number')
        unqualified.oid = request.form.get('oid')
        unqualified.name = request.form.get('name')
        unqualified.type_certificate = request.form.get('type_certificate')
        unqualified.status = request.form.get('status')
        unqualified.electronic_request = request.form.get('electronic_request')
        unqualified.release = request.form.get('release')
        unqualified.number_notification = request.form.get('number_notification')
        unqualified.date_notification = request.form.get('date_notification')
        unqualified.return_certificate = request.form.get('return_certificate')
        unqualified.filing_case = request.form.get('filing_case')
        unqualified.note = request.form.get('note')
        try:
            db.session.commit()
            return redirect('/post/unqualified_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/unqualified_update.html', unqualified=unqualified)

@post.route('/post/<int:item_journal>/cancellation_update', methods=['POST', 'GET'])
@login_required
def cancellation_update(item_journal):
    cancellation = Cancellation_db.query.get(item_journal)
    if request.method == 'POST':
        cancellation.item_journal = request.form.get('item_journal')
        cancellation.conditional_name = request.form.get('conditional_name')
        cancellation.valid_name = request.form.get('valid_name')
        cancellation.subordination = request.form.get('subordination')
        cancellation.out_number = request.form.get('out_number')
        cancellation.in_number = request.form.get('in_number')
        cancellation.oid = request.form.get('oid')
        cancellation.name = request.form.get('name')
        cancellation.status = request.form.get('status')
        cancellation.date_cancellation = request.form.get('date_cancellation')
        cancellation.oid_cancellation = request.form.get('oid_cancellation')
        cancellation.number_notification = request.form.get('number_notification')
        cancellation.date_notification = request.form.get('date_notification')
        cancellation.filing_case = request.form.get('filing_case')
        cancellation.note = request.form.get('note')
        try:
            db.session.commit()
            return redirect('/post/cancellation_table')
        except Exception as e:
            return f'Произошла ошибка: {str(e)}'
    else:
        return render_template('post/cancellation_update.html', cancellation=cancellation)

@post.route('/post/upload',  methods=['POST', 'GET'])
def upload_file():
    upload_folder = os.path.join('app', 'static', 'upload')
    if 'file' not in request.files:
        return jsonify({"error": "Файл не выбран"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Файл не выбран"}), 400
    # Сохраняем файл в папку static/upload
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    flash(f"Данные из файла добавлены!", "success")
    # Извлекаем текст из изображения
    text = extract_text_from_image(file_path)
    # Извлекаем данные (name и conditional_name)
    data = {
        "name": extract_name(text),
        "conditional_name": extract_conditional_name(text)
    }
    # Возвращаем данные в формате JSON
    return jsonify(data)
