from flask import Flask, render_template, request, redirect, url_for
from models.producto_CRUD import ProductoCRUD

app = Flask(__name__)

with app.app_context():
    ProductoCRUD.inicializar_bd()

@app.route('/')
def index():
    productos = ProductoCRUD.listar()
    return render_template('index.html', productos=productos)

@app.route('/guardar', methods=['POST'])
def guardar():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    cantidad = int(request.form['cantidad'])
    ProductoCRUD.insertar(codigo, nombre, precio, cantidad)
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        ProductoCRUD.actualizar(id, codigo, nombre, precio, cantidad)
        return redirect(url_for('index'))
    
    producto = ProductoCRUD.obtener_por_id(id)
    return render_template('editar.html', producto=producto)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    ProductoCRUD.eliminar(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)