function PatientHistoryList({ entries }) {
  return (
    <section className="panel">
      <h2>Patient History 📘</h2>
      <div className="detail-section-list">
        {entries.map((entry) => (
          <article className="detail-card" key={entry.id}>
            <span>{entry.date}</span>
            <strong>{entry.title}</strong>
            <p>{entry.notes}</p>
          </article>
        ))}
      </div>
    </section>
  )
}

export default PatientHistoryList
