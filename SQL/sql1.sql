CREATE TABLE IF NOT EXISTS `device_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `device_id` int(11) NOT NULL,
  `device_type` varchar(64) NOT NULL,
  `ver` varchar(64) NOT NULL COMMENT '是否完成',
  `create_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

insert into device_info (id, device_id, device_type, ver, create_time) values(1, 1, 'A', '1.0', 1482214350), (2, 1, 'B', '1.1', 1482214350);
