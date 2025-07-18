import React, { useState } from "react";
import { queryLLM } from "../api/queryLLM";

function Typewriter({ text, speed = 30 }) {
  const [displayedText, setDisplayedText] = React.useState("");

  React.useEffect(() => {
    let index = 0;
    setDisplayedText("");
    const interval = setInterval(() => {
      setDisplayedText((prev) => prev + text.charAt(index));
      index++;
      if (index >= text.length) clearInterval(interval);
    }, speed);

    return () => clearInterval(interval);
  }, [text, speed]);

  return <p>{displayedText}</p>;
}

export default function ChatInterface() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    setLoading(true);
    try {
      const response = await queryLLM(question);
      setAnswer(response);
    } catch (err) {
      setAnswer("Error fetching response.");
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <div>
        <h1 className="text-2xl font-bold mb-4">NOCLLAMA Assistant</h1>
        <textarea
          rows="3"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a NOC question..."
          className="w-full p-2 border border-gray-300 rounded mb-4"
        />
        <br />
        <button
          onClick={handleAsk}
          disabled={loading}
          className={`bg-blue-600 text-white px-4 py-2 rounded ${loading ? "opacity-50" : ""}`}
        >
          {loading ? "Thinking..." : "Ask"}
        </button>
        <div className="mt-4 whitespace-pre-wrap">
          <strong>Answer:</strong>
          <Typewriter text={answer} speed={20} />
        </div>
      </div>
    </div>
  );
}