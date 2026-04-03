# Wagfu Database Design Specification

This document outlines the architecture, relational mapping, and data constraints for the Wagfu application backend. It serves as the single source of truth for the database schema and programmatic validation.

---

## 1. Core Architecture Overview
The Wagfu database follows a **Base Identity + Profile Extension** pattern. 
- **Base Table**: `Users` serves as the primary registry for all entities.
- **Extension Tables**: Specialized tables (`Pet_Owner`, `Doctors`, etc.) extend the base user with specific attributes using a 1:1 relationship via `user_id`.
- **Relational Tables**: `Pets` functions as a child entity linked to owners.

---

## 2. Primary Entities

### 2.1 Users (Internal Identity)
The primary entry point for all system actors. Identifies the "Who".
- `user_id` (**UUID**): Primary Key.
- `type` (**Enum**): `UserType` (See §4.1).
- `email` (**String**): Unique.
- `password_hash` (**String**): Secure storage.
- `created_at` (**Timestamp**): Record creation.

### 2.2 Pets (Child Table)
Stores individual pet profiles.
- `pet_id` (**String**): Formatted Unique ID (See §5.1).
- `owner_id` (**String**): Reference to `Pet_Owner`.
- `name` (**String**): Pet name.
- `age` (**Integer/Float**): Age of the pet.
- `type` (**Enum**): Species classification (See §4.2).
- `breed` (**String**): Specific breed from mapped options (See §4.3).
- `color` (**String**): Primary visual color (See §4.4).
- `weight` (**Float**): Weight in KG (decimal precision).
- `height` (**Float**): Height in CM (decimal precision).
- `vaccines` (**JSONB**): Array of vaccination records.
- `medical_history` (**JSONB**): Structured medical logs.

---

## 3. Profile Extension Tables (Derived Entities)

### 3.1 Pet_Owner
Extends base `Users` for customers.
- `user_id` (**UUID**): Foreign Key (Users).
- `owner_id` (**String**): Formatted ID (PW-slug).
- `name` (**String**): Full name.
- `location` (**JSONB**): Geo-coordinates or address.
- `pet_ids` (**JSONB**): List of associated `pet_id` strings.

### 3.2 Emergency (EME)
Logistics and mobile response units.
- `user_id` (**UUID**): Foreign Key (Users).
- `eme_id` (**String**): Formatted ID (EME-slug).
- `name` (**String**): Service/Driver name.
- `contact` (**String**): Emergency phone number.
- `vehicle_type` (**Enum**): e.g., Ambulance, Transport.
- `vehicle_reg_no` (**String**): License plate.
- `vehicle_capacity` (**Integer**): Payload/Space.
- `level` (**Integer**): [1-5] Capacity/Priority scale.
- `status` (**Enum**): `Available`, `Busy`, `Offline`.

### 3.3 Doctors (DOC)
Specialized medical professionals.
- `user_id` (**UUID**): Foreign Key (Users).
- `doc_id` (**String**): Formatted ID (DOC-slug).
- `clinic_name` (**String**): Registered clinic.
- `specialization` (**String**): Medical focus area.
- `experience` (**Integer**): Years in practice.
- `availability` (**JSONB**): Complex schedule mapping.
- `rating` (**Float**): [0.0-10.0] aggregated score.
- `reviews` (**JSONB**): Array of review objects `{rating, comment}`.

### 3.4 Admin (ADM)
Internal management and operations.
- `user_id` (**UUID**): Foreign Key (Users).
- `admin_id` (**String**): Formatted ID (ADM-slug).
- `role` (**String**): Permission level (Master, Support, Moderator).
- `permissions` (**JSONB**): Specific action scopes.

---

## 4. Reference Enums & Mappings

### 4.1 User Types (UserType)
- `pet owner`
- `emergency` (Logistics/Mobile Units)
- `docs` (Medical/Clinics)
- `admin` (System Staff)

### 4.2 Pet Species
- `DOG`, `CAT`, `BRD` (Bird), `FIH` (Fish), `REP` (Reptile), `RBT` (Rabbit), `OTH` (Other).

### 4.3 Breed Mappings
| Type        | Breeds Possible                                                                                    |
| :---------- | :------------------------------------------------------------------------------------------------- |
| **Dog**     | Labrador, German Shepherd, Golden Retriever, French Bulldog, Beagle, Poodle, Rottweiler            |
| **Cat**     | Persian, Maine Coon, Siamese, Ragdoll, Bengal, Sphynx, British Shorthair                           |
| **Bird**    | Budgie, Cockatiel, African Grey, Lovebird, Canary, Macaw, Cockatoo                                 |
| **Fish**    | Betta, Goldfish, Guppy, Molly, Angelfish, Neon Tetra, Oscar                                        |
| **Reptile** | Bearded Dragon, Leopard Gecko, Ball Python, Corn Snake, Red-Eared Slider, Veiled Chameleon, Iguana |
| **Rabbit**  | Holland Lop, Mini Rex, Netherland Dwarf, Lionhead, Flemish Giant, English Angora, Dutch Rabbit     |
| **Other**   | Hamster, Guinea Pig, Ferret, Chinchilla, Hedgehog, Sugarglider, Rat                                |

### 4.4 Color Mappings
| Type        | Colors Possible                                          |
| :---------- | :------------------------------------------------------- |
| **Dog**     | Black, White, Brown, Golden, Brindle, Cream              |
| **Cat**     | Black, White, Calico, Tabby, Ginger, Grey, Tortoiseshell |
| **Bird**    | Blue, Green, Yellow, Red, White, Multi-colored, Grey     |
| **Fish**    | Red, Blue, Gold, Silver, Orange, Spotted, Neon           |
| **Reptile** | Green, Brown, Yellow, Grey, Orange, Patterned, Black     |
| **Rabbit**  | White, Black, Grey, Cinnamon, Spotted, Agouti, Brown     |
| **Other**   | Grey, Cream, Brown, Black, White, Tan, Multi             |

---

## 5. System Logic & Formatting

### 5.1 ID Generation Protocol
Used for client-facing identity. Unlike internal UUIDs, these are reconstructable.
**Format**: `[Type-Slug]-[Year]-[5-digit-Padded-Integer]`

- **Slugs**: `PW`, `EME`, `DOC`, `ADM`.
- **Validation**: Any 5-digit value of `00000` is invalid.
- **Example**: `DOC-2026-00012`

---

## 6. Logical Audit & Programmatic Notes

> [!IMPORTANT]
> **Observation 1: Relational Redundancy**  
> You have `pet_ids` as an array in `Pet_Owner` AND `owner_id` in `Pets`. In a relational database, you should pick one source of truth (usually `owner_id` in `Pets`) to avoid desync. If using PostgreSQL, favor the Foreign Key approach.
>
> **Observation 2: ID Slugs**  
> Your ID Format (§5.1) used `PET` in some earlier notes but `PW` (Pet Owner) in others. I have standardized on `PW` for owners to match your User Types.
>
> **Observation 3: Data Precision**  
> `Height` and `Weight` are marked as `Float`. Ensure your FastAPI models use `confloat` or `Decimal` if precision is critical for medical dosages.