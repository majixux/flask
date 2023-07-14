from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)

# Configuración de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'west_productos'

# Inicializar la extensión MySQL
mysql.init_app(app)

@app.route('/')
def index():
    
    sql = "SELECT * FROM `west_productos`.`productos`;"
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    productos = cursor.fetchall()
    print(productos)
    
    #print("-"*60)
    #for producto in db_productos:
       # print(producto)
    #print("-"*60)
    
    #conn.commit()
    return render_template('productos/index.html', productos=productos)

@app.route('/create')
def create():
    return render_template('productos/create.html')

@app.route('/store', methods=['POST'])
def storage():
    
    _genero=request.form['txtGenero']
    _categoria=request.form['txtCategoria']
    _talle=request.form['txtTalle']
    _precio=request.form['numPrecio']
    _nombre=request.form['txtNombre']
    
    datos = (_genero,_categoria,_talle,_precio,_nombre)
    
    sql = "INSERT INTO `west_productos`.`productos` (`id`, `genero`, `categoria`, `talle`, `precio`, `nombre`) VALUES (NULL, %s, %s, %s, %s, %s);"
    
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return render_template('productos/index.html')
if __name__ == '__main__':
    app.run(debug=True)
