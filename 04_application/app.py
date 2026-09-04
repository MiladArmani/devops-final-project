from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)
tasks = {}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(list(tasks.values())), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400
    task_id = str(uuid.uuid4())
    task = {"id": task_id, "title": title, "done": False}
    tasks[task_id] = task
    return jsonify(task), 201

@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(task), 200

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    data = request.get_json(silent=True) or {}
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task), 200

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "not found"}), 404
    del tasks[task_id]
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
