from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/receive_sec', methods=['POST'])
def receive_sec():
    data = request.json
    bank_account = data['bank_account']
    data = data['converted_sec']
    # Simulate sending sec to bank account
    if bank_account in ['197278463', '20057942287']:
        return jsonify({"status": "success", "message": "Sec sent successfully"})
    else:
        return jsonify({"status": "failure", "message": "Invalid bank account"})

@app.route('/recharge_phone', methods=['POST'])
def recharge_phone():
    data = request.json
    phone_number = data['phone_number']
    data = data['data']
    data = data['airtime']
    # Simulate recharging phone
    if phone_number in ['0630915425', '0781461828', '069926061', '0785880914', '0736457220', '0639807554', '0729518653']:
        return jsonify({"status": "success", "message": "Phone recharged successfully"})
    else:
        return jsonify({"status": "failure", "message": "Invalid phone number"})

@app.route('/voice_command', methods=['POST'])
def voice_command():
    data = request.json
    command = data['command']
    try:
        if "install" in command:
            app_name = command.split("install")[-1].strip()
            subprocess.run(["sudo", "apt-get", "install", app_name])
            return jsonify({"status": "success", "message": f"{app_name} installed successfully"})
        elif "open browser" in command:
            subprocess.run(["open", "-a", "Safari"])  # Change this command according to your OS and browser
            return jsonify({"status": "success", "message": "Browser opened successfully"})
        # Add more voice commands here
        else:
            return jsonify({"status": "failure", "message": "Command not recognized"})
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)



