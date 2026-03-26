import NotificationCenter from '../components/NotificationCenter'

function HomePage({ doctorName, notifications }) {
  return (
    <>
      <header className="hero-panel">
        <div className="hero-copy">
          <span className="hero-kicker">Doctor dashboard</span>
          <h1>Good morning Dr. {doctorName} ☀️</h1>
          <p>
            Here is the prioritized medical notification summary for today. The
            highest priority items are shown first so urgent cases stay visible
            🐾
          </p>
        </div>
        <div className="hero-side-card">
          <span>Today&apos;s focus</span>
          <strong>{notifications.length} active updates</strong>
          <p>Critical reviews, follow-ups, and patient activity are organized in one view 🩺</p>
        </div>
      </header>

      <NotificationCenter notifications={notifications} />
    </>
  )
}

export default HomePage
