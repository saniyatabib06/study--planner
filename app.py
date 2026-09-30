from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        subject = request.form["subject"]
        task = request.form["task"]
        date = request.form["date"]

        tasks.append({
            "subject": subject,
            "task": task,
            "date": date,
            "completed": False
        })

        return redirect("/")

    task_list = ""

    for i, item in enumerate(tasks):
        status = "✅ Completed" if item["completed"] else "⏳ Pending"

        task_list += f"""
        <li>
            <b>{item['subject']}</b> -
            {item['task']} -
            {item['date']} -
            {status}

            <a href="/complete/{i}">Complete</a>
            <a href="/delete/{i}">Delete</a>
        </li>
        """

    return f"""
    <html>
    <head>
        <title>Study Planner</title>
    </head>

    <body>
        <h1>📚 My Study Planner</h1>

        <h2>Add Study Task</h2>

        <form method="POST">
            Subject:
            <input type="text" name="subject" required><br><br>

            Task:
            <input type="text" name="task" required><br><br>

            Date:
            <input type="date" name="date" required><br><br>

            <button type="submit">Add Task</button>
        </form>

        <h2>My Tasks</h2>

        <ul>
            {task_list}
        </ul>

    </body>
    </html>
    """


@app.route("/complete/<int:index>")
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

    return redirect("/")


@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)