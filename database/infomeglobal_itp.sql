-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2023 at 07:01 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `infomeglobal_itp`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_speakerregistrations`
--

CREATE TABLE `app_speakerregistrations` (
  `id` bigint(20) NOT NULL,
  `first_name` longtext DEFAULT NULL,
  `last_name` longtext DEFAULT NULL,
  `designation` longtext DEFAULT NULL,
  `company` longtext DEFAULT NULL,
  `email` longtext DEFAULT NULL,
  `mobile` longtext DEFAULT NULL,
  `country` longtext DEFAULT NULL,
  `traveling_from` longtext DEFAULT NULL,
  `retun_date_time` datetime(6) DEFAULT NULL,
  `outline_talk` longtext DEFAULT NULL,
  `passport_copy` varchar(100) DEFAULT NULL,
  `photo_upload` varchar(100) DEFAULT NULL,
  `depature_date_time` datetime(6) DEFAULT NULL,
  `ksa_visa` int(11) DEFAULT NULL,
  `approved_by` int(11) DEFAULT NULL,
  `collected` int(11) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `print_status` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `app_speakerregistrations`
--

INSERT INTO `app_speakerregistrations` (`id`, `first_name`, `last_name`, `designation`, `company`, `email`, `mobile`, `country`, `traveling_from`, `retun_date_time`, `outline_talk`, `passport_copy`, `photo_upload`, `depature_date_time`, `ksa_visa`, `approved_by`, `collected`, `created_at`, `print_status`, `status`, `updated_at`) VALUES
(1, 'awdaw', 'awdawd', '', '', '', '', '', '', '2023-04-21 16:10:00.000000', '', 'user_None/wallpaperflare.com_wallpaper_2.jpg', 'user_None/wallpaperflare.com_wallpaper_1.jpg', '2023-04-22 16:10:00.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'awdaw', 'awdawd', 'fawf', 'awfawf', 'awfa', 'wfawfa', 'awfaw', 'awfawf', '2023-04-21 16:10:00.000000', '', 'speakerReginstration/awdaw/wallpaperflare.com_wallpaper_2.jpg', 'speakerReginstration/awdaw/wallpaperflare.com_wallpaper_1.jpg', '2023-04-22 16:10:00.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'mansoor', 'k', 'fawf', 'awfawf', 'awfa', 'wfawfa', 'awfaw', 'awfawf', '2023-04-21 16:10:00.000000', '', 'speakerReginstration/mansoor/wallpaperflare.com_wallpaper_2.jpg', 'speakerReginstration/mansoor/wallpaperflare.com_wallpaper_1.jpg', '2023-04-22 16:10:00.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'mansoor', 'k', 'fawf', 'awfawf', 'awfa', 'wfawfa', 'awfaw', 'awfawf', '2023-04-21 16:10:00.000000', '', 'speakerReginstration/mansoork/wallpaperflare.com_wallpaper_2.jpg', 'speakerReginstration/mansoork/wallpaperflare.com_wallpaper_1.jpg', '2023-04-22 16:10:00.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'mansoor', 'k', 'developer', 'infome', 'mansoor@gmail.cpm', '12345', 'india', 'dubai', '2023-04-22 16:25:00.000000', 'noo', 'speakerReginstration/mansoor/wallpaperflare.com_wallpaper_1_9xPWxZp.jpg', 'speakerReginstration/mansoor/wallpaperflare.com_wallpaper_1_sKzWEEX.jpg', '2023-04-26 16:25:00.000000', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'TEST', 'last', 'kochi', 'infome', 'emial@emial.com', '1234`', 'india', '121', '2023-05-02 16:43:00.000000', 'nop', 'speakerReginstration/TEST/783px-Test-Logo.svg.png', 'speakerReginstration/TEST/colorful-illustration-test-word-260nw-1438324490.webp', '2023-04-14 16:43:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'TEST', 'last', 'kochi', 'infome', 'emial@emial.com', '1234`', 'india', '121', '2023-05-02 16:43:00.000000', 'nop', 'speakerReginstration/TEST/783px-Test-Logo.svg_58PEhST.png', 'speakerReginstration/TEST/colorful-illustration-test-word-260nw-1438324490_x3Uq7N4.webp', '2023-04-14 16:43:00.000000', 0, NULL, NULL, NULL, NULL, NULL, NULL),
(8, 'TEST', 'last', 'kochi', 'infome', 'emial@emial.com', '1234`', 'india', '121', '2023-05-02 16:43:00.000000', 'nop', 'speakerReginstration/None/783px-Test-Logo.svg.png', 'speakerReginstration/None/colorful-illustration-test-word-260nw-1438324490.webp', '2023-04-14 16:43:00.000000', 0, NULL, NULL, NULL, NULL, NULL, NULL),
(9, 'adfaw', 'dadawdawd', '213', 'adaw', 'awda@gm.v', '1231', 'awda', 'awda', '2023-04-06 16:48:00.000000', 'adw', 'speakerReginstration/1231/783px-Test-Logo.svg.png', 'speakerReginstration/1231/783px-Test-Logo.svg_8QciVzw.png', '2023-04-15 16:48:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(10, 'dwad', 'awdawd', 'awdaw', 'awdaw', '1231@f.co', 'dwad', 'awdadw', 'awdawd', '2023-04-25 17:13:00.000000', 'awdawd', 'speakerReginstration/dwad/colorful-illustration-test-word-260nw-1438324490.webp', 'speakerReginstration/dwad/783px-Test-Logo.svg.png', '2023-04-08 17:13:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'dwada', 'dawdawd', 'awdawd', '2131', 'dawd@f.c', 'awdawd', 'awdad', 'wawd', '2023-04-05 17:15:00.000000', 'awdad', 'speakerReginstration/awdawd/colorful-illustration-test-word-260nw-1438324490.webp', 'speakerReginstration/awdawd/colorful-illustration-test-word-260nw-1438324490_u6ncqbS.webp', '2023-04-15 19:15:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(12, '', '', '', '', '', '', '', '', '2023-04-15 17:16:00.000000', '', '', '', '2023-04-23 17:16:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(13, '', '', '', '', '', '', '', '', '2023-04-22 17:17:00.000000', '', '', '', '2023-04-29 17:17:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(14, '', '', '', '', '', '', '', '', '2023-04-13 17:18:00.000000', '', '', '', '2023-04-09 17:17:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(15, 'adwawd', 'awdawd', 'awdaw', '213a', 'awdad@#g.c', 'awda', 'wdawd', 'awdaw', '2023-04-19 17:20:00.000000', 'awdaw', 'speakerReginstration/awda/colorful-illustration-test-word-260nw-1438324490.webp', 'speakerReginstration/awda/783px-Test-Logo.svg.png', '2023-04-15 17:20:00.000000', 1, NULL, NULL, NULL, NULL, NULL, NULL),
(16, 'mansoor', 'kk', 'dev', 'infome', 'email.com', '12345', 'dubai', 'kochi', '2023-04-10 10:19:00.000000', 'ooo', 'speakerReginstration/12345/colorful-illustration-test-word-260nw-1438324490.webp', 'speakerReginstration/12345/783px-Test-Logo.svg.png', '2023-04-10 10:19:00.000000', 1, 0, 0, '2023-04-10 04:49:43.350122', 0, 0, '2023-04-10 04:49:43.350122');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add speaker registrations', 7, 'add_speakerregistrations'),
(26, 'Can change speaker registrations', 7, 'change_speakerregistrations'),
(27, 'Can delete speaker registrations', 7, 'delete_speakerregistrations'),
(28, 'Can view speaker registrations', 7, 'view_speakerregistrations'),
(29, 'Can add user_db', 8, 'add_user_db'),
(30, 'Can change user_db', 8, 'change_user_db'),
(31, 'Can delete user_db', 8, 'delete_user_db'),
(32, 'Can view user_db', 8, 'view_user_db'),
(33, 'Can add buildpass_table', 9, 'add_buildpass_table'),
(34, 'Can change buildpass_table', 9, 'change_buildpass_table'),
(35, 'Can delete buildpass_table', 9, 'delete_buildpass_table'),
(36, 'Can view buildpass_table', 9, 'view_buildpass_table'),
(37, 'Can add build_designation', 10, 'add_build_designation'),
(38, 'Can change build_designation', 10, 'change_build_designation'),
(39, 'Can delete build_designation', 10, 'delete_build_designation'),
(40, 'Can view build_designation', 10, 'view_build_designation'),
(41, 'Can add eventpass_table', 11, 'add_eventpass_table'),
(42, 'Can change eventpass_table', 11, 'change_eventpass_table'),
(43, 'Can delete eventpass_table', 11, 'delete_eventpass_table'),
(44, 'Can view eventpass_table', 11, 'view_eventpass_table'),
(45, 'Can add eventpass_image_db', 12, 'add_eventpass_image_db'),
(46, 'Can change eventpass_image_db', 12, 'change_eventpass_image_db'),
(47, 'Can delete eventpass_image_db', 12, 'delete_eventpass_image_db'),
(48, 'Can view eventpass_image_db', 12, 'view_eventpass_image_db'),
(49, 'Can add eventpass_designation', 13, 'add_eventpass_designation'),
(50, 'Can change eventpass_designation', 13, 'change_eventpass_designation'),
(51, 'Can delete eventpass_designation', 13, 'delete_eventpass_designation'),
(52, 'Can view eventpass_designation', 13, 'view_eventpass_designation'),
(53, 'Can add vapp_table', 14, 'add_vapp_table'),
(54, 'Can change vapp_table', 14, 'change_vapp_table'),
(55, 'Can delete vapp_table', 14, 'delete_vapp_table'),
(56, 'Can view vapp_table', 14, 'view_vapp_table'),
(57, 'Can add vapp_vehicle_type', 15, 'add_vapp_vehicle_type'),
(58, 'Can change vapp_vehicle_type', 15, 'change_vapp_vehicle_type'),
(59, 'Can delete vapp_vehicle_type', 15, 'delete_vapp_vehicle_type'),
(60, 'Can view vapp_vehicle_type', 15, 'view_vapp_vehicle_type'),
(61, 'Can add vapp_category', 16, 'add_vapp_category'),
(62, 'Can change vapp_category', 16, 'change_vapp_category'),
(63, 'Can delete vapp_category', 16, 'delete_vapp_category'),
(64, 'Can view vapp_category', 16, 'view_vapp_category');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(3, 'pbkdf2_sha256$260000$kEMoj2q7rNhsOdVnPUnACm$MQGgmU2BL8Z4Q2eqjnNbsPRMc4nIURs2y3iAFbwLBcY=', '2023-02-18 17:47:21.266579', 0, 'Shadin', '', '', '', 0, 1, '2022-10-28 06:40:47.000000'),
(4, 'pbkdf2_sha256$320000$wX10yxIahwlGVkvoRg94Tz$/BEZ49GWsj3AlkbDGjtiM99OfalRtb4AVYskxHtXatw=', '2023-04-10 04:12:01.271934', 1, 'Don', '', '', '', 1, 1, '2022-10-28 06:42:35.000000'),
(5, 'pbkdf2_sha256$260000$vWw4L3pvPY9T76HhlsbD3m$sAS7jd3zXbdLvtcu4lH6ieONcv1qHfgTItDkaNYZYjM=', '2022-12-08 11:21:30.432329', 0, 'INFOMEUSER', '', '', '', 0, 1, '2022-10-28 06:43:30.989289'),
(6, 'pbkdf2_sha256$320000$vK0FIygQJY5kKhKjAb3Xrv$O8uFCD5zi2fWRYDa7fVmNFOxV/sshT/KAFtW6FqFNvQ=', '2022-10-29 11:27:02.148632', 0, 'MOTNSUPERADMIN', '', '', '', 0, 1, '2022-10-28 06:45:09.963050'),
(7, 'pbkdf2_sha256$260000$VaT263MscyQ2onyDYXdlxk$8FI0PHN0IcQCRJONfStJtCHv7nyr7WTHEI6RkU99E+o=', '2023-02-06 06:43:29.902750', 0, 'sreenath', '', '', '', 0, 1, '2022-11-10 07:15:59.000000'),
(8, 'pbkdf2_sha256$260000$ktl3W5WS9fTEks6jEHCkX0$osFXYFLcytw+2PZqM6bGFnkDWGK7jDBcceL3KAEwKmg=', '2023-03-20 08:40:53.718193', 0, 'Uvais', '', '', '', 0, 1, '2022-11-10 09:48:08.000000'),
(9, 'pbkdf2_sha256$260000$KtU38A4cL5fgQB4Y86Nura$1Mdlm3DJsgczBLIicNGcBGlTbSUctebu4mwc4bSVoD0=', '2023-03-29 10:12:46.006200', 1, 'mansoorgt700', '', '', '', 1, 1, '2023-01-25 10:23:48.562317'),
(10, 'pbkdf2_sha256$260000$J6gkC2t0r3zjiu0ERTtHCO$AmOlCKzBu1vHvC10WRjoRYQOGhLIcHck0WRgg/m0UYo=', '2023-02-09 11:44:05.415635', 0, 'kochi_dev', '', '', '', 0, 1, '2023-01-30 11:05:03.237720'),
(11, 'pbkdf2_sha256$260000$W2i6yLhsSTOHnKDKySlrdf$csqW3ohehoO20kUDFVeySLxoC5DLLXdTmrvhLs6qyZA=', '2023-03-14 10:32:06.131550', 0, 'dazadmin', '', '', '', 0, 1, '2023-02-01 11:37:30.500357');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'App', 'speakerregistrations'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'Portal', 'buildpass_table'),
(10, 'Portal', 'build_designation'),
(13, 'Portal', 'eventpass_designation'),
(12, 'Portal', 'eventpass_image_db'),
(11, 'Portal', 'eventpass_table'),
(8, 'Portal', 'user_db'),
(16, 'Portal', 'vapp_category'),
(14, 'Portal', 'vapp_table'),
(15, 'Portal', 'vapp_vehicle_type'),
(6, 'sessions', 'session');

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
(1, 'contenttypes', '0001_initial', '2023-04-05 07:32:04.835459'),
(2, 'auth', '0001_initial', '2023-04-05 07:32:07.986478'),
(3, 'admin', '0001_initial', '2023-04-05 07:32:08.614389'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-05 07:32:08.674091'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-05 07:32:08.696603'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-05 07:32:08.943722'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-05 07:32:09.224797'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-05 07:32:09.277146'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-05 07:32:09.298141'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-05 07:32:09.575770'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-05 07:32:09.592356'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-05 07:32:09.618360'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-05 07:32:09.675408'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-05 07:32:09.728190'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-05 07:32:09.776430'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-05 07:32:09.799637'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-05 07:32:09.856978'),
(18, 'sessions', '0001_initial', '2023-04-05 07:32:10.015981'),
(19, 'App', '0001_initial', '2023-04-05 10:29:06.883395'),
(20, 'App', '0002_speakerregistrations_depature_date_time_and_more', '2023-04-05 10:45:36.979902'),
(21, 'App', '0003_alter_speakerregistrations_table', '2023-04-05 10:52:07.697113'),
(22, 'App', '0004_alter_speakerregistrations_table', '2023-04-05 10:52:29.543435'),
(23, 'App', '0005_speakerregistrations_ksa_visa', '2023-04-05 11:11:40.144612'),
(24, 'App', '0006_speakerregistrations_approved_by_and_more', '2023-04-10 04:36:07.382777');

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
('01r1dgxfi9leym7wsweywhtu3viwtf1z', '.eJxVjsEKgzAQRP8l5yDJJmr12Hu_oIjsJmu1lQhRC6X03xuLB3sZmH2zw7xFi-vSt-vMsR28qIUR8ngjdA8OG_B3DLcpc1NY4kDZFsl2OmeXyfN43rN_BT3OffpWecmq6kzlDJ20sdQhWTpRqdgBcEGAeVFYpY3LK3DgsQNDyuUITImk0l9dnEYWtd7dtthIwU8OSzItxogvUV-tVlYmMY0UtA6jP0KwADKJ3kQ1ny9M71MU:1pBbo1:SRUQ7pK2lZQMHshPWkmxfougop8kSdr-YDeZF7U4GtU', '2023-01-14 13:21:45.881516'),
('04286q3seum6v4qwgb11l74vet6sylw2', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1os373:45QVcJaD9sLB9WiD2ItLfWwj30FeM1HI5h5PSs_mP9s', '2022-11-21 14:28:33.631065'),
('07mli5401th9pcx1artpb33cyutvdtau', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p1XDk:y3cPsIgpysBqoYhF4bf01J8QRhODtTbY4WW40pQEvz4', '2022-12-17 18:26:40.099032'),
('0ni4wfly2h1wrm3uzh5s938i0j8o3pae', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n18:mbqi7QTh1HIoV891WWI77JUBpOXmhCQnD9C38QHEpDU', '2022-12-15 17:06:34.140640'),
('0oqlz0woenliqmhuslhvzdxd3sno2t46', '.eJxVjr0OgzAMhN8lcxU1PyaBsTvPgJzYFFpEJAJT1XdvqDK0m8939-leYsBjn4Yj8zbMJDphxeX3FzA-eT0NeuB6TzKmdd_mIM-IrG6WfSJebjX7B5gwT6VtGqfHaFiRChxca1yDwYAHHpGQCGwE0MgO0Fv25Ww1QXv1QBi0VQX6xW1pYdGpqs7F5v0BIJlAqg:1phq4w:FowYBG3ORj9GiLLy86ApRssYOZs-X8vuhWiUmwDwxf8', '2023-04-13 11:04:26.260518'),
('0zg1zyps9vy4uz0rf4bveeo4nhb7t9t5', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1otlyv:NrIhjJGxRlyoXkcCgfhv-SwkU3VHjlpqCUwYHB8o8bo', '2022-11-26 08:35:17.118086'),
('1dp9zco97w5owvdrdo8l4uj9io3d36np', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n17:w4w7YoPCPKZ3ErQWSKttKJCabOzSBcqm4OCDG7D8viY', '2022-12-15 17:06:33.506180'),
('1fth4manw4zpvsjnxv6mqa8jiyexym2d', '.eJxVjEEOgyAQRe_CuiE4YEGX3XsGMjBDtTWSgK6a3r3auGi3_73_XsLjto5-q1z8RKIXWlx-t4DxycsB6IHLPcuYl7VMQR6KPGmVQyaeb6f7FxixjvtbRcMpNgStDmyNbbBDaLrkVEzKxARXBYa0hZatBa2UhmSZHbXGuIBuj35zJc8senh_AAgoPBc:1ook0a:ujgVfXYstqAJY-rv9h86pj-RpE7qtrgSGZe6lotdJto', '2022-11-12 11:28:12.480661'),
('1p6qnoq2upk3k3ayopwafrryo1fmyzjq', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p2UsQ:NWYMLLqa53tMu5Cf9sYBP7lAK2tOpikHjbYrIFbORng', '2022-12-20 10:08:38.425281'),
('24yiium0qujy7itdbmc3rvnybm79tixj', '.eJxVjsEKgzAQRP8l5yAxazR67L1fUER2k221FQNRC6X03xuLh3oZmH2zw7xFh-vSd-vMsRu8aAQI-X8jdA-eNuDvON1C5sK0xIGyLZLtdM7OwfN42rOHgh7nPn2zrh243DBTYcGo2lm8Fl5pIqtKQMxVZbWlqwWqLJSKyPhSOQZGX2pOpb-6GEYWTb67bbGRgtZh9Ml0GCO-RHPJoa5lkqqVgp88LQdoCpBJdPv5As5_UoA:1pU06C:whWUIlT47zHSJ4zjCddF9xuG_1uhLJ5hWkpOhCzkkRc', '2023-03-06 06:56:32.807894'),
('25zfi1b1u9gcrhwyg17u0k7bqm0bpcpb', 'e30:1ooJIS:EX2V5o9WlCaxmSUEfW7Z9IHHYuKwbWuT49FZT1Sw5o4', '2022-11-11 06:56:52.688593'),
('2jummuajt2ycmgtlgxhkfwtg3oygr2zu', '.eJxVjsEKgzAQRP8lZxETN7Hx2Hu_oIhssptqKwpRC6X03xuLh3oZmHmzw75Fi-vStevMse1J1OIksv_MoX_wuAG643ibcj-NS-xdvlXync75ZSIeznv3MNDh3KVrcNKRITSkKgXKgwNC0KARrAm6tJiC0hsNFWkMXASuArJV1knFFtPoby5OA4ta7m772GTCrf1AybQYI75EfZVQQJak3EQ2meAnj8uxYVWCVjafL40wU9I:1pU1GZ:LOp8wH-fUhRJOZwDXXMpalv9kK6UwfVg_vLOZrlsLME', '2023-03-06 08:11:19.615512'),
('3ay2nugvg993m3b49pobhk53f1h1yk37', '.eJxVjk0OgjAQhe_StWmYotMOS_eegUw7raCEJhRWxrsLpgtdvr8v76V63tah30pc-lFUpwDU6df0HJ5xPhJ58HzPOuR5XUavj4quadG3LHG61u4fYOAy7OsWgJKz6FGcESNeMIExHLxFTudGrCMCaRgFrcAFnSOOgYliQ20wO_SLW_IUVQdVHZfd-wMqTECR:1pc1ws:t81UsiSwoePqi1Jv42nIa34uxa2qf591_Bdlc_Yz49U', '2023-03-28 10:32:06.140519'),
('3iirio5kj127a1zzr3e1x48z470hub6l', '.eJxVjsuqgzAQht8l6yBxxnhbdt8nKEVmkvHoqShELZTSd29SXLSbD_75L8xTdbRvQ7evErrRq1ah0t83JneTORn-n-a_JXPLvIWRsxTJDnfNzouX6XRkfwYGWofYNrYS0_TYOOQ6x4J74oJrrow4ACkZyJZlYXJ0tgEHnnpANs4SCEcnjn7mwjKJavNDpY9RK97HyUfRUQj0UO0FsKl1RJVQJtgETMivWsld5u27gICgEQCurzcA-1Yx:1p3xl8:vXXv4LSXDRdSCVR5CDhj2eEZp00RJn3j7tvjsARDcRI', '2022-12-24 11:11:10.094388'),
('3ovd07yltsz2of87s9x95gvcrd8zx4za', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n16:-n0GylobUQ6x9g4jsbnHzKWgpnI7Q4ZPIzC_2_jrpEs', '2022-12-15 17:06:32.296147'),
('3rse3vvgpwlcvgmtr9sdya4p4s7ayz5g', '.eJxVjk0OgyAQhe_CuiGDwIAuu-8ZDDBQbA0kqKumd682Ltrl-_vyXmx025rHbYltnIgNTAC7_JrehWcsR0IPV-6Vh1rWNnl-VPiZLvxWKc7Xs_sHyG7J-1r61MsQtETsMIEGCxCU6skYiMko9AqlQ0sgyEInAwJ6geSdFkaT3KFfXKtzZIM41XHZvD_p5z9-:1pPGe7:N3Vx1WqDXaLDJ8-2S4bsCcrVGp06IHq18L2GqnsXn_k', '2023-02-21 05:35:59.130714'),
('4enzs820s7r5zl1d4mntlj30c8sq7rhg', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1owGRv:7ob24FTObRVewT1bh_g85-rWJ5K3flz8v9-TIXftoWc', '2022-12-03 05:31:31.994909'),
('5dtntqf6jk00gm3ntv5n7etp43us9o92', '.eJxVjEEOgyAQRe_CuiEwYEGX3XsGMjBDtTWSiK6a3r3auGi3_73_XiLgtg5hq7yEkUQnjLj8bhHTk-cD0APne5GpzOsyRnko8qRV9oV4up3uX2DAOuxvlSznpAkaE9lZp7FF0G32KmVlU4arAkvGQcPOgVHKQHbMnhprfUS_R7-5pUwsOv3-AAgmPBY:1opom0:tG9KgZVTKHw8HQoEo_mRRY7C6GQwOvlA7IUVsJ_eMU8', '2022-11-15 10:45:36.437247'),
('5oquxmm9jm35mm4ya6crgxrnhcijy9gz', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p54BO:93HCg8sGh2_l6_Jc9ZyahVSUiMEKRmfyCMIEnMONBSI', '2022-12-27 12:14:50.800204'),
('5rphx5h7b8al3kg44dlprxbxec64eqem', '.eJxVjsFuhCAQht-FMzEwI4gee98n2GzMDGC1NbpB3aRp-u6FxoM9zJcM_zd_-BY9HfvYH1tM_RREJ1DI6xuT_4xLCcIHLe9r5ddlTxNXRanOdKtua4jz2-n-KxhpG_O1Mk1U7YCtR3Yaax6Ia3bcqOgBomUgY22tNHrTgodAAyArbwgi5ySX_tWldY6i0-dWfoxS8DHNIS89pURforuDcY3MsAWmoC7AhxTxFZf96qKzWqIDI7GpsUBn7UXP59WyoKUFJa1u87jHzy8P_GD3:1pBBBU:vznoAIqvjZiw4zgBJua34TtuVpcwQSv4vvqfP62VXv0', '2023-01-13 08:56:12.366652'),
('63gxyhkh1g264n53qphqyd40993zhgma', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p7bqW:zWsn6B54lUmqarLl2HC-m176RKuUGk01BzX99eQNxO0', '2023-01-03 12:35:48.411361'),
('67ras5el6oz138oxik9le0qe0svj4wvk', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n18:mbqi7QTh1HIoV891WWI77JUBpOXmhCQnD9C38QHEpDU', '2022-12-15 17:06:34.534974'),
('6ei7kwelrevh8gho312b5ncz30lgx8y0', '.eJxVjssOgjAQRf-la9O0HVoGlu79BjLTDoISmvBYGf9dMF3o8r5O7kt1tG9Dt6-ydGNSrQJ1-fWY4lPmM0gPmu9Zxzxvy8j6rOiSrvqWk0zX0v0DDLQOx1pcEyFaL8IVgjdNROqrZBwzmgBE1tTokHsErhGCYfYpmCgglIKTA_rFLXkS1dqizsf-_QENVkCb:1pMo8A:Zkln8uLnqSvbltT5jKCCq04H2AqdjQQBdO56OABjYTM', '2023-02-14 10:44:50.323865'),
('6rucmshik6wvjip2p870odq8h25q2r1n', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p36fD:U30irquH6Tpd_e9Z5cr5tXX06IiBiJBKguyQoVXYog8', '2022-12-22 02:29:31.893399'),
('6yim17sezxuvujq2v1d5uede3p6lrxwn', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p8Mcf:EKrkPHgGTWHyawPqNeFO4gbrmtCVb3_GmiteJsDc5Vo', '2023-01-05 14:32:37.390544'),
('7c5vhlv9doqnt9jph7zjiwyfk3wao82b', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p3VXq:zir7VvFj-lTvBJ9ifOEWSGD96xaACr9GB7HDnYEnDbU', '2022-12-23 05:03:34.496483'),
('7d8bui3qtpw4czeqxwcv0e9du9yo3yh0', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n19:AwLambbzkKqtwjFFdlxwBT-NNkALmhYVRdiMREpdErU', '2022-12-15 17:06:35.268769'),
('7e7unt5zowj2u9qf03tbvze48ct8aozr', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1ovZ47:8w4Q4yiGMMPBUB_xY38zjUHTcIuYvH_ovglcV6lfOVQ', '2022-12-01 07:12:03.852197'),
('7jllae10a1tx9apk5a8cwpxf1ynrbvz2', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p4euZ:oaplfIfyJ3zdJK_kRUPeVIlLqOVd5BEDvGAsGjykmBs', '2022-12-26 09:15:47.085828'),
('7uw9xmce06ksuqxn0sjufeheyj32fkut', '.eJxVjssKgzAQRf8l6yBONCa67L5fUEQmcVJtJZH4gFL679Xiou7u3Mdh3qzBZe6aZaLY9C2rmGT83zNon-T3oH2gv4fEBj_H3iR7JTnSKbmGlobL0T0BOpy6be3Sgqy2TuosLwhKWWhlpDCpc9aIEsCVGlSbCS0tSlCSCg1WgSwzkxO6DfrDxTAQq8Rx7R_nnK04jptuMEZ8seomONSc0Up-Ptn15wvwzU62:1p2vlK:RtV0Zx1i6HmqkjOJIdWF192em9MUgIJZZwVcde_75rI', '2022-12-21 14:51:06.772926'),
('7z5ystqhayqkpt63veexqifznuot1fqo', '.eJxVjEEOgyAQRe_CuiEwYEGX3XsGMjBDtTWSiK6a3r3auGi3_73_XiLgtg5hq7yEkUQnjLj8bhHTk-cD0APne5GpzOsyRnko8qRV9oV4up3uX2DAOuxvlSznpAkaE9lZp7FF0G32KmVlU4arAkvGQcPOgVHKQHbMnhprfUS_R7-5pUwsOv3-AAgmPBY:1oq5LH:h-G322eUp9enOyBbhdeW4M0-426IHPQNLKUWDXNRflo', '2022-11-16 04:27:07.966041'),
('7zhbzouly0ffssomrl4p6u93a0ef6drc', '.eJxVjssKwjAQRf8l6xLSTNPX0r1fIBJmkqmtSgJpK4j476bShS7vnHsP8xIW12W068zJTl70AkTxeyN0Nw4b8FcMlyhdDEuaSG4VudNZHqPn-2Hv_glGnMe8VqZh1Q3QOaC2hIoGpIpaahQ7rbkmjaauK1WCM5122uOggZQzqJkyydKvLsU7i77c0_YxFIIfHJYcLKaET9Gfzu8PUEtHiA:1p7C5c:hgJ0ueWmCK-AjDo4zepqhXFiQVLQ-4-UWWIuXbB3aBs', '2023-01-02 09:05:40.248758'),
('8u8kkcove8jttwl2cvsnpqv4g5bw1k0x', '.eJxVjDEOgzAQBP_iOrJsc4ChTJ83oLNvCSQISxiqKH8PRBRJuzM7L9Xxtg7dlrF0o6hWVeryuwWOT8wHkAfP96RjmtdlDPpQ9EmzviXBdD3dv8DAedjfHn1JBjE2Ho68eKlAaGprUYuzgRCEmYqGbOlMX3OwBQHOhOiKypk9-s0taYJq7fsDKZs8pg:1oofqm:YCbzvcnmQYxBG22BHLtVStEd7U6Zc4xLclKzACIEbcg', '2022-11-12 07:01:48.437189'),
('8w7qz9htlpdpp5efcjqx0ws4rc8gwdvl', '.eJxVjk0OgjAQhe_SNSEtQ2nL0r0nMKSZ_igooaSAiTHe3dawkMVM5s335mXeROO29npbfNSDIy0RpPjfGbQPP2Xg7jjdQmnDtMbBlNlS7nQpz8H58bR7DwE9Ln269mCVQF5dQTJmXS0Nd3UjnDKIgIpKXguwzNr6yllTgQTpueUUOFKpKE-hv7gYRk9atqv8cZrNNowuCY0x4ou0FwaCFgwalZvsCvLEeT4aEq9Eqqb7fAFA4lJR:1pTnWj:v7FBYfqm55OkgD3ODxz4xPsZwIU5y6AswIRHNYB8Qvg', '2023-03-05 17:31:05.226812'),
('939gi1hm5t5vyizx6ysoixp5hmvc9qja', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p4QM1:l2ttz5sIhCFGWfVZYPCVN6X-BxIRJ38SnGRw56tv078', '2022-12-25 17:43:09.352250'),
('9m2ci1p9btzyryajnl6n7z44itx6fbg6', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1pNrUo:tKos0kbWFe4StlbYPTgD04tOdRSRWQjPOB7JxJwZs4c', '2023-02-17 08:32:34.926946'),
('a5qb3u9803n9i22ddeegh3cfd2jbmhsf', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1pTKcw:s95L7C9leccy-lFKojpdm4t745biwMrRoU_rR1Ut1J0', '2023-03-04 10:39:34.348500'),
('ajbk537djqp3k3ix7y5e8drmoeml0xe6', '.eJxVjEEOgyAQRe_CuiEwYEGX3XsGMjBDtTWSiK6a3r3auGi3_73_XiLgtg5hq7yEkUQnjLj8bhHTk-cD0APne5GpzOsyRnko8qRV9oV4up3uX2DAOuxvlSznpAkaE9lZp7FF0G32KmVlU4arAkvGQcPOgVHKQHbMnhprfUS_R7-5pUwsOv3-AAgmPBY:1oqC6A:kBEzHyWzbfbS7Igxm1uEeQ7wzbAQRwqqrfkAoe51GRg', '2022-11-16 11:39:58.672340'),
('auvmlrcqevnzz4rtvf8ppaxi1b7wnywe', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n15:EIdQQsseHEnKVBefnUsPr7wqCKBAaPAA2ofWR48SpE8', '2022-12-15 17:06:31.417605'),
('bjut4z25poq4t2qstl8giepqyrfm6216', '.eJxVzk2KwzAMBeC7eB2CLdv5W3bfE5QSJFuZZBoScJJCKXP3sYYsOpsP5Cc_9FY9HvvYHxunfoqqU1YVn2-E4cGLBPEbl6-1DOuyp4lKWSnPdCuva-T5cu7-KxhxG_Nv7WvW7WDbYKkx1tGA5KihWnMA4IoAfVU5bWzwLQSIOIAlHTwCU05y6V9dWmdWnTknudgWip-87HnoMSV8qe7mjDFFRmd0KzRCLVSCF5xgBbgXio5pjp8lUBt3__kF0klY3w:1pDPo8:xSKxzEMVuqNXl7RV56XqaDJoMT3_dwroupB9LO1klM0', '2023-01-19 12:57:20.722884'),
('bt5iqnzt3hz1e1n3wf2ya58rpbvegmmx', '.eJxVjEEOgyAQRe_CuiEwYEGX3XsGMjBDtTWSiK6a3r3auGi3_73_XiLgtg5hq7yEkUQnjLj8bhHTk-cD0APne5GpzOsyRnko8qRV9oV4up3uX2DAOuxvlSznpAkaE9lZp7FF0G32KmVlU4arAkvGQcPOgVHKQHbMnhprfUS_R7-5pUwsOv3-AAgmPBY:1opOvu:HkztG2GqHTd7EN1Eg0TXjkUaoYUwg5lxIKD3OIwY4D0', '2022-11-14 07:10:06.930068'),
('c5118fcpxjzzyof2r2lcjxhqc19s27p9', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p2USc:ul3dny6mGzT55XGCD4Y5FAZvxrww2T5-tRh0mhaRzdQ', '2022-12-20 09:41:58.906126'),
('c7yn3k40tumlxnfyngj5ulyn4xi1k4f2', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p3nbF:zgsxRkKsxemWQ0502evChCEMsZlS1fTScWfngBEtT_4', '2022-12-24 00:20:17.006054'),
('ce620e6rjvmb2p1ifm6nzzkivrivnlnz', '.eJxVjEEOgyAQRe_CuiEwYEGX3XsGMjBDtTWSiK6a3r3auGi3_73_XiLgtg5hq7yEkUQnjLj8bhHTk-cD0APne5GpzOsyRnko8qRV9oV4up3uX2DAOuxvlSznpAkaE9lZp7FF0G32KmVlU4arAkvGQcPOgVHKQHbMnhprfUS_R7-5pUwsOv3-AAgmPBY:1opMbX:MmNptB-RfU5O_xkqTKinguYLK8GHJpndWMELwnUrI9I', '2022-11-14 04:40:55.019920'),
('ewbchix7npw2hk4fg04pp2hwjg4hebhm', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1oqytP:a-_sne5k7VkuaPbHrlEvqz0E18XDe9ns2VAxSmtfzZU', '2022-11-18 15:46:03.045889'),
('exyjm5h4if933h37ty0g32aw5ufoilo9', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1pADR8:adAa4-Lc1UALNmIr6PrnT-nE_Ch20oLbfNeuq48F394', '2023-01-10 17:08:22.359749'),
('f0r810h4ozj6bk9jg5cituf7sbvaspxh', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1phT3K:PyjkWGbD__UsO-VsTJu3S5dcX_zxq-t9EgORWryMQSs', '2023-04-12 10:29:14.848241'),
('fhhkwe21qt5ce7yjfcl9s0e2t6jctap9', '.eJxVjk0OgjAQhe_StWmYotMOS_eegUw7raCEJhRWxrsLpgtdvr8v76V63tah30pc-lFUpwDU6df0HJ5xPhJ58HzPOuR5XUavj4quadG3LHG61u4fYOAy7OsWgJKz6FGcESNeMIExHLxFTudGrCMCaRgFrcAFnSOOgYliQ20wO_SLW_IUVQdVHZfd-wMqTECR:1pViKY:GAJpvqwkw7hKSMIRAsFNCBH7EejcQpXUvbj6PUBdepM', '2023-03-11 00:22:26.339369'),
('fv6h6ytsnu3foc5i0z8g5uoy8fvo8xuf', '.eJxVzsEKgzAMBuB36VmkTa1Wj7vvCcaQpMbpNhSqDsbYu68ZHrbLB-mf_uSlWtzWod0Wju3YqUZZlf2-EYYbTxJ0V5wucx7maY0j5bKS7-mSH-eO74d9969gwGVIv7WrWNe9rYMlb2xBPVJBnirNAYBLAnRlWWhjg6shQIc9WNLBITClJJV-6-J8Z9WYfZKLbab4wdOahhZjxKdqTuB8nSW8UAml4IRCsAIIRtDn9wfiqFFX:1p3F3K:ompFkpIAmdXJxIwztknVjnl8TXfdGgRtz74Ut02C7LU', '2022-12-22 11:26:58.678830'),
('g0mwcvfx3n0bf1x7e9ttarh2r9qh6i6d', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1pOEjQ:pKXgENpP6LDhM1yHrRFWQqEE4kqzuZR8A0pI0UxPFEk', '2023-02-18 09:21:12.312238'),
('g7polu7fg1532ljgflpwqqunugk2hy1n', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p4GRC:qf3vEk6uZ9M9KOw3LGSdv4Cux694dqN9VMq392JqFjU', '2022-12-25 07:07:50.080452'),
('g95slfj34s3i2a0d5c0wzwf5o4b0m2hg', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1osiRA:A7ykd0ucZllo__KE54york9QLJPkynI1f3n5VHzKELw', '2022-11-23 10:36:04.935160'),
('glj3wla89o73yp0jmndmk6vpvpreees4', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n19:AwLambbzkKqtwjFFdlxwBT-NNkALmhYVRdiMREpdErU', '2022-12-15 17:06:35.245825'),
('gtdxp8db06uv8stz9chbhctlr49oqrin', '.eJxVjssOgjAQRf-la9O0HVoGlu79BjLTDoISmvBYGf9dMF3o8r5O7kt1tG9Dt6-ydGNSrQJ1-fWY4lPmM0gPmu9Zxzxvy8j6rOiSrvqWk0zX0v0DDLQOx1pcEyFaL8IVgjdNROqrZBwzmgBE1tTokHsErhGCYfYpmCgglIKTA_rFLXkS1dqizsf-_QENVkCb:1pMoE5:eWXJaC9wMvAI-M3A3mr9zduRQBDLUoRvRfVml3Hft9c', '2023-02-14 10:50:57.781533'),
('h72s78xkzk2xj6fxlr313dqzjv9ukvzv', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1orBHT:CNIxagnkZv-_KXLKbQahkGtCzJu332q0z8Y0txlaqa4', '2022-11-19 04:59:43.827677'),
('h8sdu6n1mg8z94om8nf0as52ks1lwnfs', '.eJxVjs0OgkAMhN9lz4Tstsvv0btPYAxplyKogWQBE2N8d4vhoIfvMJ3pZF6moXXpm3WW2AytqQ2a5PfGFG4ybkZ7pfEypWEalzhwukXS3Z3T49TK_bBn_wp6mnv9tlkhtuqwCsilQ88dseeSCysBQHIGyvLcW4chqyBASx0g25ARCKujpd-6ON3F1G5X22JMjDxkXFQ0FCM9TX3y6BIPlVIqhZIrqIDizu8PTQdNkg:1p3EsG:LJCcMyLW2faPpmlg6NTyEo8UxEoob7POsWYGaHZ5sPQ', '2022-12-22 11:15:32.832311'),
('h8ymivr3ja9kc73vgpo5haimp9lddkm9', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n17:w4w7YoPCPKZ3ErQWSKttKJCabOzSBcqm4OCDG7D8viY', '2022-12-15 17:06:33.845260'),
('hnhpxx0sw4g88agfokao7up5wj0c0p5p', '.eJxVjssOgjAQRf-la9O0HVoGlu79BjLTDoISmvBYGf9dMF3o8r5O7kt1tG9Dt6-ydGNSrQJ1-fWY4lPmM0gPmu9Zxzxvy8j6rOiSrvqWk0zX0v0DDLQOx1pcEyFaL8IVgjdNROqrZBwzmgBE1tTokHsErhGCYfYpmCgglIKTA_rFLXkS1dqizsf-_QENVkCb:1pMoBx:lXj5UpCy-8d2eZEUcru7pPgkuF_e0EuPNXOHYPaHjug', '2023-02-14 10:48:45.805356'),
('hnz1wzpnv00dsk3g4nk1501jgdx6kn8w', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1oqaPb:djnZVYHn9JhLpxXmfLv-akmTzL176mYb646MiRaZ3kM', '2022-11-17 13:37:39.217691'),
('i2jyzpqvaowqcc46cu0mgk05k2r0d5l9', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n19:AwLambbzkKqtwjFFdlxwBT-NNkALmhYVRdiMREpdErU', '2022-12-15 17:06:35.457744'),
('icm5ewvjljg1kgby6zabjdyhlfp8v7ul', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p03Q1:3JYSPv4odV_DeLTD-mV8xEawIMq6HRUiqHjgGg0CLlw', '2022-12-13 16:25:13.683596'),
('icqpq65nva4xwcgq13gzukf0wtaneiit', '.eJxVjEEOgyAQRe_CuiEwYEGX3XsGMjBDtTWSiK6a3r3auGi3_73_XiLgtg5hq7yEkUQnjLj8bhHTk-cD0APne5GpzOsyRnko8qRV9oV4up3uX2DAOuxvlSznpAkaE9lZp7FF0G32KmVlU4arAkvGQcPOgVHKQHbMnhprfUS_R7-5pUwsOv3-AAgmPBY:1opjbp:vUw_M_BWEOTQ3oNxC7E3AtDTavAfvi-4tNPZNH1Cugs', '2022-11-15 05:14:45.656144'),
('ihj6yjklw6079bsd8sui2hq9ze7zitww', '.eJxVjssOgjAQRf-la9O0HVoGlu79BjLTDoISmvBYGf9dMF3o8r5O7kt1tG9Dt6-ydGNSrQJ1-fWY4lPmM0gPmu9Zxzxvy8j6rOiSrvqWk0zX0v0DDLQOx1pcEyFaL8IVgjdNROqrZBwzmgBE1tTokHsErhGCYfYpmCgglIKTA_rFLXkS1dqizsf-_QENVkCb:1pTRIv:GwzaFIgfg8L6x2GIMvdufDFwdG3n_RLF2rIaDQJr048', '2023-03-04 17:47:21.276665'),
('ioufiuss8i14v1e8pzu27yxqv4qpi2ef', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p4fuU:9IGO5n8q6abxOLSrPHAmQup3QOZ-VRjtU2sm_Hit9RA', '2022-12-26 10:19:46.580200'),
('iybkzdgbwfjd8e9pa53rq5idshjapmes', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n16:-n0GylobUQ6x9g4jsbnHzKWgpnI7Q4ZPIzC_2_jrpEs', '2022-12-15 17:06:32.427618'),
('jlhu4oojsvvnygknmebs33m6v13l4mj3', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p0eRt:kx9EioBfj-kIu-7bzJmYDw3qnxIeFnfLVp1PHmZ65hA', '2022-12-15 07:57:37.297184'),
('kflxh1c6j2m6z6gu0bw2qr911xodx1w6', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n17:w4w7YoPCPKZ3ErQWSKttKJCabOzSBcqm4OCDG7D8viY', '2022-12-15 17:06:33.257507'),
('kwdsbgjnwt4nqw1cbaha7vsemjvya7we', '.eJxVjk0OwiAQhe_C2hChA5Uu3XsGMjCDVJuSlHZlvLvUdKHL9_flvYTHbc1-q7z4kcQgLuL06wWMT573gB4434uMZV6XMci9Io-0ylshnq5H9w-Qsea2hqACWUJLutegIwQgBAMGwdlkOofN6KI10JPBxOfEfUJ22gWl2WGDfnFLmVgM6lD7Y_v-ACfHQQ4:1peB4X:fZB9h3f05RWbYeo6WHP4FHNWoqNA7iLjw8ne9Wm8w9Q', '2023-04-03 08:40:53.725355'),
('lqutvw3dbi1oz0gq8h5g974tbsjksmke', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n17:w4w7YoPCPKZ3ErQWSKttKJCabOzSBcqm4OCDG7D8viY', '2022-12-15 17:06:33.915173'),
('m6ryb221xyg1mjnt0dspwfwxhq9palp9', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1oqytQ:TxNqrTLVUMBmg4cmFiwzm7MfQT5HAL7rN21N8blhGRA', '2022-11-18 15:46:04.489124'),
('m758srrzkr12gcbeh88wmpmo6wh8h5a8', '.eJxVjsEOgjAQRP-l54Z0aZEuR-9-gSFk2y6CEiAFTYzx3y2Gg14mmZ2Zl32Jhu5r19wXjk0fRCWMkL83R_7G4xaEK42XKfPTuMbeZVsl29MlO02Bh-Pe_QN0tHRprb1H3xbaMkLQgG1Rcq5cG3Tg1oBzB4VoDWijtMoBcrKmBCw1IVkEn6BfXJwGFhXsbvtYS8EPHtdkGoqRnqI6Q9rKJCrJAWspHjTPvwVbSGvq9wdeYVFG:1paF7M:m16CijkHdDOLT7eIyxHdBXUMzUSRaU5vXPFhXhiPChs', '2023-03-23 12:11:32.833016'),
('mhlgd8ms1gn9qdrm83rr35kow9zir14a', '.eJxVjksOgzAMBe-SNUIOIQ6w7L4nqBBy4lBoEaDwkaqqdy9ULOjOnvc88ltUtMxNtUw-VC2LQkgQ0Rlack_f7wk_qL8PsRv6ObQ23ivxkU7xdWDfXY7un6Chqdmula1z5ZxWiAnWoCEDcGmaszHga5OiTVERZgySM0iUQ0ArkS1paTSrTfrThaHzopDHtr9sIrHSOG5zRSHQSxQ3LCNhl7bjM1R6x371_XzG5ecLPOpVXw:1pSHVo:q5cKEYkpCCZjcIPAoPbbVGyM-iSkvvkaDTff2LU8_zw', '2023-03-01 13:07:52.297552'),
('myxt4bf14p8iwcppxzvhmemd1ucwrtm9', '.eJxVjr0OgzAMhN8lcxU1PyaBsTvPgJzYFFpEJAJT1XdvqDK0m8939-leYsBjn4Yj8zbMJDphxeX3FzA-eT0NeuB6TzKmdd_mIM-IrG6WfSJebjX7B5gwT6VtGqfHaFiRChxca1yDwYAHHpGQCGwE0MgO0Fv25Ww1QXv1QBi0VQX6xW1pYdGpqs7F5v0BIJlAqg:1phkdq:dtJrP4-j7-wcO5jWNQBjX-f6aONk04kuFMzhY6pD394', '2023-04-13 05:16:06.628692'),
('n0v82609ycpjpvhkmrwwbp4ijhkxcpko', '.eJxVjDsOwyAQBe9CHSHD8rPL9DmDtSwQnFggGbuKcvfYkYukfTNvXmzEbc3j1uIyToENDNjld_NIz1gOEB5Y7pVTLesyeX4o_KSN32qI8_V0_wIZW97fHqxMqMGSJoXOOEHSx5SMdwSBqAdUDpK1TkjTWSATUzAdWOw1KDJ79Jtb6hzZIN4fIrg8jw:1os0Xq:rN6-6KwjoOeRR1EsooU9mTxDcZRMSl4OxVXyfzCjNe0', '2022-11-21 11:44:02.193577'),
('n6p8na9evxk2cyjidrcpygzh0j7a05kq', '.eJxVjMsOgjAUBf-la9O0t8VSl-75BnJfCGpoQmFl_HclYaHbMzPnZXrc1rHfqi79JOZiojn9boT80HkHcsf5ViyXeV0msrtiD1ptV0Sf18P9Oxixjt-aOHFCgkEDNbEBQBUg4Mbj4AJnF5M4l9sovs1ZPSOl7M5CmnwECeb9Af4nOCE:1ooJ8P:tTrEMnSBGumYqgkprvgVY0g7YW8__l5JembcS_RffRc', '2022-11-11 06:46:29.626952'),
('nbdcuxdtq7px2gncfopuftuogbm4hcj3', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n14:qJThgV6mU5mEZQjItecDxYMyYeSSExcKPSr8PKLLJW0', '2022-12-15 17:06:30.729724'),
('nsl6zz7fp051guzwn0ssrus2tuj4xx97', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p090E:TMYrd-demPcZF8piVxMMGnwvh78tfdqE8KF4Mki6O6c', '2022-12-13 22:22:58.832938'),
('o6suv8r6py4r08mqylmlsvjjllv2n3u1', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1otivu:6H_dmyU5al_PiAGMDzQc7eIdULGcUY6w5ckr1xa0UtU', '2022-11-26 05:19:58.572591'),
('ohl5kisk3qw3e6hs825aqel5ztjldzfo', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1oxNqV:BWDxgkWTB7nMtpquAqADfyzG37lEwNiYNNO8AMZNse8', '2022-12-06 07:37:31.717707'),
('osd2d997snkhwq56z9zxo82q16u1ifu9', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p5D0X:m_3nAl64QnBUz4OsndRwiA9ta90zPsgJzhT21DDzBCk', '2022-12-27 21:40:13.044662'),
('p0f8vtgtkf4roe4jgrykbsg689w8yo5t', '.eJxVjrkOwjAQRP_FtWX5yPpISc8XIGT5JIEolpykQIh_x0EpoJhidmaf5oWs29bBbkuqdoyoR4Dw78278EjzHsS7m2-FhDKvdfRkr5AjXci5xDSdju4fYHDL0L4zlSnokEGLTiZmQGrlgXuac_DcMJaNZioKriE4YAqS1CwoBkb4LrncoF9cLVNCPT_cvrjDyG_jFJuxrlb3RP1FUI4FZU0Uc2Oa9PX9AZ0QStM:1owMQ6:aLXJHGV0NKpyVVUQeJOufJKtInhxMSq73NFzt-7TtoY', '2022-12-03 11:54:02.985033'),
('p9tw7jywdf5q6w9yxm2iiwy47frbhyra', '.eJxVjDsOwjAQBe_iGlnrRP4sJT1nsNbrNQ4gR4qTCnF3iJQC2jcz76UibWuNW5clTlmd1aBOv1sifkjbQb5Tu82a57YuU9K7og_a9XXO8rwc7t9BpV6_NbtsgYAxsHhnPaORYNGMBCEYi55Tkjx6ccZBKQNQIV8kByGQhKjeH-W7OHg:1onzkt:b_KdASLYHYfSzCqYKY4yg_YVofxxWSOk_BrBOzmL4Lw', '2022-11-10 10:04:55.439235'),
('pd8qimt356qaelxiqfxrp2045rqthr16', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n18:mbqi7QTh1HIoV891WWI77JUBpOXmhCQnD9C38QHEpDU', '2022-12-15 17:06:34.777130'),
('pqvh5sbhte9z8nvgbocc50k0t051vvkf', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1pZ5jc:fQuKBw1ExrTD0M9YbTrdZf1SrkSwONYz5Ay-UQ5ESfg', '2023-03-20 07:58:16.034320'),
('q70fmy9j315u7k95easvjmti8tqn8pmx', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n15:EIdQQsseHEnKVBefnUsPr7wqCKBAaPAA2ofWR48SpE8', '2022-12-15 17:06:31.459282'),
('qjj0rpmi18amd6y32r6lmmxttpfkod8r', '.eJxVzsFqhDAQBuB3yVkkySQx8dj7PkFZZCaZrbaiELVQSt-9TvHQvXww-Wd-8q0GPPZxODauw1RUr0A1_98I8wcvEpR3XN7WNq_LXidqZaW90q29rYXnl2v3qWDEbTyv2aYM2XhmchG8TjniwxVtiaIOgGh0F22kRwTqIgRN5EvQmYGxBMtn6V9dXWdWvbkm-bFvFB3TXM5hwFrxS_WvxjndGAdJiEInBMELTgDBCkaQC5vujeJPXvanOq8lTOn-8wshQ1wo:1pV53n:rcKPQFm-XSJ9ekbYBFMhoWc11PlRa9sEnvWMu9siAR4', '2023-03-09 06:26:31.677136'),
('qp42qr5hru21k42u202qh3ycokef1zi3', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1oqwJ8:VPTUomLaP-ueSMpN2JokODaFxBPzSFtxnOiO1NWVHJA', '2022-11-18 13:00:26.325822'),
('r2rga7uldbj2nchnd63kownsyn91ymdq', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p7FGX:DCyjX8lX-ZlIf9DjvgBXP1e0utnvmE2bnVCIoiohv_A', '2023-01-02 12:29:09.210569'),
('r6papeg7yt7iul7vzgdrizl8r0r0ms02', '.eJxVjk0OwiAQhe_C2hChA5Uu3XsGMjCDVJuSlHZlvLvUdKHL9_flvYTHbc1-q7z4kcQgLuL06wWMT573gB4434uMZV6XMci9Io-0ylshnq5H9w-Qsea2hqACWUJLutegIwQgBAMGwdlkOofN6KI10JPBxOfEfUJ22gWl2WGDfnFLmVgM6lD7Y_v-ACfHQQ4:1pMRCQ:IoaqnhfE3ZW6W-6DMnVlMB2fofnOZcKWyJQn4gJFaBE', '2023-02-13 10:15:42.364424'),
('rjsbf8zlm3ceyjo55nysw7xedvg59tbx', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1pLhxE:pyr-YevE68NmTYuKJWi_vUhwkA6bJ6l4eOWcQPkqrQY', '2023-02-11 09:57:00.928853'),
('s9lj5ag5cygs20s158iz4gjou7m5wyt0', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1os0dp:I86Aqm2T11lzPQQ3P2betowDU3FCwZYlK5-Az_l6FMM', '2022-11-21 11:50:13.304079'),
('sgncpjwohklh7n70ckhoohuol9x5r2bx', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1oti6v:0bhOhc2Ov-qiGtJbGuCECBsgJQD6UNPK2WjBFx8u8GQ', '2022-11-26 04:27:17.052422'),
('sjnrvjgd7l3meqg3bg151bbacemaxygo', '.eJxVjs0KwjAQhN8l51KSmM1Pj959ApGw-bPV0kBqDyK-u4n0oJcPZmd2mBexuD1Gu62x2CmQgSjS_d4c-ntcmhFuuFxz7_PyKJPrW6Tf3bU_5RDn4579KxhxHeu3RvRoQGkPKQrJhBMJgvRgpKJ4YFUJppVkFIIROkjqU-DaQUIuqPK19FtX8hzJwHbVFkNH3DbNoQqLpeCTDGdOJe8qWAWYBt2gGmQDNIjL-wOXak6u:1p2Wia:h7GJVH71v-bzBFGvt7yMRC7oa62jBGW9_PwMPO_Xekc', '2022-12-20 12:06:36.334933'),
('so8qo7u9aj42wbddp9529akzby0raadu', '.eJxVjDsOwyAQBe9CHSHD8rPL9DmDtSwQnFggGbuKcvfYkYukfTNvXmzEbc3j1uIyToENDNjld_NIz1gOEB5Y7pVTLesyeX4o_KSN32qI8_V0_wIZW97fHqxMqMGSJoXOOEHSx5SMdwSBqAdUDpK1TkjTWSATUzAdWOw1KDJ79Jtb6hzZIN4fIrg8jw:1orB01:e0hDOW2QUy8TYPLvGPU8b-S2scYF99JjRH5Kn8Tf8Ws', '2022-11-19 04:41:41.740182'),
('spdj0llyhd6t9im9vkhjc71q53vl5cyq', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p2ZGc:Q_Iz5ELvMN5zOO9vpr6Zg7qQmCIENgcEhSTJHJTQPss', '2022-12-20 14:49:54.546169'),
('t27oslrhrhazj1k7iz05jes823blfr45', 'e30:1ooJJx:9YPQrAkyw4gKpeuFFYDHl824hSP_hCXxcAbH3AsfIS0', '2022-11-11 06:58:25.293465'),
('trpx0rfggcsyq4beipvzlyck6kq5n66m', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n1A:Gf_LTWJri9Xz_i40oRT2b-7kEovi5UXth6EhGOOO-PE', '2022-12-15 17:06:36.011378'),
('uev0d4o889ocq22a59s4thvjh4c7stw8', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n16:-n0GylobUQ6x9g4jsbnHzKWgpnI7Q4ZPIzC_2_jrpEs', '2022-12-15 17:06:32.255538'),
('uizj485x4p2ai9z65po07df3hp273lhc', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n17:w4w7YoPCPKZ3ErQWSKttKJCabOzSBcqm4OCDG7D8viY', '2022-12-15 17:06:33.172483'),
('ux5b7237efkcr9ldeqqsxt8vzx38rjf7', '.eJxVjDsOwjAQBe_iGlm72LFxSvqcIVqvFxyIbCmfCnF3EpQC2jfz5qV6Wpfcr7NM_ZBUqxp1-t0i8VPKDtKDyr1qrmWZhqh3RR901l1NMl4P9y-Qac7bW6xj35BwsAYs4E1ADBgIKURvU6RG0IALVsA7wQuhQ_QYDDMbCbJFv7mpjqLa8_sD_8w8Fw:1osJJH:lLa-Sy84iwCbpTenhXadVv673kLEh02X2s5FvcguGmE', '2022-11-22 07:46:15.039216'),
('v1m7wmek92zxnzci2qrio0acxrolwdai', '.eJxVjEEOgyAQRe_CuiE4YEGX3XsGMjBDtTWSgK6a3r3auGi3_73_XsLjto5-q1z8RKIXWlx-t4DxycsB6IHLPcuYl7VMQR6KPGmVQyaeb6f7FxixjvtbRcMpNgStDmyNbbBDaLrkVEzKxARXBYa0hZatBa2UhmSZHbXGuIBuj35zJc8senh_AAgoPBc:1ooeSr:OUJthAIdrTL2pVZxNoEyblvvy1meNgMoQyt4Ekjbm9s', '2022-11-12 05:33:01.497940'),
('vplno12lo37jouraw8723wm34cx13vyq', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n18:mbqi7QTh1HIoV891WWI77JUBpOXmhCQnD9C38QHEpDU', '2022-12-15 17:06:34.585215'),
('wc7qyz2fv2bll8biiwr7c6bf7jib2tjm', '.eJxVjr0OwjAMhN8lM4qU5r8jO89QObZLClUipe2EeHda1AE2n-_u073EANuah23hNkwkemHE5feXAJ9cDoMeUO5VYi1rm5I8IvJ0F3mrxPP1zP4BMix5byvlY3LWMI6JENniaCNoBqUje_KWUlSdDqBt9PsdtHNkOm9cQhV8t0O_uFZnFr061bFYvz8eTkBi:1plisr:3abghhAHrBVGzNE9jrCjEF1J5wpsap2452M2QgUak_k', '2023-04-24 04:12:01.289348'),
('wf6gknzcoyv6dg642j1i4wxfgm7lkh9l', '.eJxVjsEOgjAMht9lZ0Icuq1w9O4TGLN0aycoYWSAiTG-u8Nw0Fvb_-uX_yUsLnNrl4mT7Ug0AkTxe3Po7zysAd1wuMbSx2FOnStXpNzSqTxF4v64sX-CFqc2fwflvVaVVPUBCJQLjoDl3msDXlaAILE2TIZYkgOjvc6YAWNqCMhhl6VfXYo9i0Zu29pYF-KB45hniynhUzTny_sDJTZHeQ:1ouVI9:24CUaTBqtxj9o4U0dScbAJB7PH60SliEVMjjjgR2g14', '2022-11-28 08:58:09.908362'),
('wgboux0odxpqkn1b49wgwp7ntu7yrl21', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1oyhrB:QTCESwW2D1ut5Q29VqCQ30Xczci6nYzSrYREnVPJY00', '2022-12-09 23:11:41.859791'),
('x3ixqgb80ipczxx7l6nahz0nzzd7ks7v', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1otiUT:bXH6YlmVz_8mqHtvKNoCTVNLdhmvcePGRKjXrj58W6c', '2022-11-26 04:51:37.631813'),
('xaz2hty36skwupmq8icffhg7smzf9oqt', '.eJxVjDEOgzAQBP_iOrJsc4ChTJ83oLNvCSQISxiqKH8PRBRJuzM7L9Xxtg7dlrF0o6hWVeryuwWOT8wHkAfP96RjmtdlDPpQ9EmzviXBdD3dv8DAedjfHn1JBjE2Ho68eKlAaGprUYuzgRCEmYqGbOlMX3OwBQHOhOiKypk9-s0taYJq7fsDKZs8pg:1ooPRu:9HGQM34Z1dX3oFbd1h4mdHT9vWByIep4ZspYEkdkfi4', '2022-11-11 13:31:02.770462'),
('xgi56i1fqtvw6swz0iha2whvrvgacuaz', '.eJxVjk0OgyAQhe_CuiGDwIAuu-8ZDDBQbA0kqKumd682Ltrl-_vyXmx025rHbYltnIgNTAC7_JrehWcsR0IPV-6Vh1rWNnl-VPiZLvxWKc7Xs_sHyG7J-1r61MsQtETsMIEGCxCU6skYiMko9AqlQ0sgyEInAwJ6geSdFkaT3KFfXKtzZIM41XHZvD_p5z9-:1pQ5LR:CpHPtFctat0vjUBefPdpbgX0ousLrwtzQLdUcI0sYqo', '2023-02-23 11:44:05.437576'),
('xldbc9p1b50nazc1cx1cf372uw4diz7s', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p7wRf:RN739k0NpDoSbxGDb6EW3mvhn9I2diRBH33gNdrThQc', '2023-01-04 10:35:31.552091'),
('xxx2r0skmg195qxl2sxyjg4z8mbikus7', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1pEr0I:U7cqdPy8MTEY6Ejo8IIBNmX9ECIpUtlDaHPuPRYAO84', '2023-01-23 12:11:50.481055'),
('y6ublboy5zq9bfnc80ky6jva7kpa3zin', '.eJxVjDEOgzAQBP_iOrJsc4ChTJ83oLNvCSQISxiqKH8PRBRJuzM7L9Xxtg7dlrF0o6hWVeryuwWOT8wHkAfP96RjmtdlDPpQ9EmzviXBdD3dv8DAedjfHn1JBjE2Ho68eKlAaGprUYuzgRCEmYqGbOlMX3OwBQHOhOiKypk9-s0taYJq7fsDKZs8pg:1ooeXe:bpAFP7kiNUEt6l2JZJRFaDbCTZhZYXbiRakn1OO2S5U', '2022-11-12 05:37:58.838712'),
('y9maaqm1nwo6mb2aht4oej3grg5uz33n', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1oxQfB:ZcVj3c6Eao-aaG_v2u_B4Gc-z1wI7Ft21hkB_ahkGPw', '2022-12-06 10:38:01.080979'),
('yazitoyeifvywrz96iz08mscqsrifwii', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p7eUu:v1dfjvD_lRit1Pf5sDOFoTDE4zc3DBW6JGqt5dKl6ck', '2023-01-03 15:25:40.843248'),
('yq45bn91k3lxpt237p9q8ilf2w6i4we3', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p248r:TtwQz0nsdW7NpmWlwfsnE2U0pUnKpo1WwQhpKZhxPug', '2022-12-19 05:35:49.164604'),
('yty8t11828eqrv6jjri8w8mo3ptbciwg', '.eJxVjk0OgjAQhe_StWk6TJEOS_ecgUzbqaCEJhRWxrsLhoUu39-X91I9b-vQb0WWfoyqVVZdfj3P4SnzEcQHz_esQ57XZfT6qOgzLbrLUabb2f0DDFyGfY0hUEg1OiGICJTqRirjU8QoyYL3V0PkLKA1aCqAip1tgBpkYkcQdugXt-RJVAunOh7j-wPrDz-L:1pNYoe:b4iHUkS-i1GmlkutfkJc-bcjj23vPwrdezpegFxhhnk', '2023-02-16 12:35:48.378475'),
('yyo8csm9n106a5z7iwsxvqmozfz255s0', '.eJxVjs0KwjAQhN8l51CaJpufHr37BCIlPxtblRbSVhDx3d1KD3r4DrMzO8yLdX5d-m6dsXRDYi0Dxn9vwccbjpuRrn68TFWcxqUModoi1e7O1XFKeD_s2b-C3s89fedaY7Qxg5VKo3CgrQnQhDrnGBonRHZWmCQbC9GDMIDaimgEOBkU-kyl37oy3ZG1za62xYozfOC4kOh8Kf7J2pM0iksjCUHUXGpHWMIQmgBCnd8fnJlO6w:1p3Ey2:TI21zrPeXmtDicPWIZscAoAx0s8t7PgNbiw8hNyG48U', '2022-12-22 11:21:30.460507'),
('z7r6p2qqdm9odpg5udkngl2wadsp2kpy', '.eJxVjDsOwyAQBe9CHSHD8rPL9DmDtSwQnFggGbuKcvfYkYukfTNvXmzEbc3j1uIyToENDNjld_NIz1gOEB5Y7pVTLesyeX4o_KSN32qI8_V0_wIZW97fHqxMqMGSJoXOOEHSx5SMdwSBqAdUDpK1TkjTWSATUzAdWOw1KDJ79Jtb6hzZIN4fIrg8jw:1orINH:_j5JcsaaXw-deRpDBorlVOz5f55by7yOngxsR1n4r8U', '2022-11-19 12:34:11.193026'),
('zbd6z9qnl6tx3e52a2ibx3qd6xtp0bge', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1p0n1A:Gf_LTWJri9Xz_i40oRT2b-7kEovi5UXth6EhGOOO-PE', '2022-12-15 17:06:36.023784'),
('zdflixn94o1d00k0vmfey99bg36qx2rh', '.eJxVjjkOwjAQRe_iGlkZJ-MlJT1niOzxGAeiWMpSIe5OglxA-ben_xKD37c87CsvwxhFL1Bcfr3g6cnzGcSHn-9FUpm3ZQzyrMiarvJWIk_X2v0DZL_mY50azWQpoW07zeBQWxNQhSYlCsoBJGfBxFZZJI9gkLUFMoCuDR37dEC_uKVMLHpV1fm4e38A8iVABA:1othg4:1vP5-C6_DDKgUUoNHghYK51wgVP2O9Sku3kDqc7Z66g', '2022-11-26 03:59:32.020067'),
('ziawzdgi0z3mp9tfy60m95yvug0zpyyq', '.eJxVjksOwjAMRO-SNYpSu0k_S_acobIdlxaqRupnhbg7LcoClp438-SX6Wjfhm5fdenGaFqD5vKbMclT5xPEB833ZCXN2zKyPSs209XeUtTpmrt_goHW4Vg7X6lremwEuS6w5J645JorpwKggYF8CKUrUHwDApF6QHbiCZQPcki_uiVNatoiX-fH-P4AAMpAWg:1p5Pep:yt7lZa9C4tX-m5LlBzR6tDZQc9XeuPNLpQbY8hbHX_A', '2022-12-28 11:10:39.308516'),
('zy5ii3vg8eyi6rylmt1psfxuqscfak13', '.eJxVjskOgjAURf-la9LQ4XVg6d4vMKZ5nQQlNCmwMMZ_FwwLXd7p5L6Iw3Xp3Tqn6oZIOgKk-fU8hkea9iDecboVGsq01MHTvUKPdKbnEtN4Orp_gB7nflvnVqVgQgYjpErMgjLaA_dtzsFzy1i2hukouIGAwDQkZVjQDKzwMmHeoF9cLWMiHT_U_lg2xK_DGDfhsFZ8ku6iZKPE9f0BnlJIHw:1otOlQ:iNlssCNNuZOUTJYrYEF2GASioMDTS7pFRd2djudCBlY', '2022-11-25 07:47:48.443163');

-- --------------------------------------------------------

--
-- Table structure for table `vapp_vehicle_type`
--

CREATE TABLE `vapp_vehicle_type` (
  `id` bigint(20) NOT NULL,
  `type` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vapp_vehicle_type`
--

INSERT INTO `vapp_vehicle_type` (`id`, `type`) VALUES
(1, '1TON\r\n'),
(2, '2TON'),
(3, '3TON'),
(4, '7TON'),
(5, '10TON'),
(6, 'TRAILERS'),
(7, 'CRANES'),
(8, 'HATCH'),
(9, 'SEDAN'),
(10, 'SUV'),
(11, '18 TON');

-- --------------------------------------------------------

--
-- Table structure for table `webapp_buildpass_table`
--

CREATE TABLE `webapp_buildpass_table` (
  `id` bigint(20) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `company_name` varchar(200) DEFAULT NULL,
  `event_pass` tinyint(1) NOT NULL,
  `designation_id` int(11) DEFAULT NULL,
  `reg_created_at` datetime(6) NOT NULL,
  `exp_date` date DEFAULT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `mobile` varchar(200) DEFAULT NULL,
  `UID` varchar(200) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `print_count` int(11) DEFAULT NULL,
  `print_status` int(11) DEFAULT NULL,
  `other_designation` varchar(200) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `collected` int(11) DEFAULT 0,
  `approved_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `webapp_build_designation`
--

CREATE TABLE `webapp_build_designation` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `webapp_build_designation`
--

INSERT INTO `webapp_build_designation` (`id`, `designation`) VALUES
(0, 'OTHER'),
(1, 'POLICE'),
(2, 'DCT'),
(3, 'DCT AAA'),
(4, 'ORGANIZER'),
(5, 'ORGANIZER AAA'),
(7, 'EVENT STAFF'),
(8, 'CONTRACTOR'),
(18, 'VENDOR'),
(19, 'CLEANER'),
(21, 'F&B VENDOR'),
(23, 'SECURITY');

-- --------------------------------------------------------

--
-- Table structure for table `webapp_eventpass_designation`
--

CREATE TABLE `webapp_eventpass_designation` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `webapp_eventpass_designation`
--

INSERT INTO `webapp_eventpass_designation` (`id`, `designation`) VALUES
(0, 'OTHER'),
(1, 'POLICE'),
(2, 'DCT'),
(3, 'DCT AAA'),
(4, 'ORGANIZER'),
(5, 'ORGANIZER AAA'),
(7, 'EVENT STAFF'),
(8, 'CONTRACTOR'),
(9, 'PROTOCOL'),
(10, 'POLICE VOLUNTEERS'),
(11, 'ROAMING PERFORMERS'),
(12, 'LIVE AREA STAGE ARTIST'),
(13, 'FOOD HUB STAGE ARTIST'),
(14, 'EVENT STAFF LIVE ARENA STAGE'),
(15, 'EVENT STAFF FOOD HUB STAGE'),
(16, 'SPONSORS OR PARTNERS'),
(17, 'MEDIA'),
(18, 'VENDOR'),
(19, 'CLEANER'),
(20, 'LIVE AREANA CLEANER'),
(21, 'F&B VENDOR'),
(22, 'PRODUCTION'),
(23, 'SECURITY'),
(24, 'VOLUNTEERS'),
(26, 'VISITOR'),
(35, 'ORGANIZER AAA STAR'),
(36, 'EVENT STAFF LIVE ARENA'),
(37, 'F&B VENDOR LIVE ARENA'),
(38, 'VOLUNTEERS LIVE ARENA'),
(39, 'PROTOCOL AAA'),
(40, 'CONCERT STAGE ARTIST'),
(41, 'BUSKER STAGE ARTIST'),
(42, 'EVENT STAFF CONCERT STAGE'),
(43, 'EVENT STAFF BUSKER STAGE'),
(44, 'CONCERT ARENA CLEANER'),
(45, 'EVENT STAFF CONCERT ARENA'),
(46, 'VOLUNTEER CONCERT ARENA');

-- --------------------------------------------------------

--
-- Table structure for table `webapp_eventpass_image_db`
--

CREATE TABLE `webapp_eventpass_image_db` (
  `id` bigint(20) NOT NULL,
  `pass_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `webapp_eventpass_image_db`
--

INSERT INTO `webapp_eventpass_image_db` (`id`, `pass_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `webapp_eventpass_table`
--

CREATE TABLE `webapp_eventpass_table` (
  `id` bigint(20) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `company_name` varchar(200) DEFAULT NULL,
  `designation_id` int(11) DEFAULT NULL,
  `reg_created_at` datetime(6) NOT NULL,
  `exp_date` date DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `mobile` varchar(200) DEFAULT NULL,
  `UID` varchar(200) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `print_count` int(11) DEFAULT NULL,
  `print_status` int(11) DEFAULT NULL,
  `id_proof` varchar(200) DEFAULT NULL,
  `id_proof_cat` int(11) DEFAULT NULL,
  `nationality` varchar(200) DEFAULT NULL,
  `other_designation` varchar(200) DEFAULT NULL,
  `id_proof_img` varchar(100) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `id_proof_back_img` varchar(100) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `collected` int(11) DEFAULT 0,
  `approved_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `webapp_user_db`
--

CREATE TABLE `webapp_user_db` (
  `id` bigint(20) NOT NULL,
  `username` varchar(200) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `is_online` int(11) DEFAULT NULL,
  `last_req_updated_time` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `webapp_user_db`
--

INSERT INTO `webapp_user_db` (`id`, `username`, `role`, `is_online`, `last_req_updated_time`) VALUES
(1, 'sreenath', 1, 0, '2023-02-22 05:40:06.004083'),
(3, 'Don', 1, 1, '2023-03-30 11:15:27.202688'),
(4, 'INFOMEUSER', 2, NULL, NULL),
(5, 'Shadin', 1, 0, '2023-02-27 08:30:24.133231'),
(6, 'Uvais', 1, 0, '2023-03-20 08:57:21.317630'),
(7, 'kochi_dev', 1, 0, '2023-02-25 07:05:19.988142'),
(8, 'dazadmin', 1, 0, '2023-03-14 19:39:39.511817');

-- --------------------------------------------------------

--
-- Table structure for table `webapp_vapp_category`
--

CREATE TABLE `webapp_vapp_category` (
  `id` bigint(20) NOT NULL,
  `category` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `webapp_vapp_category`
--

INSERT INTO `webapp_vapp_category` (`id`, `category`) VALUES
(1, 'VIP'),
(2, 'ACCREDITED PARKING'),
(3, 'VALET PARKING'),
(4, 'DELIVERY'),
(5, 'PARKING');

-- --------------------------------------------------------

--
-- Table structure for table `webapp_vapp_table`
--

CREATE TABLE `webapp_vapp_table` (
  `id` bigint(20) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `vehicle_number` varchar(200) DEFAULT NULL,
  `mobile_number` varchar(200) DEFAULT NULL,
  `company_name` varchar(200) DEFAULT NULL,
  `reg_created_at` datetime(6) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `exp_date` date DEFAULT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `UID` varchar(200) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `print_count` int(11) DEFAULT NULL,
  `print_status` int(11) DEFAULT NULL,
  `approved_date` date DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `emirates_id` varchar(100) DEFAULT NULL,
  `mulkya` varchar(100) DEFAULT NULL,
  `emirates_id_back` varchar(100) DEFAULT NULL,
  `vehicle_type_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `collected` int(11) DEFAULT 0,
  `approved_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_speakerregistrations`
--
ALTER TABLE `app_speakerregistrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

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
-- Indexes for table `vapp_vehicle_type`
--
ALTER TABLE `vapp_vehicle_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `webapp_buildpass_table`
--
ALTER TABLE `webapp_buildpass_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `webapp_build_designation`
--
ALTER TABLE `webapp_build_designation`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_speakerregistrations`
--
ALTER TABLE `app_speakerregistrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
