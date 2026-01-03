#!/usr/bin/env python
"""Quick test of Gemini API configuration"""
import sys
sys.path.insert(0, 'd:\\Chatbotnew\\chatbotapi')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbotapi.settings')

import django
django.setup()

import google.generativeai as genai
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Test Gemini setup
api_key = "AIzaSyAI0wlVeB4RJPuNlB8juqQugA1CWK9Q6hw"
print(f"API Key length: {len(api_key)}")

try:
    genai.configure(api_key=api_key)
    print("✓ genai.configure() succeeded")
except Exception as e:
    print(f"✗ genai.configure() failed: {e}")
    sys.exit(1)

try:
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    print("✓ GenerativeModel created")
except Exception as e:
    print(f"✗ GenerativeModel failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    response = model.generate_content("Say the word 'working'")
    print(f"✓ generate_content() returned: {type(response)}")
    if hasattr(response, 'text'):
        print(f"✓ response.text exists: {response.text[:50]}")
    else:
        print(f"✗ response has no .text attribute. Attributes: {dir(response)}")
except Exception as e:
    print(f"✗ generate_content() failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n✓ All tests passed!")
