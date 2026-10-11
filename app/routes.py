from flask import Blueprint, request, jsonify
from app.database import addNewCustomer, getAllCustomers
from ai_service import talkWithAI

api_blueprint = Blueprint('api_blueprint', __name__)

@api_blueprint.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    text = data.get('mesaj')
    
    if not text:
        return jsonify({'basari': False, 'hata': 'Mesaj boş olamaz.'}), 400
        
    response = talkWithAI(text)
    return jsonify({'basari': True, 'cevap': response})

@api_blueprint.route('/leads', methods=['POST'])
def addLead():
    data = request.json or {}
    
    # İstediğiniz veri isimlendirmeleri (name, email, phone, message)
    name = data.get('name')
    email = data.get('email', '')
    phone = data.get('phone', '') 
    message = data.get('message', '')
    
    # İsim ve mesaj alanlarını zorunlu kılıyoruz
    if not name or not message:
        return jsonify({'error': 'İsim ve mesaj alanları zorunludur.'}), 400
        
    # Veritabanına kaydetme işlemi
    addNewCustomer(name, email, phone, message)
    return jsonify({'basari': True, 'message': 'Kayıt başarıyla oluşturuldu'})

@api_blueprint.route('/leads', methods=['GET'])
def getLeads():
    # Hiçbir limit veya arama parametresi olmadan tüm veriyi çek
    customers = getAllCustomers()
    return jsonify({'basari': True, 'toplam': len(customers), 'leads': customers})
