# Notes API — Authentication & Foundations

## Overview
This project implements a **secure authentication layer** and the **foundations for a notes management system** using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

The work was done under **strict time constraints**, with a deliberate focus on correctness, security, and clean architecture over feature breadth.

---

## Tech Stack
- **FastAPI** — REST API framework  
- **SQLAlchemy (2.x)** — ORM  
- **PostgreSQL** — database  
- **Alembic** — database migrations  
- **JWT (PyJWT)** — authentication tokens  
- **bcrypt / passlib** — password hashing  
- **Pydantic** — request/response validation  
- **Docker / docker-compose** — local infrastructure (DB)

---

## What Was Implemented ✅

### 1. Authentication (Fully Implemented)
A complete, production-grade authentication flow.

#### Endpoints
- `POST /auth/register`
  - Registers a new user
  - Hashes password using bcrypt
  - Returns a JWT access token
- `POST /auth/login`
  - Verifies credentials
  - Returns a JWT access token
- `GET /me`
  - Requires Bearer token
  - Returns the authenticated user’s profile

#### Security Decisions
- Passwords are **never stored in plaintext**
- JWT includes:
  - `sub` (user_id)
  - `iat` (issued at)
  - `exp` (expiration)
- Secrets (`JWT_SECRET`, `DATABASE_URL`, etc.) are loaded from **environment variables**
- Refresh tokens were intentionally not implemented to keep scope minimal

---

### 2. Database & Models
- PostgreSQL database with Alembic migrations
- `users` table:
  - `id`, `email` (unique)
  - `password_hash`
  - `display_name`
  - `created_at`, `updated_at`
- `notes` table already exists in the schema
- SQLAlchemy relationships between `User` and `Note`
- Explicit model registration to avoid mapper/relationship initialization issues

---

### 3. Architecture & Code Organization
Clear separation of concerns:
- `api/routes` — HTTP endpoints
- `api/deps` — shared dependencies (DB, auth)
- `core/security` — hashing & JWT logic
- `models` — SQLAlchemy ORM models
- `schemas` — Pydantic schemas

The structure is designed to scale cleanly into authorization rules, sharing, and additional features.

---

### 4. Manual End-to-End Verification
All authentication flows were verified manually using `curl`:
- Register → token returned
- Login → token returned
- `/me` with token → `200 OK`
- `/me` without token → `401 Unauthorized`

---

## What Was NOT Implemented ⏳

Due to time constraints, the following planned features were **not completed**, although the groundwork is in place.

### 1. Notes CRUD API
Planned but not implemented:
- `POST /notes`
- `GET /notes`
- `GET /notes/{id}`
- `PATCH /notes/{id}`
- `DELETE /notes/{id}`

The database schema and ORM models already exist, so implementation would mainly involve:
- Adding routers
- Enforcing owner-only access
- Writing tests

---

### 2. Authorization Rules for Notes
Not yet implemented:
- Owner-only access to notes
- Returning `404` instead of `403` to avoid resource enumeration
- Note sharing logic (future stage)

---

### 3. Automated Tests
- No automated test suite was added
- Focus was placed on:
  - Correct DB schema
  - Correct authentication behavior
  - Manual end-to-end verification

Tests were planned as the next step.

---

## Design Rationale
Given the limited time, priority was given to:
1. **Security correctness**
2. **Clean architecture**
3. **Clear extension points**

Rather than implementing partial or fragile CRUD logic, the goal was to deliver a **solid authentication foundation** that future features can safely build upon.

---

## Next Steps (If More Time Were Available)
1. Implement owner-only Notes CRUD
2. Add automated tests for Auth and Notes
3. Introduce sharing and permission rules
4. Add pagination and filtering for notes

---

## Summary
This project delivers:
- A **fully working authentication system**
- A **clean, extensible backend architecture**
- A **ready database schema** for notes management

The remaining work is additive and can be implemented without refactoring existing code.
