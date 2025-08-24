import { useEffect, useState } from "react"

function App() {
  const [note, setNote] = useState(null)

  useEffect(() => {
    fetch("http://65.0.178.126:3000/note").then((res) => res.json()).then(data => setNote(data))
  }, [])
  return (
    <>
     {`Note: ${note?.title}`}
    </>
  )
}

export default App
