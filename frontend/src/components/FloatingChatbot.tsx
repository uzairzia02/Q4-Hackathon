import React, { useState } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import clsx from 'clsx';
import styles from './FloatingChatbot.module.css';

interface ChatMessage {
  text: string;
  sender: 'user' | 'bot';
}

const FloatingChatbot: React.FC = () => {
  const { siteConfig } = useDocusaurusContext();
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const backendUrl = siteConfig.customFields?.backendUrl || 'http://localhost:8000';
  const apiKey = siteConfig.customFields?.apiKey;

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || !apiKey) return;

    const userMessage: ChatMessage = { text: input, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch(`${backendUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-KEY': apiKey,
        },
        body: JSON.stringify({
          query: userMessage.text,
          selected_text: null,
          user_id: 'docusaurus-user'
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage: ChatMessage = { text: data.answer || data.response || "Sorry, I didn't receive a response", sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error sending message to backend:", error);
      const errorMessage: ChatMessage = { text: "Sorry, I'm having trouble connecting to the chatbot.", sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.floatingChatbot}>
      {isOpen ? (
        <div className={styles.chatContainer}>
          <div className={styles.chatHeader}>
            <span>🤖 Robotics AI Assistant</span>
            <button 
              className={styles.closeButton} 
              onClick={() => setIsOpen(false)}
            >
              ×
            </button>
          </div>
          <div className={styles.messages}>
            {messages.length === 0 ? (
              <div className={styles.welcomeMessage}>
                Hello! I'm your Robotics AI Assistant. Ask me anything about the course!
              </div>
            ) : (
              messages.map((msg, index) => (
                <div key={index} className={clsx(styles.message, styles[msg.sender])}>
                  {msg.text}
                </div>
              ))
            )}
            {isLoading && (
              <div className={clsx(styles.message, styles.bot)}>
                <div className={styles.loadingDots}>
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            )}
          </div>
          <form onSubmit={sendMessage} className={styles.inputForm}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about robotics..."
              disabled={isLoading}
            />
            <button type="submit" disabled={isLoading}>➤</button>
          </form>
        </div>
      ) : (
        <button 
          className={styles.chatButton}
          onClick={() => setIsOpen(true)}
        >
          🤖
        </button>
      )}
    </div>
  );
};

export default FloatingChatbot;