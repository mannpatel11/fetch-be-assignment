from flask import Flask, request, jsonify 
from collections import defaultdict, deque
from datetime import datetime

app = Flask(__name__)

transactions = []
payer_balance = defaultdict(int)

def add_transaction(payer, points, timestamp):
    timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    transactions.append({'payer': payer, 'points': points, 'timestamp': timestamp})
    payer_balance[payer] += points

@app.route('/add', methods = ['POST'])
def add_points():
    data = request.get_json()
    payer = data['payer']
    points = data['points']
    timestamp = data['timestamp']

    add_transaction(payer, points, timestamp)
    return '', 200

@app.route('/spend', methods = ['POST'])
def spend_points():
    data = request.get_json()
    points_to_spend = data['points']
    
    total_points = sum(payer_balance.values())
    if points_to_spend > total_points:
        return 'Error: Not enough points', 400

    spent_points = defaultdict(int)
    remaining_points = points_to_spend

    sorted_transactions = sorted(transactions, key=lambda x: x['timestamp'])


    for transaction in sorted_transactions:
        if remaining_points <= 0:
            break
        
        payer = transaction['payer']
        points_available = transaction['points']
        points_to_deduct = min(abs(points_available), remaining_points)

        if points_available > 0:
            spent_points[payer] += points_to_deduct
            payer_balance[payer] -= points_to_deduct
            remaining_points -= points_to_deduct
        else:
            payer_balance[payer] += points_to_deduct
            remaining_points += points_to_deduct

    result = [{'payer': payer, 'points': -points} for payer, points in spent_points.items()]
    return jsonify(result), 200

@app.route('/balance', methods = ['GET'])
def get_balance():
    return jsonify(dict(payer_balance)), 200

if __name__ == '__main__':
    app.run(port=8000)
