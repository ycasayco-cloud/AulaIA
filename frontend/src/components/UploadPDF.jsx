import axios from 'axios'

function UploadPDF() {

  const subirPDF = async (e) => {

    const file = e.target.files[0]

    if (!file) return

    const formData = new FormData()

    formData.append('file', file)

    try {

      await axios.post(
        'https://aulaia.onrender.com/subir-pdf',
        formData
      )

      alert('PDF subido correctamente')

    } catch (error) {
      console.error(error)
      alert('Error al subir PDF')
    }
  }

  return (
    <div>
      <label className="bg-blue-600 hover:bg-blue-700 p-3 rounded-xl cursor-pointer block text-center">
        Subir PDF

        <input
          type="file"
          accept="application/pdf"
          className="hidden"
          onChange={subirPDF}
        />
      </label>
    </div>
  )
}

export default UploadPDF