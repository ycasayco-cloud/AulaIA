import Sidebar from './components/Sidebar'
import Chat from './components/Chat'

function App() {
  return (
    <div className="flex h-screen bg-slate-900 text-white">
      <Sidebar />
      <Chat />
    </div>
  )
}

export default App