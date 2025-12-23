from flask import Flask, request, jsonify
from flask_cors import CORS
from bakong_khqr import KHQR
import json
import uuid
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Bakong KHQR Configuration - CL University
BAKONG_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoiMmVhMmY0NWUzMmE5NDY5OCJ9LCJpYXQiOjE3NjYxNDY1MjMsImV4cCI6MTc3MzkyMjUyM30.06L0xglmHehAEPDPm7qdtAu6UCrCVid4dj9FDH8oykE"
BANK_ACCOUNT = "hut_soksitchey1@aclb"
MERCHANT_NAME = "CL University"
MERCHANT_CITY = "Phnom Penh"
PHONE_NUMBER = "855977416126"

khqr = KHQR(BAKONG_TOKEN)

DATA_FILE = 'data/school_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'students': [], 'lecturers': [], 'staff': [], 'courses': [],
        'departments': [], 'payments': [], 'salaries': [], 'enrollments': [],
        'fees': {'tuition_per_credit': 50, 'registration_fee': 100, 'library_fee': 25, 'lab_fee': 50, 'graduation_fee': 200}
    }

def save_data(data):
    os.makedirs('data', exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, default=str)

school_data = load_data()

# ==================== STUDENTS ====================
@app.route('/api/students', methods=['GET', 'POST'])
def students():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['students']})
    data = request.json
    student = {
        'id': str(uuid.uuid4()),
        'student_id': f"STU{datetime.now().strftime('%Y')}{len(school_data['students'])+1:04d}",
        'first_name': data.get('first_name'), 'last_name': data.get('last_name'),
        'email': data.get('email'), 'phone': data.get('phone'),
        'date_of_birth': data.get('date_of_birth'), 'gender': data.get('gender'),
        'address': data.get('address'), 'department_id': data.get('department_id'),
        'status': 'active', 'created_at': datetime.now().isoformat()
    }
    school_data['students'].append(student)
    save_data(school_data)
    return jsonify({'success': True, 'data': student})

@app.route('/api/students/<id>', methods=['PUT', 'DELETE'])
def student_detail(id):
    global school_data
    if request.method == 'DELETE':
        school_data['students'] = [s for s in school_data['students'] if s['id'] != id]
        save_data(school_data)
        return jsonify({'success': True})
    data = request.json
    for i, s in enumerate(school_data['students']):
        if s['id'] == id:
            school_data['students'][i].update(data)
            save_data(school_data)
            return jsonify({'success': True, 'data': school_data['students'][i]})
    return jsonify({'success': False, 'error': 'Not found'}), 404


# ==================== LECTURERS ====================
@app.route('/api/lecturers', methods=['GET', 'POST'])
def lecturers():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['lecturers']})
    data = request.json
    lecturer = {
        'id': str(uuid.uuid4()),
        'lecturer_id': f"LEC{datetime.now().strftime('%Y')}{len(school_data['lecturers'])+1:04d}",
        'first_name': data.get('first_name'), 'last_name': data.get('last_name'),
        'email': data.get('email'), 'phone': data.get('phone'),
        'qualification': data.get('qualification'), 'specialization': data.get('specialization'),
        'department_id': data.get('department_id'), 'salary': data.get('salary', 0),
        'status': 'active', 'created_at': datetime.now().isoformat()
    }
    school_data['lecturers'].append(lecturer)
    save_data(school_data)
    return jsonify({'success': True, 'data': lecturer})

@app.route('/api/lecturers/<id>', methods=['PUT', 'DELETE'])
def lecturer_detail(id):
    global school_data
    if request.method == 'DELETE':
        school_data['lecturers'] = [l for l in school_data['lecturers'] if l['id'] != id]
        save_data(school_data)
        return jsonify({'success': True})
    data = request.json
    for i, l in enumerate(school_data['lecturers']):
        if l['id'] == id:
            school_data['lecturers'][i].update(data)
            save_data(school_data)
            return jsonify({'success': True, 'data': school_data['lecturers'][i]})
    return jsonify({'success': False, 'error': 'Not found'}), 404

