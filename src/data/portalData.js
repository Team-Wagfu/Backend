export const doctorProfile = {
  name: 'Dummy',
  qualification: 'BVSc & AH, MVSc',
  specialization: 'Small Animal Surgery',
  clinic: 'WagFu Veterinary Center',
  experience: '9 years',
  email: 'aditya.sharma@wagfu.example',
  phone: '+91 91234 56789',
  shift: '8:00 AM to 6:00 PM',
  location: 'Chennai, Tamil Nadu',
}

export const notifications = [
  {
    id: 'notif-1',
    title: 'Emergency revisit scheduled for Bruno',
    message: 'Breathing irregularity reported by the owner. Review case notes before 9:00 AM.',
    priority: 5,
    type: 'Critical',
  },
  {
    id: 'notif-2',
    title: 'Vaccination reminder approvals pending',
    message: 'Five patient reminders need doctor confirmation before they are released to owners.',
    priority: 4,
    type: 'Action Needed',
  },
  {
    id: 'notif-3',
    title: 'Post-surgery follow-up queue updated',
    message: 'Luna, Coco, and Max require progress review during the afternoon consultation block.',
    priority: 3,
    type: 'Follow-up',
  },
  {
    id: 'notif-4',
    title: 'Lab reports available',
    message: 'New blood panel results are available for Daisy and Simba.',
    priority: 2,
    type: 'Reports',
  },
]

export const patients = [
  {
    id: 'pet-001',
    petName: 'Luna',
    ownerName: 'Priya Raman',
    passportId: 'WF-2048',
    species: 'Canine',
    breed: 'Golden Retriever',
    age: '6 years',
    gender: 'Female',
    weight: '28.4 kg',
    primaryConcern: 'Post-surgery recovery',
    vaccinationStatus: 'Up to date',
    allergies: 'No known allergies',
    currentMedication: 'Carprofen 75 mg',
    emergencyContact: '+91 98765 43210',
    notes: [
      {
        id: 'note-1',
        title: 'Post-operative checkup',
        date: '12 March 2026',
        notes:
          'Incision healing well. Mild stiffness remains in the left hind limb. Continue restricted activity for one more week.',
      },
      {
        id: 'note-2',
        title: 'Cruciate ligament surgery',
        date: '25 February 2026',
        notes:
          'Successful TPLO procedure completed. Pain management plan issued and rehabilitation timeline explained to the owner.',
      },
      {
        id: 'note-3',
        title: 'Orthopedic consultation',
        date: '10 February 2026',
        notes:
          'Intermittent limping observed for three weeks. X-ray and blood work recommended before surgery planning.',
      },
    ],
    appointments: [
      {
        id: 'appt-1',
        title: 'Mobility assessment',
        date: '29 March 2026, 10:00 AM',
        description: 'Review gait progress, pain response, and update recovery exercises.',
      },
      {
        id: 'appt-2',
        title: 'Suture review',
        date: '04 April 2026, 9:30 AM',
        description: 'Inspect healing progress and decide whether bandage support is still needed.',
      },
    ],
  },
  {
    id: 'pet-002',
    petName: 'Bruno',
    ownerName: 'Rahul Menon',
    passportId: 'WF-1186',
    species: 'Canine',
    breed: 'Beagle',
    age: '4 years',
    gender: 'Male',
    weight: '16.1 kg',
    primaryConcern: 'Respiratory review',
    vaccinationStatus: 'Booster due next month',
    allergies: 'Dust sensitivity',
    currentMedication: 'Nebulization support as needed',
    emergencyContact: '+91 99887 77665',
    notes: [
      {
        id: 'note-4',
        title: 'Respiratory follow-up',
        date: '20 March 2026',
        notes:
          'Night coughing reduced, but owner reported two wheezing episodes. Monitor oxygen response if symptoms repeat.',
      },
      {
        id: 'note-5',
        title: 'Initial respiratory consult',
        date: '14 March 2026',
        notes:
          'Mild airway inflammation suspected. Advised chest imaging if no improvement within one week.',
      },
    ],
    appointments: [
      {
        id: 'appt-3',
        title: 'Emergency breathing review',
        date: '26 March 2026, 9:00 AM',
        description: 'Assess breathing pattern and determine if imaging is needed immediately.',
      },
      {
        id: 'appt-4',
        title: 'Vaccination planning',
        date: '02 April 2026, 5:00 PM',
        description: 'Review respiratory stability before approving the next vaccination schedule.',
      },
    ],
  },
  {
    id: 'pet-003',
    petName: 'Milo',
    ownerName: 'Sneha Iyer',
    passportId: 'WF-3302',
    species: 'Feline',
    breed: 'Persian',
    age: '3 years',
    gender: 'Male',
    weight: '5.2 kg',
    primaryConcern: 'Diet and skin maintenance',
    vaccinationStatus: 'Up to date',
    allergies: 'Chicken protein',
    currentMedication: 'Omega-3 supplement',
    emergencyContact: '+91 90909 88112',
    notes: [
      {
        id: 'note-6',
        title: 'Dermatology review',
        date: '15 March 2026',
        notes:
          'Skin irritation reduced. Continue elimination diet and reassess coat quality in two weeks.',
      },
      {
        id: 'note-7',
        title: 'Nutrition consult',
        date: '01 March 2026',
        notes:
          'Owner transitioned to hypoallergenic feed. Mild weight gain observed and accepted.',
      },
    ],
    appointments: [
      {
        id: 'appt-5',
        title: 'Skin progress evaluation',
        date: '30 March 2026, 3:30 PM',
        description: 'Check coat texture, irritation level, and diet compliance.',
      },
    ],
  },
]
