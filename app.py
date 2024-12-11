# Mengimpor Flask dan fungsi-fungsi lain yang diperlukan
from flask import Flask, render_template, request

# Membuat aplikasi Flask
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Menampilkan halaman 'index.html' saat membuka halaman utama
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Mengambil data 'name' yang diisi pengguna di form
    name = request.form.get('name')
    # Menampilkan pesan sapaan menggunakan nama yang diambil
    return f"Hello, {name}!"

# Menjalankan aplikasi jika file ini dieksekusi langsung
if __name__ == '__main__':
    # Menjalankan aplikasi Flask dengan mode debug aktif
    app.run(debug=True)



