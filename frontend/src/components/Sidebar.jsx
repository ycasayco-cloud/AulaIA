import UploadPDF from './UploadPDF'

function Sidebar() {
  return (
    <div className="w-72 bg-slate-950 border-r border-slate-800 p-4 flex flex-col">

      <h1 className="text-2xl font-bold mb-6">
        AulaIA
      </h1>

      <UploadPDF />

      <div className="mt-6">
        <h2 className="text-sm text-slate-400 mb-2">
          Documentos
        </h2>

        <div className="space-y-2">
          <div className="bg-slate-800 p-3 rounded-xl">
            mineria.pdf
          </div>

          <div className="bg-slate-800 p-3 rounded-xl">
            tesis.pdf
          </div>
        </div>
      </div>

    </div>
  )
}

export default Sidebar