# ==================== STAFF ====================
@app.route('/api/staff', methods=['GET', 'POST'])
def staff():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['staff']})
    data = request.json
    member = {
        'id': str(uuid.uuid4()),
        'staff_id': f"STF{datetime.now().strftime('%Y')}{len(school_data['staff'])+1:04d}",
        'first_name': data.get('first_name'), 'last_name': data.get('last_name'),
        'email': data.get('email'), 'phone': data.get('phone'),
        'position': data.get('position'), 'department_id': data.get('department_id'),
        'salary': data.get('salary', 0), 'status': 'active', 'created_at': datetime.now().isoformat()
    }
    school_data['staff'].append(member)
    save_data(school_data)
    return jsonify({'success': True, 'data': member})

@app.route('/api/staff/<id>', methods=['PUT', 'DELETE'])
def staff_detail(id):
    global school_data
    if request.method == 'DELETE':
        school_data['staff'] = [s for s in school_data['staff'] if s['id'] != id]
        save_data(school_data)
        return jsonify({'success': True})
    data = request.json
    for i, s in enumerate(school_data['staff']):
        if s['id'] == id:
            school_data['staff'][i].update(data)
            save_data(school_data)
            return jsonify({'success': True, 'data': school_data['staff'][i]})
    return jsonify({'success': False, 'error': 'Not found'}), 404

# ==================== DEPARTMENTS ====================
@app.route('/api/departments', methods=['GET', 'POST'])
def departments():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['departments']})
    data = request.json
    dept = {
        'id': str(uuid.uuid4()), 'code': data.get('code'), 'name': data.get('name'),
        'description': data.get('description'), 'created_at': datetime.now().isoformat()
    }
    school_data['departments'].append(dept)
    save_data(school_data)
    return jsonify({'success': True, 'data': dept})

# ==================== COURSES ====================
@app.route('/api/courses', methods=['GET', 'POST'])
def courses():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['courses']})
    data = request.json
    course = {
        'id': str(uuid.uuid4()), 'code': data.get('code'), 'name': data.get('name'),
        'credits': data.get('credits', 3), 'department_id': data.get('department_id'),
        'lecturer_id': data.get('lecturer_id'), 'fee_per_credit': data.get('fee_per_credit', 50),
        'created_at': datetime.now().isoformat()
    }
    school_data['courses'].append(course)
    save_data(school_data)
    return jsonify({'success': True, 'data': course})

# ==================== ENROLLMENTS ====================
@app.route('/api/enrollments', methods=['GET', 'POST'])
def enrollments():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['enrollments']})
    data = request.json
    course = next((c for c in school_data['courses'] if c['id'] == data.get('course_id')), None)
    fee = course['credits'] * course.get('fee_per_credit', 50) if course else 0
    enrollment = {
        'id': str(uuid.uuid4()), 'student_id': data.get('student_id'),
        'course_id': data.get('course_id'), 'semester': data.get('semester'),
        'year': data.get('year', datetime.now().year), 'fee': fee,
        'paid': False, 'created_at': datetime.now().isoformat()
    }
    school_data['enrollments'].append(enrollment)
    save_data(school_data)
    return jsonify({'success': True, 'data': enrollment})


# ==================== PAYMENTS (Bakong KHQR) ====================
@app.route('/api/payments', methods=['GET'])
def get_payments():
    return jsonify({'success': True, 'data': school_data['payments']})

