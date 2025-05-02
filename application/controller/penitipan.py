from flask import Blueprint, request, jsonify, current_app
from bson.objectid import ObjectId
from datetime import datetime, timedelta

penitipan_bp = Blueprint('penitipan', __name__)

@penitipan_bp.route('/', methods=['GET'])
def get_penitipan():
    db = current_app.db
    items = list(db.penitipan.find())
    for item in items:
        item['_id'] = str(item['_id'])
    return jsonify(items)

@penitipan_bp.route('/', methods=['POST'])
def create_penitipan():
    data = request.json
    db = current_app.db

    tarif = data.get('tarif', 0)
    durasi = data.get('durasi_penitipan', 0)
    tanggal_penitipan = datetime.strptime(data.get('tanggal_penitipan'), '%Y-%m-%d')
    tanggal_pengambilan = datetime.strptime(data.get('tanggal_pengambilan'), '%Y-%m-%d')

    expected_return = tanggal_penitipan + timedelta(days=durasi)
    overdue_days = max((tanggal_pengambilan - expected_return).days, 0)
    denda = overdue_days * tarif
    total_biaya = (tarif * durasi) + denda

    data['denda'] = denda
    data['total_biaya'] = total_biaya

    result = db.penitipan.insert_one(data)
    return jsonify({'inserted_id': str(result.inserted_id)}), 201

@penitipan_bp.route('/<id>', methods=['PUT'])
def update_penitipan(id):
    data = request.json
    db = current_app.db

    existing = db.penitipan.find_one({'_id': ObjectId(id)})
    if not existing:
        return jsonify({'message': 'Data tidak ditemukan'}), 404

    tarif = data.get('tarif', existing.get('tarif', 0))
    durasi = data.get('durasi_penitipan', existing.get('durasi_penitipan', 0))

    tanggal_penitipan = data.get('tanggal_penitipan', existing.get('tanggal_penitipan'))
    tanggal_pengambilan = data.get('tanggal_pengambilan', existing.get('tanggal_pengambilan'))

    try:
        tanggal_penitipan = datetime.strptime(tanggal_penitipan, '%Y-%m-%d')
        tanggal_pengambilan = datetime.strptime(tanggal_pengambilan, '%Y-%m-%d')
    except Exception as e:
        return jsonify({'message': 'Format tanggal tidak valid (harus YYYY-MM-DD)'}), 400

    expected_return = tanggal_penitipan + timedelta(days=durasi)
    overdue_days = max((tanggal_pengambilan - expected_return).days, 0)
    denda = overdue_days * tarif
    total_biaya = (tarif * durasi) + denda

    data['denda'] = denda
    data['total_biaya'] = total_biaya

    db.penitipan.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Penitipan updated'})

@penitipan_bp.route('/<id>', methods=['DELETE'])
def delete_penitipan(id):
    db = current_app.db
    db.penitipan.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Penitipan deleted'})
