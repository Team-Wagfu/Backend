function DoctorProfilePage({ doctor }) {
  const details = [
    { label: 'Full Name', value: doctor.name },
    { label: 'Qualification', value: doctor.qualification },
    { label: 'Specialization', value: doctor.specialization },
    { label: 'Clinic', value: doctor.clinic },
    { label: 'Experience', value: doctor.experience },
    { label: 'Email', value: doctor.email },
    { label: 'Phone', value: doctor.phone },
    { label: 'Shift', value: doctor.shift },
    { label: 'Location', value: doctor.location },
  ]

  return (
    <>
      <header className="page-header">
        <span className="section-kicker">Doctor account</span>
        <h1>Doctor Profile 👩‍⚕️</h1>
        <p>
          Core veterinarian information is organized here so additional profile
          features can be added later.
        </p>
      </header>

      <section className="panel panel-highlight">
        <div className="profile-grid">
          {details.map((detail) => (
            <article className="profile-card" key={detail.label}>
              <span>{detail.label}</span>
              <h3>{detail.value}</h3>
            </article>
          ))}
        </div>
      </section>
    </>
  )
}

export default DoctorProfilePage
