-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2023 at 05:31 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_pooling_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'sessions', '0001_initial', '2023-03-05 07:18:26.524584');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('u5jnuok0d6h45yoqmb1zoiu2clre7etv', 'e30:1pdtj5:KC0ezp6PoL59jzd8LMXSQxmiFdD0qAj_J35KH52RvSc', '2023-04-02 14:09:35.249090'),
('vxx6jomqynxt9g3xm4264nibiulxg251', 'eyJ1c2VyX2lkIjoxfQ:1prJPA:IAXs11SCiMBNuH7P7O029pC1wM5ZTkfjzd-1ZaHWGEw', '2023-05-09 14:12:28.860474');

-- --------------------------------------------------------

--
-- Table structure for table `ratings`
--

CREATE TABLE `ratings` (
  `r_id` int(11) NOT NULL,
  `r_given_by` int(11) NOT NULL,
  `r_given_to` int(11) NOT NULL,
  `r_for_trip` int(11) NOT NULL,
  `r_ratings` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ratings`
--

INSERT INTO `ratings` (`r_id`, `r_given_by`, `r_given_to`, `r_for_trip`, `r_ratings`) VALUES
(1, 1, 1, 1, 4),
(3, 1, 1, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `trips`
--

CREATE TABLE `trips` (
  `trip_id` int(11) NOT NULL,
  `passenger_u_id` int(11) NOT NULL,
  `trip_charges_paid` int(11) NOT NULL,
  `trip_status` varchar(255) NOT NULL,
  `trip_details_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trips`
--

INSERT INTO `trips` (`trip_id`, `passenger_u_id`, `trip_charges_paid`, `trip_status`, `trip_details_id`) VALUES
(2, 1, 100, 'Booked', 3),
(3, 1, 100, 'Booked', 1),
(4, 1, 100, 'Booked', 1),
(5, 1, 100, 'Cancelled', 4),
(6, 1, 100, 'Booked', 1);

-- --------------------------------------------------------

--
-- Table structure for table `trip_details`
--

CREATE TABLE `trip_details` (
  `trip_details_id` int(11) NOT NULL,
  `trip_from` varchar(255) NOT NULL,
  `trip_to` varchar(255) NOT NULL,
  `trip_date` date NOT NULL,
  `trip_driver_id` int(11) NOT NULL,
  `trip_car_number` varchar(255) NOT NULL,
  `trip_total_spots` int(11) NOT NULL,
  `trip_charges_per_person` int(11) NOT NULL,
  `trip_spots_available` int(11) NOT NULL,
  `trip_time` datetime NOT NULL,
  `trip_route_details` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trip_details`
--

INSERT INTO `trip_details` (`trip_details_id`, `trip_from`, `trip_to`, `trip_date`, `trip_driver_id`, `trip_car_number`, `trip_total_spots`, `trip_charges_per_person`, `trip_spots_available`, `trip_time`, `trip_route_details`) VALUES
(1, 'Juhapura', 'CG Road', '2023-03-05', 1, 'GJ01RN5249', 4, 100, 1, '2023-03-05 18:10:45', 'Through Paldi'),
(3, 'TP 85 ', 'Garima Park', '2023-03-05', 1, 'GJ01RN5249', 2, 100, 1, '2023-03-05 20:00:00', 'Via SG Highway'),
(4, 'TP 85 ', 'Garima Park', '2023-03-12', 1, 'GJ01RN5249', 3, 100, 3, '2023-03-12 13:45:00', 'TP 85 to Garima Park via SG Highway');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `user_pwd` varchar(255) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `user_mobile_no` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_name`, `user_pwd`, `user_email`, `user_mobile_no`) VALUES
(1, 'Sahil Mansuri', 'sahil1234', 'sahil.mansuri@gmail.com', '9974921248'),
(2, 'Heena', 'heena@1234', 'heena.mansuri@gmail.com', '9825010084');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `ratings`
--
ALTER TABLE `ratings`
  ADD PRIMARY KEY (`r_id`),
  ADD KEY `r_given_by` (`r_given_by`),
  ADD KEY `r_given_to` (`r_given_to`),
  ADD KEY `r_for_trip` (`r_for_trip`);

--
-- Indexes for table `trips`
--
ALTER TABLE `trips`
  ADD PRIMARY KEY (`trip_id`),
  ADD KEY `passenger_u_id` (`passenger_u_id`),
  ADD KEY `trip_details_id` (`trip_details_id`);

--
-- Indexes for table `trip_details`
--
ALTER TABLE `trip_details`
  ADD PRIMARY KEY (`trip_details_id`),
  ADD KEY `trip_driver_id` (`trip_driver_id`),
  ADD KEY `trip_details_id` (`trip_details_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ratings`
--
ALTER TABLE `ratings`
  MODIFY `r_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `trips`
--
ALTER TABLE `trips`
  MODIFY `trip_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `trip_details`
--
ALTER TABLE `trip_details`
  MODIFY `trip_details_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ratings`
--
ALTER TABLE `ratings`
  ADD CONSTRAINT `ratings_ibfk_1` FOREIGN KEY (`r_given_by`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ratings_ibfk_2` FOREIGN KEY (`r_given_to`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ratings_ibfk_3` FOREIGN KEY (`r_for_trip`) REFERENCES `trip_details` (`trip_details_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `trips`
--
ALTER TABLE `trips`
  ADD CONSTRAINT `trips_ibfk_1` FOREIGN KEY (`passenger_u_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `trips_ibfk_2` FOREIGN KEY (`trip_details_id`) REFERENCES `trip_details` (`trip_details_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `trip_details`
--
ALTER TABLE `trip_details`
  ADD CONSTRAINT `trip_details_ibfk_1` FOREIGN KEY (`trip_driver_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
