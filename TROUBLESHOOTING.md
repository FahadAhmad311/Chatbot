# Troubleshooting Guide - 500 Internal Server Error Fix

## ✅ Issues Fixed

The 500 error you encountered has been resolved. Here's what was done:

### 1. Database Migrations
```bash
python manage.py makemigrations chatbot
python manage.py migrate chatbot
```
**Issue**: ChatHistory table wasn't created.
**Solution**: Created proper database schema.

### 2. Django Settings Updated
- ✅ Added `ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']`
- ✅ Added `CSRF_TRUSTED_ORIGINS` for frontend origins
- ✅ Changed `DEFAULT_PERMISSION_CLASSES` to `AllowAny` for public endpoints
- ✅ Enabled CORS for frontend communication

### 3. Frontend Error Handling
- ✅ Added detailed error logging in API client
- ✅ Improved error messages in Register and Login components
- ✅ Added response error interceptor for debugging

---

## How to Test Now

### Step 1: Clear Everything
1. **Backend**: Restart Django server
2. **Frontend**: 
   - Press `F12` to open DevTools
   - Go to `Application` → `Storage` → `Local Storage`
   - Delete all entries
   - Clear browser cache or do a hard refresh (`Ctrl+Shift+R`)

### Step 2: Test Registration

**In Browser Console (F12 > Console):**
```javascript
// Test if backend is running
fetch('http://localhost:8000/api/register/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'testuser',
    email: 'test@example.com',
    password: 'TestPass123'
  })
}).then(r => r.json()).then(d => console.log(d))
```

You should see a response with `token` and `user` data.

### Step 3: Try the UI
1. Go to http://localhost:5173/register
2. Fill in the form
3. Click Sign Up
4. Check browser console (F12) for any errors

---

## Common Issues & Solutions

### Issue 1: Still Getting 500 Error
**Solution:**
```bash
# Check Django logs in terminal
# Look for database connection errors
# Verify PostgreSQL is running
psql -U postgres -d chatbot -c "SELECT 1"
```

### Issue 2: CORS Error
**Error Message**: `Access to XMLHttpRequest has been blocked by CORS`

**Solution:**
- Verify Django is running on `http://localhost:8000`
- Check CORS_ALLOWED_ORIGINS in settings.py
- Restart Django server

### Issue 3: "Invalid credentials" after registration
**Solution:**
- Database might not have the user
- Check Django admin: http://localhost:8000/admin
- Or check database directly:
  ```bash
  psql -U postgres -d chatbot -c "SELECT * FROM auth_user;"
  ```

### Issue 4: Token not saving to localStorage
**Solution:**
- Check browser localStorage (F12 > Application > Storage > Local Storage)
- Clear all entries and try again
- Make sure JavaScript is enabled

---

## Verification Checklist

- [ ] Django server running on `http://localhost:8000`
- [ ] Frontend running on `http://localhost:5173`
- [ ] PostgreSQL database `chatbot` exists and is running
- [ ] Database migrations completed (`python manage.py migrate`)
- [ ] Browser cache cleared and localStorage emptied
- [ ] Console shows no CORS errors
- [ ] Test API endpoint returns token

---

## Backend Logs

If you still get errors, restart Django and watch the logs:

```bash
cd chatbotapi
python manage.py runserver
```

The logs will show:
- Database connection errors
- Migration issues
- Permission denied errors
- Missing modules

---

## Frontend Debugging

Open Browser Console (F12) and look for:
1. Network errors (red in Network tab)
2. JavaScript errors (red text in Console)
3. Response data from API

All API responses are now logged. You'll see messages like:
```
API Error: {error: "Invalid credentials"}
```

---

## Test Workflow

1. **Register**: Create new account
   - Username: `testuser123`
   - Email: `test123@example.com`
   - Password: `SecurePass123!`

2. **Login**: Sign in with credentials
   - Should redirect to `/chat`
   - Should see "Greetings! testuser123" in top right

3. **Chat**: Send a message
   - Type: "Hello"
   - Should get AI response
   - Should see in chat history (left sidebar)

4. **Logout**: Click Logout button
   - Should redirect to login page
   - Session should clear

---

## If Still Not Working

Please share:
1. **Browser Console Error** (F12 > Console tab)
2. **Network Tab Response** (F12 > Network, filter to `register`, click, see Response)
3. **Django Terminal Output** (the logs when server is running)
4. **PostgreSQL Status** (is it running?)

---

## Quick Reset

If everything is broken, do a complete reset:

```bash
# Backend reset
cd chatbotapi
python manage.py migrate --fake chatbot zero  # Undo migrations
python manage.py makemigrations chatbot
python manage.py migrate
python manage.py runserver

# Frontend reset (in another terminal)
cd chatbotfrontend
# Open in browser, press Ctrl+Shift+R (hard refresh)
# Or clear cache in DevTools
```

---

**You're all set!** The API is verified to be working. Just clear your browser cache and try registration again. 🚀
