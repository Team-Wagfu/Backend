function NotificationCenter({ notifications }) {
  return (
    <section className="panel">
      <h2>Notification Center 🔔</h2>
      <div className="notification-stack">
        {notifications.map((notification) => (
          <article className="notification-card" key={notification.id}>
            <div className="notification-copy">
              <h3>{notification.title}</h3>
              <p>{notification.message}</p>
            </div>
            <div className="notification-right">
              <div className="notification-priority">P{notification.priority}</div>
              <div className="notification-meta">{notification.type}</div>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}

export default NotificationCenter
