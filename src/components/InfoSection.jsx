function InfoSection({ title, items }) {
  return (
    <section className="panel">
      <h2>{title === 'Clinical Details' ? `${title} 🧾` : `${title} ✨`}</h2>
      <div className="detail-section-list">
        {items.map((item) => (
          <div className="detail-card" key={item.label}>
            <span>{item.label}</span>
            <strong>{item.value}</strong>
          </div>
        ))}
      </div>
    </section>
  )
}

export default InfoSection
