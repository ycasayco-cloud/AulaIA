function Message({ role, text }) {

  const isUser = role === 'user'

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>

      <div
        className={`
          max-w-[70%]
          p-4
          rounded-2xl
          whitespace-pre-wrap
          ${isUser
            ? 'bg-blue-600'
            : 'bg-slate-800'}
        `}
      >
        {text}
      </div>

    </div>
  )
}

export default Message