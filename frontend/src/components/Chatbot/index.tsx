import React, { useState, useEffect, useRef } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './styles.module.css';

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const { siteConfig } = useDocusaurusContext();
  console.log('DEBUG: siteConfig.customFields:', siteConfig.customFields);
  const { backendUrl, apiKey } = siteConfig.customFields;
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen && messages.length === 0) {
      setMessages([
        {
          text: "Hello! I am your AI assistant. How can I help you today?",
          isBot: true,
        },
      ]);
    }
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSend = async () => {
    if (input.trim() === '') return;

    // Check if API key is available
    if (!apiKey) {
      const newMessages = [...messages, { text: input, isBot: false }];
      setMessages([
        ...newMessages,
        { text: "Error: API key is not configured. Please check your settings.", isBot: true }
      ]);
      setInput('');
      return;
    }

    const newMessages = [...messages, { text: input, isBot: false }];
    setMessages(newMessages);
    setInput('');

    try {
      const response = await fetch(`${backendUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-KEY': apiKey,
        },
        body: JSON.stringify({
          query: input,
          selected_text: null,  // Explicitly send null for optional field
          user_id: 'docusaurus-user',
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage = data.answer || data.response || "Sorry, I didn't receive a proper response from the server.";

      setMessages([...newMessages, { text: botMessage, isBot: true }]);
    } catch (error) {
      console.error("Failed to fetch from chatbot API:", error);
      setMessages([
        ...newMessages,
        { text: "Sorry, I'm having trouble connecting to the server. Please try again later.", isBot: true },
      ]);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <>
      <button className={styles.chatToggleButton} onClick={toggleChat}>
        {isOpen ? '✖' : '🤖'}
      </button>
      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h2>AI Assistant</h2>
            <button onClick={toggleChat} className={styles.closeButton}>✖</button>
          </div>
          <div className={styles.chatMessages}>
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`${styles.message} ${
                  msg.isBot ? styles.botMessage : styles.userMessage
                }`}
              >
                {msg.text}
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
          <div className={styles.chatInput}>
            <input
              type="text"
              value={input}
              onChange={handleInputChange}
              onKeyPress={handleKeyPress}
              placeholder="Type a message..."
            />
            <button onClick={handleSend}>Send</button>
          </div>
        </div>
      )}
    </>
  );
};

export default Chatbot;
