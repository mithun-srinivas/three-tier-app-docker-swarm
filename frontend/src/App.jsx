import { useEffect, useState } from "react"

function App() {
  const [note, setNote] = useState(null)

  useEffect(() => {
    fetch("http://localhost:3001/note").then((res) => res.json()).then(data => setNote(data))
  }, [])
  return (
    <>
     {`Note: ${note?.title}`}
    </>
  )
}

export default App
