from flask import Flask, request, jsonify
from algorithms import Solution
from tree_node import build_tree
from urllib.parse import quote_plus as url_quote  # Replace with quote_plus if needed

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the root endpoint. Please use /max-path-sum to calculate maximum path sum."

@app.route('/max-path-sum', methods=['POST'])
def max_path_sum():
    data = request.get_json()
    if not data or 'tree' not in data:
        return jsonify({"error": "Invalid input"}), 400
    tree_values = data['tree']
    root = build_tree(tree_values)
    solution = Solution()
    max_sum = solution.maxPathSum(root)
    return jsonify({"max_path_sum": max_sum})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
