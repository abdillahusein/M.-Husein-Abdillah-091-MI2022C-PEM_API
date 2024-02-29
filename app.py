from flask import Flask, jsonify, request

app = Flask(__name__)

# Contoh data sementara
tasks = [
    {
        'id': 1,
        'title': 'Belajar Python',
        'description': 'Belajar Python untuk pengembangan web.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Buat REST API',
        'description': 'Buat REST API sederhana menggunakan Flask.',
        'done': False
    }
]

@app.route('/')
def home():
    return 'Selamat datang di aplikasi Flask!'

# Route untuk mendapatkan semua tugas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route untuk mendapatkan sebuah tugas berdasarkan id
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Tugas tidak ditemukan'}), 404
    return jsonify({'task': task[0]})

# Route untuk menambahkan sebuah tugas
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'Data tidak lengkap'}), 400
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Route untuk mengubah status tugas menjadi selesai
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Tugas tidak ditemukan'}), 404
    task[0]['done'] = True
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
