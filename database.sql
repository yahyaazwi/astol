-- إنشاء قاعدة البيانات
CREATE DATABASE IF NOT EXISTS fuel_management;
USE fuel_management;

-- جدول السائقين
CREATE TABLE drivers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    status ENUM('متاح', 'مشغول', 'غير-موجود', 'صيانة', 'سائق-جديد') DEFAULT 'سائق-جديد',
    license_number VARCHAR(50) UNIQUE NOT NULL,
    permit_ids VARCHAR(255), -- سيتم ربطه بجدول التصاريح
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT 'جدول إدارة بيانات السائقين';

-- جدول التصاريح
CREATE TABLE permits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    permit_type ENUM('وقود', 'شحنات', 'خاص') NOT NULL,
    description TEXT,
    valid_from DATE NOT NULL,
    valid_to DATE NOT NULL,
    driver_id INT,
    FOREIGN KEY (driver_id) REFERENCES drivers(id) ON DELETE SET NULL
) COMMENT 'جدول إدارة تصاريح العمل';

-- جدول الشاحنات
CREATE TABLE trucks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plate_number VARCHAR(20) UNIQUE NOT NULL,
    capacity INT NOT NULL COMMENT 'السعة باللتر',
    current_driver_id INT,
    status ENUM('متاحة', 'مشغولة', 'صيانة') DEFAULT 'متاحة',
    FOREIGN KEY (current_driver_id) REFERENCES drivers(id) ON DELETE SET NULL
) COMMENT 'جدول إدارة الشاحنات';

-- جدول الطلبات
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT NOT NULL,
    truck_id INT NOT NULL,
    order_type ENUM('توصيل', 'استلام') NOT NULL,
    quantity INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('مكتمل', 'قيد التنفيذ', 'ملغي') DEFAULT 'قيد التنفيذ',
    FOREIGN KEY (driver_id) REFERENCES drivers(id),
    FOREIGN KEY (truck_id) REFERENCES trucks(id)
) COMMENT 'جدول إدارة طلبات الشحن';

-- إنشاء الفهارس
CREATE INDEX idx_driver_status ON drivers(status);
CREATE INDEX idx_permit_validity ON permits(valid_to);
CREATE INDEX idx_truck_status ON trucks(status);

-- لتنفيذ البرنامج النصي استخدم الأمر التالي في محطة MySQL:
-- mysql -u اسم_المستخدم -p fuel_management < database.sql