# CL University - School Management System

Full-stack school management system with Bakong KHQR payment integration.

## Features
- Student, Lecturer, Staff Management
- Department & Course Management
- Enrollment System
- Bakong KHQR Payment (Real-time QR payment)
- Salary/Payroll Management
- Fee Structure Configuration
- Dashboard with Statistics

## Setup

### Backend (Flask API)
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Backend runs on: http://localhost:5001

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on: http://localhost:3000

## Payment Integration
Uses Bakong KHQR for CL University payments.
- Merchant: CL University
- Location: Phnom Penh
