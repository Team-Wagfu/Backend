function AppointmentTimeline({ appointments }) {
  return (
    <section className="panel">
      <h2>Upcoming Appointments 🗓️</h2>
      <div className="timeline-list">
        {appointments.map((appointment) => (
          <article className="timeline-item" key={appointment.id}>
            <span>{appointment.date}</span>
            <h3>{appointment.title}</h3>
            <p>{appointment.description}</p>
          </article>
        ))}
      </div>
    </section>
  )
}

export default AppointmentTimeline
