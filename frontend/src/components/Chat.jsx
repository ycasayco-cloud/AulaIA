import { useEffect, useState } from 'react'
import axios from 'axios'
import Message from './Message'

import {
  collection,
  addDoc,
  onSnapshot,
  orderBy,
  query
} from 'firebase/firestore'

import { db } from '../firebase'

function Chat() {

  const [mensaje, setMensaje] = useState('')

  const [mensajes, setMensajes] = useState([])

  const sessionId = localStorage.getItem('sessionId') || crypto.randomUUID()

  localStorage.setItem('sessionId', sessionId)

  useEffect(() => {

    const q = query(
      collection(db, 'chats', sessionId, 'mensajes'),
      orderBy('createdAt')
    )

    const unsubscribe = onSnapshot(q, (snapshot) => {

      const datos = snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      }))

      setMensajes(datos)
    })

    return () => unsubscribe()

  }, [])

  const enviarPregunta = async () => {

  }
  return (
    <div className="flex-1 flex flex-col">

      <div className="flex-1 overflow-y-auto p-6 space-y-4">

        {
          mensajes.map((msg) => (
            <Message
              key={msg.id}
              role={msg.role}
              text={msg.text}
            />
          ))
        }

      </div>

      <div className="border-t border-slate-800 p-4 flex gap-4">

        <input
          type="text"
          placeholder="Escribe tu pregunta..."
          value={mensaje}
          onChange={(e) => setMensaje(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              enviarPregunta()
            }
          }}
          className="
            flex-1
            bg-slate-800
            rounded-xl
            px-4
            py-3
            outline-none
          "
        />

        <button
          onClick={enviarPregunta}
          className="bg-blue-600 hover:bg-blue-700 px-6 rounded-xl"
        >
          Enviar
        </button>

      </div>

    </div>
  )
}

export default Chat