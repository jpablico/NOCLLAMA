import React, { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import { queryLLM } from "../api/queryLLM";

function Typewriter({ text, speed = 30 }) {
  const [displayedText, setDisplayedText] = useState("");

  useEffect(() => {
    let index = 0;
    setDisplayedText("");
    const interval = setInterval(() => {
      setDisplayedText((prev) => prev + text.charAt(index));
      index++;
      if (index >= text.length) clearInterval(interval);
    }, speed);

    return () => clearInterval(interval);
  }, [text, speed]);

  return <ReactMarkdown>{displayedText}</ReactMarkdown>;
}

function MessageBubble({ role, text, index }) {
  const baseStyle = "px-2 py-1 rounded-lg max-w-xl whitespace-pre-wrap";
  const userStyle = "bg-blue-600 text-white self-end";
  const assistantStyle = "bg-gray-700 text-white self-start";
  return (
    <div className={`my-1 flex ${role === "user" ? "justify-end" : "justify-start"}`}>
      <div className={`${baseStyle} ${role === "user" ? userStyle : assistantStyle}`}>
        {role === "assistant" ? (
          <div className="text-sm leading-snug space-y-1 markdown-content">
            <Typewriter text={text} />
          </div>
        ) : (
          text
        )}
      </div>
    </div>
  );
}

export default function ChatInterface() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleAsk = async () => {
    if (!question.trim()) return;
    const userMessage = { role: "user", text: question };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);
    setQuestion("");

    try {
      const response = await queryLLM(userMessage.text);
      const assistantMessage = { role: "assistant", text: response };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      setMessages((prev) => [...prev, { role: "assistant", text: "Error fetching response." }]);
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white">
      <header className="p-4 bg-gray-800 text-xl font-bold text-center">NOCLLAMA Assistant</header>

      <div className="flex-1 overflow-y-auto p-4">
        <div className="mx-auto max-w-4xl space-y-2">
          {messages.map((msg, idx) => (
            <MessageBubble key={idx} role={msg.role} text={msg.text} index={idx} />
          ))}
          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className="p-4 bg-gray-800">
        <div className="mx-auto max-w-4xl flex items-center space-x-2">
          <textarea
            rows="2"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                handleAsk();
              }
            }}
            placeholder="Ask a NOC question..."
            className="flex-1 p-2 rounded border border-gray-600 bg-gray-700 text-white resize-none"
          />
          <button
            onClick={handleAsk}
            disabled={loading}
            className={`h-full px-4 py-2 rounded ${loading ? "bg-blue-800 opacity-50" : "bg-blue-600"} text-white`}
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>
      </div>
    </div>
  );
}