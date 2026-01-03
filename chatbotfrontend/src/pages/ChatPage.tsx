import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { chatAPI } from '../api';
import { ChatMessage } from '../components/ChatMessage';
import { ChatSidebar } from '../components/ChatSidebar';
import '../styles/Chat.css';

interface ChatItem {
  id: number;
  query: string;
  response: string;
  created_at: string;
}

export const ChatPage = () => {
  const { user, logout } = useAuth();
  const [messages, setMessages] = useState<ChatItem[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [selectedChat, setSelectedChat] = useState<ChatItem | null>(null);
  const [error, setError] = useState('');

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      setError('');
      const response = await chatAPI.getHistory();
      setMessages(response.data || []);
    } catch (err: any) {
      console.error('Failed to load history', err);
      setError('Failed to load chat history');
    }
  };

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    setLoading(true);
    setError('');
    
    try {
      const response = await chatAPI.sendMessage(input);
      setMessages([response.data, ...messages]);
      setInput('');
      setSelectedChat(response.data);
    } catch (err: any) {
      console.error('Failed to send message', err);
      const errorMsg = err.response?.data?.error || 'Failed to send message. Please try again.';
      setError(errorMsg);
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteChat = async (chatId: number) => {
    try {
      setError('');
      await chatAPI.deleteChat(chatId);
      setMessages(messages.filter(m => m.id !== chatId));
      setSelectedChat(null);
    } catch (err: any) {
      console.error('Failed to delete chat', err);
      setError('Failed to delete chat');
    }
  };

  return (
    <div className="chat-container">
      <ChatSidebar 
        messages={messages} 
        selectedChat={selectedChat}
        onSelectChat={setSelectedChat}
        onDeleteChat={handleDeleteChat}
      />
      <div className="chat-main">
        <div className="chat-header">
          <h1>ChatBot</h1>
          <div className="user-section">
            <span>Greetings! {user?.username}</span>
            <button onClick={logout} className="logout-btn">Logout</button>
          </div>
        </div>

        {error && <div className="error-message" style={{margin: '10px', padding: '10px', background: '#fee', border: '1px solid #fcc', color: '#c33', borderRadius: '5px'}}>{error}</div>}

        <div className="messages-area">
          {selectedChat ? (
            <div className="selected-chat">
              <ChatMessage 
                type="user" 
                content={selectedChat.query}
                timestamp={selectedChat.created_at}
              />
              <ChatMessage 
                type="assistant" 
                content={selectedChat.response}
                timestamp={selectedChat.created_at}
              />
            </div>
          ) : (
            <div className="welcome-message">
              <h2>Welcome to ChatBot!</h2>
              <p>Start a new conversation or select a previous chat from the sidebar.</p>
            </div>
          )}
        </div>

        <form onSubmit={handleSendMessage} className="chat-form">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Sending...' : 'Send'}
          </button>
        </form>
      </div>
    </div>
  );
};
