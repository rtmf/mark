USE mark;
DROP PROCEDURE IF EXISTS mgen;
DELIMITER //
CREATE PROCEDURE mgen()
BEGIN
	DECLARE xci INTEGER DEFAULT NULL;
	DECLARE xrs VARCHAR(65535) DEFAULT "";
	DECLARE xrv FLOAT DEFAULT NULL;
	DECLARE xcw VARCHAR(255) DEFAULT "";
	DECLARE xns INTEGER DEFAULT NULL;
	DECLARE xwa INTEGER DEFAULT NULL;
	DECLARE xwb INTEGER DEFAULT NULL;
	DECLARE xwc INTEGER DEFAULT NULL;

	SELECT id INTO xns FROM words WHERE word="";
	SET xwa=xns;
	SET xwb=xns;
	SET xwc=xns;
	genloop: LOOP
		SELECT RAND() INTO xrv;
		SELECT d INTO xci FROM trigrams WHERE a=xwa AND b=xwb AND c=xwc AND f>=xrv ORDER BY f LIMIT 1;
		IF xci = xns THEN
			LEAVE genloop;
		END IF;
		SELECT word INTO xcw FROM words WHERE id=xci;
		IF xwc != xns THEN
			SELECT CONCAT_WS(" ",xrs,xcw) INTO xrs;
		ELSE
			SET xrs=xcw;
		END IF;
		SET xwa=xwb;
		SET xwb=xwc;
		SET xwc=xci;
	END LOOP;
	SELECT xrs;
END
//
