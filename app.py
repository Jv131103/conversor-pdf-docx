import os
import shutil
from tempfile import mkdtemp

from flask import Flask, flash, render_template, send_file
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from utils import docx_to_pdf, pdf_to_docx, secret

app = Flask(__name__)
app.config['SECRET_KEY'] = secret.gerar_chave_secreta()


class ConvertFileForm(FlaskForm):
    arquivo_original = FileField('Arquivo original', validators=[FileRequired()])
    arquivo_gerado = StringField('Nome do arquivo gerado', validators=[DataRequired()])
    submit = SubmitField('Converter')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ConvertFileForm()
    if form.validate_on_submit():
        arquivo = form.arquivo_original.data
        nome_saida = form.arquivo_gerado.data.strip()

        if not nome_saida:
            flash("Por favor, insira um nome para o arquivo gerado.", "error")
            return render_template('index.html', form=form)

        # Cria pasta temporária isolada para upload e conversão
        temp_dir = mkdtemp()

        try:
            # Salva arquivo enviado com nome seguro
            filename = secure_filename(arquivo.filename)
            caminho_upload = os.path.join(temp_dir, filename)
            arquivo.save(caminho_upload)

            ext_input = filename.lower().split('.')[-1]
            nome_saida_com_ext = ''
            caminho_saida = ''

            if ext_input in ['docx', 'odt']:
                nome_saida_com_ext = nome_saida + '.pdf'
                caminho_saida = os.path.join(temp_dir, nome_saida_com_ext)
                conversor = docx_to_pdf.ConvertDocxToPdf(caminho_upload, caminho_saida)
                sucesso = conversor.convert_to_pdf()
                if not sucesso:
                    flash("Erro na conversão DOCX→PDF.", "error")
                    return render_template('index.html', form=form)

            elif ext_input == 'pdf':
                nome_saida_com_ext = nome_saida + '.docx'
                caminho_saida = os.path.join(temp_dir, nome_saida_com_ext)
                conversor = pdf_to_docx.ConvertPdfToDocx(caminho_upload, caminho_saida)
                sucesso = conversor.execute_conversor()
                if not sucesso:
                    flash("Erro na conversão PDF→DOCX.", "error")
                    return render_template('index.html', form=form)

            else:
                flash("Extensão de arquivo não suportada. Use .docx, .odt ou .pdf.", "error")
                return render_template('index.html', form=form)

            # Se chegou aqui, conversão foi bem sucedida -> envia para download
            return send_file(
                caminho_saida,
                as_attachment=True,
                download_name=nome_saida_com_ext,
                mimetype='application/octet-stream'
            )

        finally:
            # Limpa pasta temporária e arquivos
            shutil.rmtree(temp_dir, ignore_errors=True)

    return render_template('index.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
