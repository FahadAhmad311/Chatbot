import '../styles/ChatMessage.css';

interface ChatMessageProps {
  type: 'user' | 'assistant';
  content: string;
  timestamp?: string;
}

export const ChatMessage = ({ type, content, timestamp }: ChatMessageProps) => {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  return (
    <div className={`chat-message ${type}`}>
      <div className="message-content">
        {type === 'user' ? (
          <div className="user-message">
            <p>{content}</p>
          </div>
        ) : (
          <div className="assistant-message">
            <p>{content}</p>
          </div>
        )}
      </div>
      {timestamp && <span className="message-time">{formatDate(timestamp)}</span>}
    </div>
  );
};
