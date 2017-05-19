INSERT INTO form_race VALUES(50,'BLANCHE');
INSERT INTO form_race VALUES(38,'NOIR');
INSERT INTO form_race VALUES(37,'VERTE');
INSERT INTO form_race VALUES(0,'NA');

INSERT INTO form_cheptel VALUES(2,'PHILLIPE');
INSERT INTO form_cheptel VALUES(1,'JEAN');
INSERT INTO form_cheptel VALUES(78355888,'HENRY');
INSERT INTO form_cheptel VALUES(0,'NA');

INSERT INTO form_preleveur VALUES(50,'PHILLIPE');

select form_genotypage.auto_increment_id,form_prelevement.auto_increment_id from form_genotypage RIGHT JOIN form_prelevement ON form_prelevement.auto_increment_id = form_genotypage.prelevement_id ORDER BY form_prelevement.auto_increment_id ASC ;

