import './App.css'
import UserProfileForm from './components/userprofileform'
import { Routes, Route, BrowserRouter } from 'react-router-dom'
import Dashboard from './components/dashboard/dashboard'

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/register" element={<UserProfileForm />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App