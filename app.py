from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    domain = request.headers.get('Domain')

    # Execute Subfinder as a subprocess
    cmd = ['./subfinder', '-d', domain]
    try:
        # Change directory to the Subfinder path
        subprocess.call('cd /app/subfinder/v2/cmd/subfinder', shell=True)
        
        # Execute Subfinder command

        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        findings = output.decode('utf-8')

        # TODO: Parse the findings if needed

        return jsonify({'status': 'Scan completed', 'findings': findings}), 200
    except subprocess.CalledProcessError as e:
        error_message = e.output.decode('utf-8')
        return jsonify({'error': 'Scan failed', 'message': error_message}), 500

@app.route('/status/<scan_id>', methods=['GET'])
def status(scan_id):
    # TODO: Check the status of the scan using the scan_id
    # Example: You can maintain a map with scan_id as key and scan status as value

    return jsonify({'status': 'Scan in progress'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

