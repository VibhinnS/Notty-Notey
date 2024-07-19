import Header from "./components/Header"
import NotesListPage from "./pages/NotesListPage"
import { useState, useEffect } from "react"
function App() {

  return (
    <div className='App'>
      <Header />
      <NotesListPage />
    </div>
  )
}

export default App
