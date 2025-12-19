import React, { useState, FormEvent } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './Chatbot.module.css';
import clsx from 'clsx';

interface ChatMessage {
  text: string;
  sender: 'user' | 'bot';
}

const Chatbot: React.FC = () => {
  const {siteConfig} = useDocusaurusContext();
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const backendUrl = siteConfig.customFields?.backendUrl || 'http://localhost:8000'; // Replace with your backend URL

  const sendMessage = async (e: FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: ChatMessage = { text: input, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      // Get the API key from site config
      const apiKey = siteConfig.customFields?.apiKey;

      // Check if API key is available
      if (!apiKey) {
        throw new Error("API key is not configured in siteConfig");
      }

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
    <div className={styles.chatbotContainer}>
      <div className={styles.chatHeader}>
        <span>🤖 Robotics AI Assistant</span>
      </div>
      <div className={styles.messages}>
        {messages.map((msg, index) => (
          <div key={index} className={clsx(styles.message, styles[msg.sender])}>
            {msg.text}
          </div>
        ))}
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
          placeholder="Ask me anything about robotics..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading}>Send</button>
      </form>
    </div>
  );
};

export default Chatbot;
