# Full Stack ChatBot Application

A modern, fully authenticated chatbot application built with Django (Backend) and React TypeScript (Frontend), integrated with Google's Gemini AI.

## 🎯 Features

- **User Authentication**
  - Sign up with username, email, and password
  - Secure login with token-based authentication
  - Persistent session management

- **AI-Powered Chat**
  - Real-time chat with Google Gemini API (gemini-1.5-flash model)
  - Intelligent responses powered by cutting-edge AI

- **Chat Management**
  - View all previous chat messages
  - Organized chat history in sidebar
  - Delete individual chats
  - Sorted by most recent

- **User Experience**
  - Personalized greeting with username
  - Responsive design (desktop & mobile)
  - Beautiful gradient UI
  - Smooth animations and transitions
  - Protected routes (only authenticated users can access chat)

- **Data Storage**
  - User information (username, email)
  - Chat queries and responses
  - Timestamps for all messages
  - Database persistence with PostgreSQL

## 🛠️ Tech Stack

### Backend
- **Django 6.0** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Database
- **google-generativeai** - Gemini AI integration
- **django-cors-headers** - CORS support

### Frontend
- **React 19** - UI library
- **TypeScript** - Type safety
- **Vite** - Fast build tool
- **Axios** - HTTP client
- **React Router** - Navigation

## 📦 Installation & Setup

### Option 1: Quick Start (Windows)
```bash
# Run the setup script
setup.bat
```

### Option 2: Manual Setup

#### Backend
```bash
cd chatbotapi

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate.bat  # On Windows
source venv/bin/activate   # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver
```

#### Frontend
```bash
cd chatbotfrontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 🚀 Running the Application

### Terminal 1: Start Backend
```bash
cd chatbotapi
venv\Scripts\activate.bat  # Activate virtual environment
python manage.py runserver
```
Backend runs on: `http://localhost:8000`

### Terminal 2: Start Frontend
```bash
cd chatbotfrontend
npm run dev
```
Frontend runs on: `http://localhost:5173`

## 📋 API Endpoints

### Authentication Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Create new user account |
| POST | `/api/login/` | Login user and get token |
| GET | `/api/profile/` | Get current user profile |

### Chat Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/chat/` | Send message to AI |
| GET | `/api/history/` | Get all user's chats |
| DELETE | `/api/history/<id>/` | Delete specific chat |

### Example Requests

**Register**
```bash
POST /api/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Login**
```bash
POST /api/login/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "securepassword123"
}
```

**Send Chat Message** (Requires Token)
```bash
POST /api/chat/
Authorization: Token your_auth_token
Content-Type: application/json

{
  "query": "What is machine learning?"
}
```

**Get Chat History** (Requires Token)
```bash
GET /api/history/
Authorization: Token your_auth_token
```

## 🔐 Authentication

The application uses **Token-based Authentication**:
1. User registers or logs in
2. Server returns an authentication token
3. Token is stored in localStorage
4. Token is sent with every API request in the `Authorization` header
5. Protected routes require valid token

## 📁 Project Structure

```
Chatbotnew/
├── chatbotapi/
│   ├── chatbot/
│   │   ├── __init__.py
│   │   ├── models.py              # ChatHistory model
│   │   ├── views.py               # API endpoints
│   │   ├── serializers.py         # Serializers
│   │   ├── urls.py                # URL routing
│   │   ├── apps.py
│   │   └── admin.py               # Admin configuration
│   ├── chatbotapi/
│   │   ├── settings.py            # Django settings
│   │   ├── urls.py                # Main URL config
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── requirements.txt           # Python dependencies
│   └── .env.example               # Environment variables template
│
├── chatbotfrontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Login.tsx          # Login page
│   │   │   ├── Register.tsx       # Registration page
│   │   │   └── ChatPage.tsx       # Main chat interface
│   │   ├── components/
│   │   │   ├── ChatMessage.tsx    # Message component
│   │   │   ├── ChatSidebar.tsx    # History sidebar
│   │   │   └── ProtectedRoute.tsx # Route protection
│   │   ├── context/
│   │   │   └── AuthContext.tsx    # Auth state management
│   │   ├── styles/
│   │   │   ├── Auth.css           # Auth pages styling
│   │   │   ├── Chat.css           # Chat page styling
│   │   │   ├── ChatMessage.css    # Message styling
│   │   │   └── ChatSidebar.css    # Sidebar styling
│   │   ├── api.ts                 # API client
│   │   ├── App.tsx                # Main app component
│   │   └── main.tsx               # Entry point
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── index.html
│
├── SETUP_INSTRUCTIONS.md           # Detailed setup guide
├── setup.bat                        # Windows setup script
└── README.md                        # This file
```

## ⚙️ Configuration

### Database
PostgreSQL configuration in `chatbotapi/chatbotapi/settings.py`:
- Database: `Chatbot`
- User: `postgres`
- Password: `etkit@136`
- Host: `localhost`
- Port: `5432`

### Gemini API
Google Gemini API key is configured in `chatbotapi/chatbot/views.py`:
```python
GEMINI_API_KEY = "AIzaSyDxV80MYlt6BJ8hJrQuVvIjSHHUlZcfzAYs"
GEMINI_MODEL = "gemini-1.5-flash"
```

### CORS
Allowed origins for frontend requests:
- `http://localhost:3000`
- `http://localhost:5173`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`

## 🐛 Troubleshooting

### Backend Won't Start
```bash
# Check if PostgreSQL is running
# Verify database credentials in settings.py
# Run migrations
python manage.py migrate

