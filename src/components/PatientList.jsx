function PatientList({ patients, onSelectPatient }) {
  return (
    <section className="panel">
      <h2>All Patients 📋</h2>
      <div className="patient-list">
        {patients.map((patient) => (
          <button
            className="patient-card"
            key={patient.id}
            onClick={() => onSelectPatient(patient.id)}
            type="button"
          >
            <div className="patient-card-header">
              <div>
                <h3>{patient.petName}</h3>
                <p>{patient.ownerName}</p>
              </div>
              <span className="passport-tag">{patient.passportId}</span>
            </div>
            <div className="patient-card-footer">
              <span>{patient.species}</span>
              <span>{patient.breed}</span>
            </div>
          </button>
        ))}
      </div>
    </section>
  )
}

export default PatientList
