import { useState } from 'react'
import './App.css'

function App() {
  const [code, setCode] = useState('')
  const [explanation, setExplanation] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleExplain = async () => {
    setLoading(true)
    setExplanation('')
    setError('')
    try {
      const response = await fetch('http://127.0.0.1:8000/explain', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }),
      })
      if (!response.ok) {
        const data = await response.text()
        throw new Error(data || 'Error from backend')
      }
      const reader = response.body.getReader()
      const decoder = new TextDecoder()
      let result = ''
      while (true) {
        const { value, done } = await reader.read()
        if (done) break
        result += decoder.decode(value, { stream: true })
        setExplanation(result)
      }
    } catch (err) {
      setError(err.message)
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Code Explainer</h1>
      <textarea
        rows={10}
        cols={60}
        placeholder="Paste your code here..."
        value={code}
        onChange={e => setCode(e.target.value)}
        disabled={loading}
        style={{ fontFamily: 'monospace', fontSize: '1rem', width: '100%' }}
      />
      <br />
      <button onClick={handleExplain} disabled={loading || !code.trim()}>
        {loading ? 'Explaining...' : 'Explain Code'}
      </button>
      {error && <div style={{ color: 'red', marginTop: 10 }}>{error}</div>}
      {explanation && (
        <div style={{ marginTop: 20, background: '#f6f8fa', padding: 15, borderRadius: 8 }}>
          <strong>Explanation:</strong>
          <div style={{ marginTop: 8 }}>{explanation}</div>
        </div>
      )}
    </div>
  )
}

export default App