@app.route('/api/payments/generate-qr', methods=['POST'])
def generate_payment_qr():
    data = request.json
    amount = data.get('amount', 0)
    payment_type = data.get('payment_type', 'tuition')
    student_id = data.get('student_id')
    currency = data.get('currency', 'USD')
    bill_number = f"CLU{datetime.now().strftime('%Y%m%d%H%M%S')}{len(school_data['payments'])+1:04d}"
    
    print(f"Generating QR: amount={amount}, currency={currency}, student={student_id}")
    
    try:
        # Create QR data
        qr_data = khqr.create_qr(
            bank_account=BANK_ACCOUNT, 
            merchant_name=MERCHANT_NAME,
            merchant_city=MERCHANT_CITY, 
            amount=float(amount), 
            currency=currency,
            store_label='CL University', 
            phone_number=PHONE_NUMBER,
            bill_number=bill_number, 
            terminal_label='Payment-Portal', 
            static=False
        )
        print(f"QR Data created: {qr_data[:50]}...")
        
        # Generate MD5 hash
        md5 = khqr.generate_md5(qr_data)
        print(f"MD5: {md5}")
        
        # Generate QR image
        qr_image = khqr.qr_image(qr_data, format='base64')
        print(f"QR Image generated, length: {len(qr_image) if qr_image else 0}")
        
        payment = {
            'id': str(uuid.uuid4()), 'bill_number': bill_number, 'student_id': student_id,
            'amount': float(amount), 'currency': currency, 'payment_type': payment_type,
            'md5': md5, 'status': 'pending', 'created_at': datetime.now().isoformat()
        }
        school_data['payments'].append(payment)
        save_data(school_data)
        
        return jsonify({
            'success': True, 
            'qr_data': qr_data, 
            'md5': md5, 
            'qr_image': qr_image, 
            'bill_number': bill_number,
            'amount': float(amount),
            'currency': currency
        })
    except Exception as e:
        import traceback
        print(f"Error generating QR: {e}")
        print(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/payments/check', methods=['POST'])
def check_payment():
    data = request.json
    md5 = data.get('md5', '')
    try:
        status = khqr.check_payment(md5)
        is_paid = status == 'PAID'
        if is_paid:
            for i, p in enumerate(school_data['payments']):
                if p['md5'] == md5:
                    school_data['payments'][i]['status'] = 'paid'
                    school_data['payments'][i]['paid_at'] = datetime.now().isoformat()
                    save_data(school_data)
                    break
        return jsonify({'success': True, 'status': status, 'paid': is_paid})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== SALARIES ====================
@app.route('/api/salaries', methods=['GET'])
def get_salaries():
    return jsonify({'success': True, 'data': school_data['salaries']})

@app.route('/api/salaries/generate-payroll', methods=['POST'])
def generate_payroll():
    data = request.json
    month, year = data.get('month', datetime.now().month), data.get('year', datetime.now().year)
    payroll = []
    
    for emp in school_data['lecturers'] + school_data['staff']:
        if emp.get('status') == 'active':
            salary = {
                'id': str(uuid.uuid4()), 'employee_id': emp['id'],
                'employee_type': 'lecturer' if 'lecturer_id' in emp else 'staff',
                'employee_name': f"{emp['first_name']} {emp['last_name']}",
                'amount': emp.get('salary', 0), 'month': month, 'year': year,
                'status': 'pending', 'created_at': datetime.now().isoformat()
            }
            school_data['salaries'].append(salary)
            payroll.append(salary)
    save_data(school_data)
    return jsonify({'success': True, 'data': payroll})

@app.route('/api/salaries/<id>/pay', methods=['POST'])
def pay_salary(id):
    for i, s in enumerate(school_data['salaries']):
        if s['id'] == id:
            school_data['salaries'][i]['status'] = 'paid'
            school_data['salaries'][i]['paid_at'] = datetime.now().isoformat()
            save_data(school_data)
            return jsonify({'success': True, 'data': school_data['salaries'][i]})
    return jsonify({'success': False, 'error': 'Not found'}), 404

# ==================== FEES ====================
@app.route('/api/fees', methods=['GET', 'PUT'])
def fees():
    global school_data
    if request.method == 'GET':
        return jsonify({'success': True, 'data': school_data['fees']})
    school_data['fees'].update(request.json)
    save_data(school_data)
    return jsonify({'success': True, 'data': school_data['fees']})

# ==================== DASHBOARD ====================
@app.route('/api/dashboard/stats', methods=['GET'])
def dashboard_stats():
    return jsonify({'success': True, 'data': {
        'total_students': len([s for s in school_data['students'] if s['status'] == 'active']),
        'total_lecturers': len([l for l in school_data['lecturers'] if l['status'] == 'active']),
        'total_staff': len([s for s in school_data['staff'] if s['status'] == 'active']),
        'total_courses': len(school_data['courses']),
        'total_departments': len(school_data['departments']),
        'total_payments': sum(p['amount'] for p in school_data['payments'] if p['status'] == 'paid'),
        'pending_payments': sum(p['amount'] for p in school_data['payments'] if p['status'] == 'pending'),
        'total_salaries_paid': sum(s['amount'] for s in school_data['salaries'] if s['status'] == 'paid'),
        'pending_salaries': sum(s['amount'] for s in school_data['salaries'] if s['status'] == 'pending')
    }})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'school': 'CL University'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
