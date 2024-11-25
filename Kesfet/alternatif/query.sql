CREATE TABLE `search_db` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `site_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
    `headline` TEXT NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
    `timestamp` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `search_url` TEXT NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
    `date_only` DATE NULL DEFAULT NULL,
    `time_only` TIME NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
