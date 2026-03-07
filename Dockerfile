# ১. পাইথনের অফিশিয়াল ইমেজ ব্যবহার করা
FROM python:3.9-slim

# ২. অ্যাপ্লিকেশনের জন্য একটি ফোল্ডার তৈরি করা
WORKDIR /app

# ৩. প্রয়োজনীয় ফাইলগুলো কপি করা
COPY requirements.txt .

# ৪. লাইব্রেরিগুলো ইনস্টল করা
RUN pip install --no-cache-dir -r requirements.txt

# ৫. অ্যাপ্লিকেশনের কোড কপি করা
COPY . .

# ৬. অ্যাপ্লিকেশনটি রান করার কমান্ড
CMD ["python", "app.py"]
