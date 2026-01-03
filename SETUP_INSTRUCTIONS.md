# Full Stack ChatBot - Setup Instructions

## Backend Setup (Django)

### 1. Install Python Dependencies
```bash
cd chatbotapi
pip install -r requirements.txt
```

### 2. Create Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Optional - for Admin Panel)
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

The Django API will be available at: `http://localhost:8000`

---

## Frontend Setup (TypeScript + React)

### 1. Install Node Dependencies
```bash
cd chatbotfrontend
npm install
```

### 2. Run Development Server
```bash
npm run dev
```

The frontend will be available at: `http://localhost:5173` (or the port shown in terminal)

---

## API Endpoints

### Authentication
- **POST** `/api/register/` - User registration
  - Body: `{ "username": string, "email": string, "password": string }`
  
- **POST** `/api/login/` - User login
  - Body: `{ "username": string, "password": string }`
  - Returns: `{ "user": {...}, "token": "..." }`

### User Profile
- **GET** `/api/profile/` - Get current user profile (Requires Auth)

### Chat/Messages
- **POST** `/api/chat/` - Send message to ChatBot (Requires Auth)
  - Body: `{ "query": string }`
  - Returns: `{ "id": number, "query": string, "response": string, "created_at": timestamp }`

- **GET** `/api/history/` - Get user's chat history (Requires Auth)
  - Returns: Array of chat objects

- **DELETE** `/api/history/<chat_id>/` - Delete specific chat (Requires Auth)

---

## Features

✅ User Authentication (Sign up / Sign in)
✅ Google Gemini AI Integration (gemini-1.5-flash model)
✅ Chat History Storage
✅ User-specific message storage
✅ Persistent session with token authentication
✅ Greeting with username display
✅ Delete chat history
✅ Responsive UI
✅ CORS enabled for cross-origin requests

---

## Important Notes

1. **Google Gemini API Key** is configured in `chatbotapi/chatbot/views.py`
   - Current Key: `AIzaSyDxV80MYlt6BJ8hJrQuVvIjSHHUlZcfzAYs`

2. **Database Configuration**: PostgreSQL is configured in settings.py
   - Database: Chatbot
   - User: postgres
   - Password: etkit@136
   - Host: localhost
   - Port: 5432

3. **CORS Settings**: Frontend can connect from:
   - http://localhost:3000
   - http://localhost:5173
   - http://127.0.0.1:3000
   - http://127.0.0.1:5173

---

## Troubleshooting

### Backend Issues
- Ensure PostgreSQL is running
- Check database credentials in `settings.py`
- Run migrations: `python manage.py migrate`

### Frontend Issues
- Clear npm cache: `npm cache clean --force`
- Reinstall packages: `rm -rf node_modules && npm install`
- Ensure backend is running on port 8000

### CORS Errors
- Make sure backend is running
- Check CORS_ALLOWED_ORIGINS in settings.py
- Verify API URL in `src/api.ts`

---

## Project Structure

```
chatbotapi/
├── chatbot/
│   ├── models.py (ChatHistory model)
│   ├── views.py (API endpoints)
│   ├── serializers.py (Data serialization)
│   ├── urls.py (Route configuration)
│   └── admin.py
├── chatbotapi/
│   ├── settings.py (Configuration)
│   ├── urls.py (Main routes)
│   └── wsgi.py
└── manage.py

chatbotfrontend/
├── src/
│   ├── pages/
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   └── ChatPage.tsx
│   ├── components/
│   │   ├── ChatMessage.tsx
│   │   ├── ChatSidebar.tsx
│   │   └── ProtectedRoute.tsx
│   ├── context/
│   │   └── AuthContext.tsx
│   ├── styles/
│   │   ├── Auth.css
│   │   ├── Chat.css
│   │   ├── ChatMessage.css
│   │   └── ChatSidebar.css
│   ├── api.ts (API client)
│   ├── App.tsx (Main app with routing)
│   └── main.tsx
└── package.json
```

---

Enjoy your ChatBot! 🚀
