import { useEffect, useState } from 'react'
import logo from './assets/logo.png'
import './App.css'
import LoadingScreen from './components/LoadingScreen'
import TopNavigation from './components/TopNavigation'
import { doctorProfile, notifications, patients } from './data/portalData'
import DoctorProfilePage from './pages/DoctorProfilePage'
import HomePage from './pages/HomePage'
import PatientDetailsPage from './pages/PatientDetailsPage'
import PatientsPage from './pages/PatientsPage'

const DEFAULT_PAGE = 'home'

function getRouteState() {
  const { pathname } = window.location
  const cleanPath = pathname.replace(/\/+$/, '') || '/'

  if (cleanPath === '/' || cleanPath === '/home') {
    return { page: 'home', patientId: null }
  }

  if (cleanPath === '/patients') {
    return { page: 'patients', patientId: null }
  }

  if (cleanPath.startsWith('/patients/')) {
    const patientId = cleanPath.split('/')[2] ?? null
    return { page: 'patient-details', patientId }
  }

  if (cleanPath === '/doctor-profile') {
    return { page: 'doctor-profile', patientId: null }
  }

  return { page: DEFAULT_PAGE, patientId: null }
}

function getPathForPage(page, patientId) {
  switch (page) {
    case 'home':
      return '/home'
    case 'patients':
      return '/patients'
    case 'patient-details':
      return patientId ? `/patients/${patientId}` : '/patients'
    case 'doctor-profile':
      return '/doctor-profile'
    default:
      return '/home'
  }
}

function App() {
  const [isLoading, setIsLoading] = useState(true)
  const initialRoute = getRouteState()
  const [currentPage, setCurrentPage] = useState(initialRoute.page)
  const [selectedPatientId, setSelectedPatientId] = useState(
    initialRoute.patientId ?? patients[0]?.id ?? null,
  )

  useEffect(() => {
    const timer = window.setTimeout(() => {
      setIsLoading(false)
    }, 1200)

    return () => window.clearTimeout(timer)
  }, [])

  useEffect(() => {
    const handlePopState = () => {
      const route = getRouteState()
      setCurrentPage(route.page)
      setSelectedPatientId(route.patientId ?? patients[0]?.id ?? null)
    }

    window.addEventListener('popstate', handlePopState)
    return () => window.removeEventListener('popstate', handlePopState)
  }, [])

  const selectedPatient =
    patients.find((patient) => patient.id === selectedPatientId) ?? patients[0]

  const sortedNotifications = [...notifications].sort(
    (left, right) => right.priority - left.priority,
  )

  const navigateTo = (page, patientId = null) => {
    const resolvedPatientId =
      page === 'patient-details' ? patientId ?? selectedPatientId ?? patients[0]?.id : null
    const nextPath = getPathForPage(page, resolvedPatientId)

    if (window.location.pathname !== nextPath) {
      window.history.pushState({ page, patientId: resolvedPatientId }, '', nextPath)
    }

    setCurrentPage(page)
    if (resolvedPatientId) {
      setSelectedPatientId(resolvedPatientId)
    }
    window.scrollTo({ top: 0, left: 0, behavior: 'auto' })
  }

  const handleNavigate = (page) => {
    if (page === 'patient-details') {
      navigateTo(page, selectedPatientId)
      return
    }

    navigateTo(page)
  }

  const handleSelectPatient = (patientId) => {
    navigateTo('patient-details', patientId)
  }

  if (isLoading) {
    return <LoadingScreen />
  }

  return (
    <main className="app-shell">
      <TopNavigation currentPage={currentPage} onNavigate={handleNavigate} />

      <div className="portal-app">
        <div className="page-container">
          {currentPage === 'home' && (
            <HomePage
              doctorName={doctorProfile.name}
              notifications={sortedNotifications}
            />
          )}

          {currentPage === 'patients' && (
            <PatientsPage
              patients={patients}
              onSelectPatient={handleSelectPatient}
            />
          )}

          {currentPage === 'patient-details' && selectedPatient && (
            <PatientDetailsPage patient={selectedPatient} />
          )}

          {currentPage === 'doctor-profile' && (
            <DoctorProfilePage doctor={doctorProfile} />
          )}
        </div>
      </div>

      <footer className="app-footer">
        <div className="app-footer-inner">
          <div className="footer-brand">
            <img alt="WagFu logo" className="footer-logo" src={logo} />
            WagFu Doctor Portal
          </div>
          <p>Phase 1. copyright WagFu</p>
        </div>
      </footer>
    </main>
  )
}

export default App
