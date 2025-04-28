-- Tabla de Usuarios
CREATE TABLE users (
    user_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR2(100) NOT NULL UNIQUE,
    username VARCHAR2(20) NOT NULL UNIQUE,
    fullname VARCHAR2(75) NOT NULL,
    password VARCHAR2(12) NOT NULL,
    phone NUMBER(8),
    datebirth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Roles
CREATE TABLE roles (
    role_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    role_name VARCHAR2(50) NOT NULL UNIQUE,
    description VARCHAR2(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Asignacion de Roles a Usuarios
CREATE TABLE user_roles (
    user_id NUMBER REFERENCES users(user_id),
    role_id NUMBER REFERENCES roles(role_id),
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, role_id)
);

-- Tabla de Coaches
CREATE TABLE coaches (
    coach_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id NUMBER REFERENCES users(user_id),
    nickname VARCHAR2(50) NOT NULL UNIQUE,
    fullname VARCHAR2(100),
    bio VARCHAR2(300),
    total_sessions NUMBER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Servicios
CREATE TABLE services (
    service_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    description VARCHAR2(500),
    category VARCHAR2(50),
    price NUMBER(10,2) NOT NULL,
    duration_minutes NUMBER DEFAULT 30,
    is_active NUMBER(1) DEFAULT 1
);

-- Tabla Coaches-Servicios
CREATE TABLE coach_services (
    coach_id NUMBER REFERENCES coaches(coach_id),
    service_id NUMBER REFERENCES services(service_id),
    price NUMBER(10,2),
    PRIMARY KEY (coach_id, service_id)
);


-- Tabla de Productos
CREATE TABLE products (
    product_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    description VARCHAR2(4000),
    price NUMBER(10,2) NOT NULL,
    stock NUMBER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);