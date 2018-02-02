use homeData;

CREATE TABLE person (
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (id));
    
INSERT INTO person (name) VALUES ('Luciano');

CREATE TABLE nightSlept (
	person MEDIUMINT NOT NULL,
    date DATE NOT NULL,
    timeStart DATETIME,
    timeFinish DATETIME,
    generalFeeling TINYINT,
    howTiredByNight TINYINT,
    howTiredByMorning TINYINT,
    alcohol TINYINT,
    chocolateCoffeeSimilar TINYINT,
    tea TINYINT,
    water TINYINT,
    protractedComputerUse TINYINT,
    redshiftOn TINYINT,
    holidayBefore BIT(1),
    holidayAfter BIT(1),
    usedSleepCycle BIT(1),
    PRIMARY KEY (person, date),
    FOREIGN KEY (person) REFERENCES person(id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE);
        
INSERT INTO nightSlept (person, date, timeStart, timeFinish, generalFeeling, 
	howTiredByNight, howTiredByMorning, alcohol, chocolateCoffeeSimilar, tea, water, protractedComputerUse,
	redshiftOn, holidayBefore, holidayAfter, usedSleepCycle) VALUES (1, '2018-02-01',
    '2018-02-02 00:48:00',
    '2018-02-02 07:20:00',
    5, 1, 0, 0, 0, 0, 1, 5, 1, b'1', b'1', b'0');
    
CREATE TABLE temperature (
    timeDate DATETIME,
    value DECIMAL(3,1),
    PRIMARY KEY (timeDate));
    
CREATE USER temperatureLogger@'192.168.1.0/255.255.255.0' IDENTIFIED BY 'tempLogger123';
GRANT INSERT ON homeData.temperature TO temperatureLogger@'192.168.1.0/255.255.255.0';
GRANT SELECT ON homeData.temperature TO temperatureLogger@'192.168.1.0/255.255.255.0';
FLUSH PRIVILEGES;

INSERT INTO temperature (timeDate, value) VALUES ('2018-02-01 11:40:00', 39.5);

CREATE USER nightLogger@'192.168.1.0/255.255.255.0' IDENTIFIED BY 'nightLogger123';
GRANT INSERT ON homeData.nightSlept TO nightLogger@'192.168.1.0/255.255.255.0';
GRANT SELECT ON homeData.nightSlept TO nightLogger@'192.168.1.0/255.255.255.0';
GRANT SELECT ON homeData.temperature TO nightLogger@'192.168.1.0/255.255.255.0';
FLUSH PRIVILEGES;