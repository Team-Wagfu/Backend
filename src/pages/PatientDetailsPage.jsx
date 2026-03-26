import AppointmentTimeline from '../components/AppointmentTimeline'
import InfoSection from '../components/InfoSection'
import PatientHistoryList from '../components/PatientHistoryList'

function PatientDetailsPage({ patient }) {
  const overview = [
    { label: 'Owner', value: patient.ownerName },
    { label: 'Passport ID', value: patient.passportId },
    { label: 'Species / Breed', value: `${patient.species} / ${patient.breed}` },
    { label: 'Age / Gender', value: `${patient.age} / ${patient.gender}` },
    { label: 'Weight', value: patient.weight },
    { label: 'Primary Concern', value: patient.primaryConcern },
  ]

  const clinicalDetails = [
    { label: 'Vaccination Status', value: patient.vaccinationStatus },
    { label: 'Allergies', value: patient.allergies },
    { label: 'Current Medication', value: patient.currentMedication },
    { label: 'Emergency Contact', value: patient.emergencyContact },
  ]

  return (
    <>
      <header className="page-header">
        <span className="section-kicker">Patient summary</span>
        <h1>{patient.petName} 🐾</h1>
        <p>
          Complete patient summary for {patient.petName}, including clinical
          details, history, and upcoming appointments.
        </p>
      </header>

      <section className="panel panel-highlight">
        <div className="patient-summary-grid">
          {overview.map((item) => (
            <div className="summary-tile" key={item.label}>
              <span>{item.label}</span>
              <strong>{item.value}</strong>
            </div>
          ))}
        </div>
      </section>

      <div className="two-column-section">
        <InfoSection title="Clinical Details" items={clinicalDetails} />
        <PatientHistoryList entries={patient.notes} />
      </div>

      <AppointmentTimeline appointments={patient.appointments} />
    </>
  )
}

export default PatientDetailsPage
