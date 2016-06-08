CREATE TABLE sandbox.workshop_data (
	name VARCHAR(30),
	msisdn INT,
	call_secs FLOAT,
	amount FLOAT
);

INSERT INTO sandbox.workshop_data (name,msisdn,call_secs,amount) values ('Alice', 123456789, 42.5,20400);
INSERT INTO sandbox.workshop_data (name,msisdn,call_secs,amount) values ('Bob', 987654321, 18.3,12000);
