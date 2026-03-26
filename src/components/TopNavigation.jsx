import logo from '../assets/logo.png'
import HomeAlt2Icon from './icons/HomeAlt2Icon'
import MedicalKitIcon from './icons/MedicalKitIcon'

function TopNavigation({ currentPage, onNavigate }) {
  return (
    <header className="top-nav">
      <button className="brand-mark" onClick={() => onNavigate('home')} type="button">
        <img alt="WagFu logo" className="brand-logo" src={logo} />
        <span className="brand-text">
          Wag<span>Fu</span>
        </span>
      </button>

      <nav className="nav-actions" aria-label="Primary navigation">
        <button
          className={`nav-button ${currentPage === 'home' ? 'is-active' : ''}`}
          onClick={() => onNavigate('home')}
          type="button"
        >
          <HomeAlt2Icon className="nav-icon-placeholder" />
          Home
        </button>
        <button
          className={`nav-button ${currentPage === 'patients' ? 'is-active' : ''}`}
          onClick={() => onNavigate('patients')}
          type="button"
        >
          <MedicalKitIcon className="nav-icon-placeholder" />
          Patients
        </button>
      </nav>

      <button
        className={`profile-button ${currentPage === 'doctor-profile' ? 'is-active' : ''}`}
        onClick={() => onNavigate('doctor-profile')}
        type="button"
      >
        <span className="profile-avatar">DR</span>
        Doctor Profile
      </button>
    </header>
  )
}

export default TopNavigation
