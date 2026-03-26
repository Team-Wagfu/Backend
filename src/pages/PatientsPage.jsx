import PatientList from '../components/PatientList'

function PatientsPage({ patients, onSelectPatient }) {
  return (
    <>
      <header className="page-header">
        <span className="section-kicker">Patient records</span>
        <h1>Patients 🐶</h1>
        <p>
          Browse all registered pets with their owner information and passport
          ID in one place.
        </p>
      </header>

      <PatientList patients={patients} onSelectPatient={onSelectPatient} />
    </>
  )
}

export default PatientsPage
