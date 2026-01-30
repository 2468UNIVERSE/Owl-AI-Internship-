from flask import Flask, request, jsonify
import mysql.connector

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)

# -----------------------------
# MySQL Configuration
# -----------------------------
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "MagicBabita@#?24",
    "database": "flask_crud_api"
}

# -----------------------------
# Database Connection
# -----------------------------
def get_db_connection():
    return mysql.connector.connect(**db_config)

# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Flask Task API is running",
        "endpoints": {
            "GET": "/tasks",
            "POST": "/tasks",
            "GET_ONE": "/tasks/<id>",
            "PUT": "/tasks/<id>",
            "DELETE": "/tasks/<id>"
        }
    })


# -----------------------------
# CREATE TASK
# -----------------------------
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Task title is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)",
        (data["title"],)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Task created successfully"}), 201

# -----------------------------
# GET ALL TASKS
# -----------------------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(tasks), 200

# -----------------------------
# GET SINGLE TASK
# -----------------------------
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    cursor.close()
    conn.close()

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200

# -----------------------------
# UPDATE TASK
# -----------------------------
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    if not task:
        cursor.close()
        conn.close()
        return jsonify({"error": "Task not found"}), 404

    title = data.get("title", task["title"])
    completed = data.get("completed", task["completed"])

    cursor.execute(
        "UPDATE tasks SET title = %s, completed = %s WHERE id = %s",
        (title, completed, task_id)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Task updated successfully"}), 200

# -----------------------------
# DELETE TASK
# -----------------------------
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM tasks WHERE id = %s", (task_id,))
    task = cursor.fetchone()

    if not task:
        cursor.close()
        conn.close()
        return jsonify({"error": "Task not found"}), 404

    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
