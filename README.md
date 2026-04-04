# Wagfu Backend

Backend service for Wagfu, a comprehensive pet care platform. This service handles user authentication, pet management, veterinary services, and emergency logistics.

## Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [API Documentation](#-api-documentation)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Running the Server](#-running-the-server)
- [Testing](#-testing)
- [Environment Variables](#-environment-variables)
- [Deployment](#-deployment)

## Features

- **User Management**: Authentication and profile management for pet owners, veterinarians, emergency services, and admins.
- **Pet Profiles**: Detailed pet profiles with breed, vaccination, and medical history tracking.
- **Veterinary Services**: Clinic and doctor management with ratings and reviews.
- **Emergency Logistics**: Real-time tracking and dispatch for emergency services.
- **Pharmaceuticals**: Management of veterinary pharmacies and medication.
- **Notifications**: Push notifications for appointments, emergencies, and updates.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Validation**: Pydantic
- **Testing**: Pytest
- **Documentation**: Swagger UI / ReDoc

## Database Schema

### Core Entities

#### Users
Base table for all system actors.

```sql
CREATE TABLE Users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type VARCHAR(50) NOT NULL,  -- pet_owner, emergency, doctor, admin, pharmaceutical
    display_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Pets
Detailed pet profiles.

```sql
CREATE TABLE Pets (
    pet_id VARCHAR(50) PRIMARY KEY,  -- Format: PET-YYYY-NNNNN
    user_id UUID REFERENCES Users(user_id),
    name VARCHAR(255) NOT NULL,
    dob DATE,
    species VARCHAR(50),
    breed VARCHAR(100),
    color VARCHAR(50),
    weight FLOAT,
    height FLOAT,
    vaccines JSONB,
    medical_history TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Profile Extensions

#### Pet Owners
```sql
CREATE TABLE Pet_Owners (
    user_id UUID PRIMARY KEY REFERENCES Users(user_id),
    owner_id VARCHAR(50) UNIQUE,  -- Format: PW-YYYY-NNNNN
    location JSONB,
    pet_ids TEXT[]  -- Array of pet_ids
);
```

#### Emergency Services
```sql
CREATE TABLE Emergency_Services (
    user_id UUID PRIMARY KEY REFERENCES Users(user_id),
    eme_id VARCHAR(50) UNIQUE,  -- Format: EME-YYYY-NNNNN
    contact VARCHAR(20),
    vehicle_type VARCHAR(50),
    vehicle_reg_no VARCHAR(20),
    vehicle_capacity INT,
    user_liscence VARCHAR(50),
    level INT,
    status VARCHAR(20) DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Doctors
```sql
CREATE TABLE Doctors (
    user_id UUID PRIMARY KEY REFERENCES Users(user_id),
    doc_id VARCHAR(50) UNIQUE,  -- Format: DOC-YYYY-NNNNN
    clinic_ids TEXT[],
    specialization VARCHAR(100),
    experience INT,
    rating FLOAT,
    reviews JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Admins
```sql
CREATE TABLE Admins (
    user_id UUID PRIMARY KEY REFERENCES Users(user_id),
    admin_id VARCHAR(50) UNIQUE,  -- Format: ADM-YYYY-NNNNN
    role VARCHAR(50),
    permissions JSONB
);
```

#### Pharmaceuticals
```sql
CREATE TABLE Pharmaceuticals (
    user_id UUID PRIMARY KEY REFERENCES Users(user_id),
    shop_id VARCHAR(50) UNIQUE,  -- Format: PHM-YYYY-NNNNN
    license_no VARCHAR(50),
    name VARCHAR(255),
    owner_name VARCHAR(255),
    contact VARCHAR(20),
    location JSONB,
    rating FLOAT,
    reviews JSONB,
    level INT,
    verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Clinics
```sql
CREATE TABLE Clinics (
    clinic_id VARCHAR(50) PRIMARY KEY,  -- Format: CLN-YYYY-NNNNN
    clinic_name VARCHAR(255),
    location JSONB,
    facilities TEXT[],
    rating FLOAT,
    reviews JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Facilities
```sql
CREATE TABLE Facilities (
    facility_id VARCHAR(50) PRIMARY KEY,  -- Format: FAC-YYYY-NNNNN
    facility_name VARCHAR(255),
    facility_description TEXT,
    facility_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Medical Records
```sql
CREATE TABLE Medical_Records (
    diagnosis_id VARCHAR(50) PRIMARY KEY,  -- Format: MED-YYYY-NNNNN
    doctor_id VARCHAR(50),
    notes TEXT,
    diagnosis TEXT,
    date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🚀 API Documentation

### Authentication

#### Register User
```http
POST /auth/register
```

**Request Body:**
```json
{
  "type": "pet_owner",
  "display_name": "John Doe",
  "email": "[EMAIL_ADDRESS]",
  "password": "securepassword",
  "phone": "1234567890"
}
```

**Response:**
```json
{
  "user_id": "uuid",
  "display_name": "John Doe",
  "type": "pet_owner",
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

#### Login
```http
POST /auth/login
```

**Request Body:**
```json
{
  "email": "[EMAIL_ADDRESS]",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

### Pets

#### Create Pet
```http
POST /pets
```

**Request Body:**
```json
{
  "name": "Buddy",
  "dob": "2022-01-15",
  "species": "DOG",
  "breed": "Labrador",
  "color": "Golden",
  "weight": 25.5,
  "height": 55.0,
  "vaccines": [
    {
      "vaccine_name": "Rabies",
      "due_date": "2023-01-15",
      "status": "due"
    }
  ]
}
```

**Response:**
```json
{
  "pet_id": "PET-2026-00001",
  "name": "Buddy",
  "dob": "2022-01-15",
  
