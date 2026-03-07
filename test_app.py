import pytest
from app import app # নিশ্চিত করুন আপনার মেইন ফাইলের নাম app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# ১. টেস্ট: হোম পেজ লোড হচ্ছে কি না
def test_index_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Docker CI/CD App" in response.data

# ২. টেস্ট: নাম লিখে সাবমিট করলে সঠিক মেসেজ দেখাচ্ছে কি না
def test_submit_functionality(client):
    test_name = "kito"
    # আমরা 'user_input' ফিল্ডে নাম পাঠাচ্ছি
    response = client.post('/', data={'user_input': test_name}, follow_redirects=True)
    
    assert response.status_code == 200
    # আপনার কোডের মেসেজ অনুযায়ী চেক করা হচ্ছে
    expected_message = f"হ্যালো, {test_name}!".encode('utf-8')
    assert expected_message in response.data
    assert b"Display Box" in response.data
