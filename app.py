from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML ইন্টারফেস (বাটন এবং ডিসপ্লে বক্স সহ)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker CI/CD Demo</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
        .container { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        input { padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 200px; }
        button { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 20px; font-weight: bold; color: #28a745; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Docker CI/CD App 🚀</h1>
        <form method="POST">
            <input type="text" name="user_input" placeholder="আপনার নাম লিখুন..." required>
            <button type="submit">Submit</button>
        </form>
        {% if display_text %}
            <div class="result">Display Box: {{ display_text }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    display_text = ""
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        display_text = f"হ্যালো, {user_input}! ডকার কন্টেইনার থেকে স্বাগতম।"
    return render_template_string(HTML_TEMPLATE, display_text=display_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
