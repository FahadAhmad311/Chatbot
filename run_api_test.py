#!/usr/bin/env python
"""Test the chat API endpoint"""
import subprocess
import time
import sys

# Give server time to start
print("Waiting for server to be ready...")
time.sleep(2)

# Test with curl-like approach using Python requests
test_script = '''
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

# Step 1: Register
print("\\n[1] Registering user...")
reg_resp = requests.post(f"{BASE_URL}/register/", json={
    "username": "chattest123",
    "email": "chattest@example.com",
    "password": "TestPass123!"
})
print(f"Status: {reg_resp.status_code}")
if reg_resp.status_code == 201:
    data = reg_resp.json()
    token = data.get("token")
    print(f"✓ Registered successfully, token: {token[:20]}...")
else:
    print(f"Response: {reg_resp.text}")
    sys.exit(1)

# Step 2: Chat
print("\\n[2] Sending chat message...")
chat_resp = requests.post(
    f"{BASE_URL}/chat/",
    headers={"Authorization": f"Token {token}"},
    json={"query": "Hello, how are you?"}
)
print(f"Status: {chat_resp.status_code}")
print(f"Response: {chat_resp.text}")

if chat_resp.status_code == 201:
    print("✓ Chat request successful!")
else:
    print("✗ Chat request failed")
    
sys.exit(0)
'''

# Run the test
result = subprocess.run([sys.executable, "-c", test_script], capture_output=True, text=True, timeout=30)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
print(f"Return code: {result.returncode}")
