import '../styles/ChatSidebar.css';

interface ChatItem {
  id: number;
  query: string;
  response: string;
  created_at: string;
}

interface ChatSidebarProps {
  messages: ChatItem[];
  selectedChat: ChatItem | null;
  onSelectChat: (chat: ChatItem) => void;
  onDeleteChat: (chatId: number) => void;
}

export const ChatSidebar = ({
  messages,
  selectedChat,
  onSelectChat,
  onDeleteChat,
}: ChatSidebarProps) => {
  const truncateText = (text: string, length: number) => {
    return text.length > length ? text.substring(0, length) + '...' : text;
  };

  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h3>Chat History</h3>
      </div>
      <div className="chat-list">
        {messages.length === 0 ? (
          <div className="empty-history">No chats yet</div>
        ) : (
          messages.map((chat) => (
            <div
              key={chat.id}
              className={`chat-item ${selectedChat?.id === chat.id ? 'active' : ''}`}
            >
              <button
                className="chat-item-content"
                onClick={() => onSelectChat(chat)}
              >
                <p className="chat-preview">{truncateText(chat.query, 40)}</p>
                <span className="chat-date">
                  {new Date(chat.created_at).toLocaleDateString()}
                </span>
              </button>
              <button
                className="delete-btn"
                onClick={() => onDeleteChat(chat.id)}
                title="Delete chat"
              >
                ×
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