# Check for errors
python manage.py check
```

### CORS Errors
```bash
# Ensure backend is running on port 8000
# Check CORS_ALLOWED_ORIGINS in settings.py
# Clear browser cache
```

### Dependencies Issues
```bash
# Clear pip cache and reinstall
pip cache purge
pip install -r requirements.txt

# For frontend
npm cache clean --force
npm install
```

### Database Connection Issues
```bash
# Verify PostgreSQL is running
# Check credentials in settings.py
# Ensure 'Chatbot' database exists
# Run: python manage.py migrate
```

## 📝 Usage Guide

### Creating an Account
1. Navigate to the Sign Up page
2. Enter username, email, and password
3. Click "Sign Up"
4. You'll be automatically logged in

### Using the ChatBot
1. After login, you'll see the chat interface
2. Type your question in the input field
3. Click "Send" or press Enter
4. The AI will respond with an answer
5. Your message will be saved to history

### Managing Chat History
1. All previous chats appear in the left sidebar
2. Click any chat to view it again
3. Click the "×" button to delete a chat
4. Chat history is sorted by most recent first

### Logging Out
1. Click the "Logout" button in the top-right corner
2. You'll be redirected to the login page
3. Your chat history is preserved for next login

## 🎨 UI Features

- **Gradient Design** - Modern gradient backgrounds
- **Responsive Layout** - Works on desktop and mobile
- **Smooth Animations** - Message transitions and button effects
- **Dark Mode Friendly** - Optimized colors for all themes
- **Accessible** - Keyboard navigation and screen reader support

## 🔒 Security Features

- Token-based authentication
- Password hashing with Django's auth system
- CSRF protection
- CORS configuration
- Secure database credentials (use .env in production)
- Protected API endpoints
- Input validation and sanitization

## 📚 API Response Examples

**Successful Login**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**Chat Response**
```json
{
  "id": 5,
  "query": "What is AI?",
  "response": "Artificial Intelligence (AI) is...",
  "created_at": "2024-12-09T10:30:45.123456Z"
}
```

**Chat History**
```json
[
  {
    "id": 5,
    "query": "What is AI?",
    "response": "Artificial Intelligence...",
    "created_at": "2024-12-09T10:30:45.123456Z"
  },
  {
    "id": 4,
    "query": "Explain Python",
    "response": "Python is a programming...",
    "created_at": "2024-12-09T10:25:30.123456Z"
  }
]
```

## 🚀 Deployment

### Backend (Django)
```bash
# Update settings.py for production
# Set DEBUG = False
# Add domain to ALLOWED_HOSTS
# Use environment variables for secrets
# Deploy to Heroku, AWS, DigitalOcean, etc.
```

### Frontend (React)
```bash
# Build for production
npm run build

# Deploy to Vercel, Netlify, or any static hosting
```

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For issues or questions, please check:
1. SETUP_INSTRUCTIONS.md for detailed setup help
2. API response errors for specific issues
3. Browser console for frontend errors
4. Django logs for backend errors

---

**Happy Chatting!** 🤖✨

Built with ❤️ using Django, React, and Google Gemini AI
