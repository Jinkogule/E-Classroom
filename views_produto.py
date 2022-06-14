from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from app import app, db
from models import Produtos
from helpers import recupera_imagem, deleta_arquivo, FormularioProduto
import time


@app.route('/')
def index():
    lista = Produtos.query.order_by(Produtos.id)
    return render_template('lista.html', titulo='Produtos', produtos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioProduto()
    return render_template('novo.html', titulo='Novo Produto', form=form)

@app.route('/criar', methods=['POST',])
def criar():
    form = FormularioProduto(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    valor = form.valor.data

    produto = Produtos.query.filter_by(nome=nome).first()

    if produto:
        flash('Produto já existente!')
        return redirect(url_for('index'))

    novo_produto = Produtos(nome=nome, categoria=categoria, valor=valor)
    db.session.add(novo_produto)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{novo_produto.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    produto = Produtos.query.filter_by(id=id).first()
    form = FormularioProduto()
    form.nome.data = produto.nome
    form.categoria.data = produto.categoria
    form.valor.data = produto.valor
    capa_produto = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Produto', id=id, capa_produto=capa_produto, form=form)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioProduto(request.form)

    if form.validate_on_submit():
        produto = Produtos.query.filter_by(id=request.form['id']).first()
        produto.nome = form.nome.data
        produto.categoria = form.categoria.data
        produto.valor = form.valor.data

        db.session.add(produto)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_arquivo(id)
        arquivo.save(f'{upload_path}/capa{produto.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Produtos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Produto deletado com sucesso!')

    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)