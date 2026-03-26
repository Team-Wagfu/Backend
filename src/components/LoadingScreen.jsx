import logo from '../assets/logo.png'

function LoadingScreen() {
  return (
    <div className="loading-screen">
      <img
        alt=""
        aria-hidden="true"
        className="loading-background-logo"
        src={logo}
      />
      <div className="loading-badge">loading wagfu</div>
    </div>
  )
}

export default LoadingScreen
